"""
# @Time    : 2022/10/20 13:50
# @Author  : violet
# @explain : JWT 用户认证系统
"""

from rest_framework.authentication import BaseAuthentication
from rest_framework import exceptions
from rest_framework_jwt.utils import jwt_decode_handler
from .. import models


class JWTUserAuthentication(BaseAuthentication):
    """ 普通用户 JWT 认证 """
    def authenticate(self, request):
        try:
            token = request.META.get('HTTP_TOKEN')
            data = jwt_decode_handler(token)
            if not models.User.objects.filter(username=data['username']).exists():
                raise exceptions.AuthenticationFailed('认证用户不存在')
        except Exception as e:
            print(e)
            raise exceptions.AuthenticationFailed('用户未登录，请登录')