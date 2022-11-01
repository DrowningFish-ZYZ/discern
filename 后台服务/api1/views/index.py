"""
# @Time    : 2022/10/26 18:00
# @Author  : violet
# @explain : 主页逻辑
"""
import os

from rest_framework.generics import GenericAPIView
from rest_framework.request import Request
from rest_framework.response import Response
from .. import models, utils
from django.db import transaction
from rest_framework import status
from datetime import date
from django.conf import settings


class ModelAPIView(GenericAPIView):
    """ 获取模型数据 """

    queryset = models.DiscernType.objects.all()
    serializer_class = utils.serializers.DiscernTypeSerializer

    def get(self, request: Request) -> Response:
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class DiscernAPIView(GenericAPIView):
    """ 识别图像, 1: 根据选择的模型去识别上传的图像；2: 再将本次识别记录存入用户的历史记录 """

    # 限流
    throttle_scope = 'discern'

    @transaction.atomic
    def post(self, request: Request, pk: int) -> Response:
        # 0.开启事务
        tid = transaction.savepoint()
        try:
            # 1. 识别
            user = models.User.objects.get(pk=pk)
            model = models.DiscernModel.objects.get(pk=request.data['model'])
            path, result = utils.discern.start(request.FILES.get('image'), model)
            if result == '':
                return Response({'message': '识别失败'}, status=status.HTTP_400_BAD_REQUEST)

            # 2. 识别完毕将数据记录
            models.Record.objects.create(image=path, date=date.today(), user=user, discernType=model.discernType,
                                         discernModel=model, result=result)
            # 5.提交事务
            transaction.savepoint_commit(tid)
            return Response(path, status=status.HTTP_201_CREATED)
        except Exception as e:
            print(e)
            # 回滚事务
            transaction.savepoint_rollback(tid)
            return Response({'message': '用户数据异常'}, status=status.HTTP_400_BAD_REQUEST)


class RecordAPIView(GenericAPIView):
    """ 根据用户去获取对应的历史记录 """

    serializer_class = utils.serializers.RecordSerializer

    def get(self, request: Request, pk: int) -> Response:
        user = models.User.objects.get(pk=pk)
        queryset = user.record_set.all()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def delete(self, request: Request, pk: int):
        """ 获取对应的用户和历史记录，删除本地文件，删除数据记录，返回新的历史记录 """
        user = models.User.objects.get(pk=pk)
        record = models.Record.objects.get(pk=request.data['recordID'])
        os.remove(f'{settings.BASE_DIR}' + record.image)
        print(f'{settings.BASE_DIR}' + record.image)
        record.delete()
        queryset = user.record_set.all()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class DetailAPIView(GenericAPIView):

    queryset = models.Detail.objects.all()
    serializer_class = utils.serializers.DetailSerializer

    """ 获取识别结果详情 """
    def get(self, request: Request):
        query = request.query_params['query']
        query = query.split(',')[:-1]
        query = list(map(lambda item: ' '.join(item.split(' ')[:-1]), query))
        queryset = self.get_queryset().filter(label__in=query).distinct()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)