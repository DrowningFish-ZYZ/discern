"""
# @Time    : 2022/10/20 14:38
# @Author  : violet
# @explain : 
"""

from rest_framework.generics import GenericAPIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from django.db import transaction
from .. import utils, models


# ------------------------------------------------ 普通用户登录视图【无需登录即可访问】 ------------------------------------------------
# 用户登录
class LoginAPIView(GenericAPIView):
    # 公共属性
    serializer_class = utils.serializers.UserLoginSerializer

    # 用户认证【局部认证会覆盖全局认证】
    authentication_classes = []

    def post(self, request: Request):
        """ 校验登录数据，校验成功颁发 token 签证 """
        # 1.获取前端传递的用户名与密码【username，password】，并进行校验
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            # 2.校验通过根据其用户生成对应的 token
            token = serializer.validated_data.get('token')
            user = serializer.validated_data.get('user')
            # 3.返回对应数据
            return Response({
                'token': token,
                'username': user.username,
                'id': user.id,
                'headPortrait': user.headPortrait,
                'gender': user.gender,
                'info': user.info
            })

        return Response({'message': '用户名或密码错误'}, status=status.HTTP_400_BAD_REQUEST)


# 用户注册
class RegisterAPIView(GenericAPIView):
    # 公共属性
    serializer_class = utils.serializers.UserRegisterSerializer

    # 用户认证【局部认证会覆盖全局认证】
    authentication_classes = []

    @transaction.atomic
    def post(self, request: Request):
        """ 注册用户 """
        # 0.开启事务
        tid = transaction.savepoint()
        result = '服务器错误'
        try:
            # 1.获取前端传递的用户名与密码【username，password】，并进行校验
            serializer = self.get_serializer(data=request.data)
            if serializer.is_valid():
                # 2.字段校验完毕，保存数据
                result = serializer.save()
                if isinstance(result, models.User):
                    # 3.保存成功，查看是否有上传用户头像，如果存在便构建用户头像
                    if request.FILES.get('image'):
                        headPortrait = utils.files.saveHeadPortrait(request.FILES.get('image'), result)
                        # 4.修改用户的头像地址
                        result.headPortrait = headPortrait

                    else: result.headPortrait = '/static/user/default.jpg'  # 如果没有上传头像，设置默认头像
                    result.save()
                    # 5.提交事务
                    transaction.savepoint_commit(tid)
                    # 返回响应【201 创建成功】
                    return Response('ok', status=status.HTTP_201_CREATED)

            return Response({'message': result}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print('------------ error ---------------- : ', e)
            # 回滚事务
            transaction.savepoint_rollback(tid)
            # 返回响应
            return Response({'message': result}, status=status.HTTP_400_BAD_REQUEST)


# 用户忘记密码
class ForgetPasswordAPIView(GenericAPIView):
    queryset = models.User.objects.all()
    serializer_class = utils.serializers.UserForgetPasswordSerializer

    # 用户认证【局部认证会覆盖全局认证】
    authentication_classes = []

    def post(self, request: Request, step: int):
        if step == 1:
            """ 第一步: 根据 username 获取用户并返回密保问题 """
            try:
                user = self.get_queryset().get(**request.data)
                return Response({'sq': user.sq}, status=status.HTTP_200_OK)
            except Exception as e:
                print(e)
                return Response({'message': '账户不正确'}, status=status.HTTP_400_BAD_REQUEST)

        elif step == 2:
            """ 第二步: 根据 username，sq，sqKey 获取用户，获取成功返回 ok """
            try:
                self.get_queryset().get(**request.data)
                return Response('ok', status=status.HTTP_200_OK)
            except Exception as e:
                print(e)
                return Response({'message': '密保不正确'}, status=status.HTTP_400_BAD_REQUEST)

        elif step == 3:
            """ 最后一步: 根据 username，sq，sqKey 获取用户, 序列化校验密码, 成功便入库存储 """
            try:
                user = self.get_queryset().get(username=request.data['username'], sq=request.data['sq'],
                                               sqKey=request.data['sqKey'])
                serializer = self.get_serializer(user, data=request.data)
                serializer.is_valid(raise_exception=True)
                serializer.save()
                return Response('ok', status=status.HTTP_200_OK)
            except Exception as e:
                print(e)
                return Response({'message': '错误'}, status=status.HTTP_400_BAD_REQUEST)

        return Response({'message': '不正常的请求'}, status=status.HTTP_400_BAD_REQUEST)


# ------------------------------------------------ 普通用户账户安全逻辑视图【需登录才可访问】 ------------------------------------------------
# POST: 用户重置密码
class ResetPasswordAPIView(GenericAPIView):
    """ 重置密码视图 """

    serializer_class = utils.serializers.UserForgetPasswordSerializer
    queryset = models.User.objects.all()

    def post(self, request: Request, pk: int):
        """ 重置用户密码, 根据用户 ID 获取对应的用户, 再判断旧密码是否与新密码一致, 一致便可重设密码 """
        try:
            user = self.get_queryset().get(pk=pk)
            if user.password == utils.password.md5(request.data['oldPassword']):
                serializer = self.get_serializer(user, data={'password': request.data['oldPassword']})
                if serializer.is_valid():
                    serializer.save()
                    return Response('ok', status=status.HTTP_200_OK)

            return Response({'message': '密码错误'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)
            return Response({'message': '异常'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# POST: 用户重置密保
class ResetSQAPIView(GenericAPIView):
    """ 重置密保视图 """

    serializer_class = utils.serializers.UserResetSQSerializer
    queryset = models.User.objects.all()

    def post(self, request: Request, pk: int):
        """ 重置密保，根据用户 ID 获取对应用户，再判断原密保是否与当前密保一致，一致便重设密保 """
        try:
            user = self.get_queryset().get(pk=pk)
            if user.sq == request.data['oldSq'] and user.sqKey == request.data['oldSqKey']:
                serializer = self.get_serializer(user, data={'sq': request.data['newSq'], 'sqKey': request.data['newSqKey']})
                if serializer.is_valid():
                    serializer.save()
                    return Response('ok', status=status.HTTP_201_CREATED)

            return Response({'message': '密保错误'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)
            return Response({'message': '异常'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# POST: 重置用户头像
class ResetHeadPortraitAPIView(GenericAPIView):

    queryset = models.User.objects.all()

    # 自定义限流
    throttle_scope = 'upload'

    def post(self, request: Request, pk: int):
        """ 重置用户头像 """
        try:
            user = self.get_queryset().get(pk=pk)
            headPortrait = utils.files.saveHeadPortrait(request.FILES.get('image'), user)
            user.headPortrait = headPortrait
            user.save()
            return Response({'headPortrait': user.headPortrait}, status=status.HTTP_201_CREATED)
        except Exception as e:
            print(e)
            return Response({'message': '错误'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# GET: 获取用户详情【邮箱，电话】
# PUT: 修改用户信息
class UserAPIView(GenericAPIView):

    serializer_class = utils.serializers.UserUpdateSerializer
    queryset = models.User.objects.all()

    def get(self, request: Request, pk: int):
        """ 根据 id 获取用户，并返回邮箱和电话 """
        try:
            user = self.get_queryset().get(pk=pk)
            return Response({'email': user.email, 'phone': user.phone}, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({'message': '错误'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request: Request, pk: int):
        try:
            user = self.get_queryset().get(pk=pk)
            serializer = self.get_serializer(user, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.validated_data, status=status.HTTP_201_CREATED)

            return Response({'message': '数据错误'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)
            return Response({'message': '错误'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)