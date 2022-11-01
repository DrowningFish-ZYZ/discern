"""
# @Time    : 2022/10/20 14:44
# @Author  : violet
# @explain : 序列化器
"""

from rest_framework import serializers
from rest_framework import exceptions
from rest_framework_jwt.utils import jwt_encode_handler
from .. import models, utils
import datetime


# --------------------------------------- 普通用户登录序列化器 ---------------------------------------
# 用户登录数据校验
class UserLoginSerializer(serializers.ModelSerializer):
    """ 用户登录序列化器 """
    username = serializers.CharField(max_length=32, min_length=4)
    password = serializers.CharField(max_length=32, min_length=4)

    class Meta:
        model = models.User
        fields = ['username', 'password']

    def validate(self, attrs):
        """ 多字段校验 """
        try:
            # 密码加密
            attrs['password'] = utils.password.md5(attrs['password'])
            # 对用户名与密码校验，校验成功便生成 token 并返回对应用户
            user = models.User.objects.get(**attrs)
            token = jwt_encode_handler({'username': user.username, 'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1)})
            return {'user': user, 'token': token}
        except Exception as e:
            print(e)
            raise exceptions.ValidationError('用户名或密码错误')

    def validate_username(self, data):
        return data

# 用户注册数据校验
class UserRegisterSerializer(serializers.ModelSerializer):
    """ 用户注册校验 """
    gender_choices = ((0, '男'), (1, '女'))

    username = serializers.CharField(max_length=32, min_length=4)
    password = serializers.CharField(max_length=32, min_length=4)
    email = serializers.CharField(allow_blank=True, default='')
    phone = serializers.CharField(allow_blank=True, default='')
    gender = serializers.ChoiceField(choices=gender_choices, default=0, allow_blank=True)
    headPortrait = serializers.CharField(allow_blank=True, default='')
    sq = serializers.CharField(max_length=32, default='', allow_blank=True)
    sqKey = serializers.CharField(max_length=32, default='', allow_blank=True)
    info = serializers.CharField(max_length=15, default='', allow_blank=True)

    class Meta:
        model = models.User
        fields = '__all__'

    def create(self, validated_data: dict):
        """ 创建新数据: 1.确保用户名未存在，2.对密码进行加密 """
        if models.User.objects.filter(username=validated_data['username']).exists():
            return '用户名已经存在'

        validated_data['password'] = utils.password.md5(validated_data['password'])
        return models.User.objects.create(**validated_data)

# 用户忘记密码数据校验
class UserForgetPasswordSerializer(serializers.ModelSerializer):
    """ 用户忘记密码数据校验 """

    password = serializers.CharField(max_length=32, min_length=4)

    class Meta:
        model = models.User
        fields = ['password']

    def update(self, instance: models.User, validated_data):
        validated_data['password'] = utils.password.md5(validated_data['password'])
        instance.password = validated_data['password']
        instance.save()
        return instance

# -----------------------------------------------------------------------------------------------
# 用户重置密保数据校验
class UserResetSQSerializer(serializers.ModelSerializer):
    sq = serializers.CharField(max_length=32, default='', allow_blank=True)
    sqKey = serializers.CharField(max_length=32, default='', allow_blank=True)

    def update(self, instance: models.User, validated_data: dict):
        instance.sq = validated_data['sq']
        instance.sqKey = validated_data['sqKey']
        instance.save()
        return instance

    class Meta:
        model = models.User
        fields = ['sq', 'sqKey']


# 用户更改个人信息数据校验
class UserUpdateSerializer(serializers.ModelSerializer):
    gender_choices = ((0, '男'), (1, '女'))

    email = serializers.CharField(allow_blank=True, default='')
    phone = serializers.CharField(allow_blank=True, default='')
    gender = serializers.ChoiceField(choices=gender_choices, default=0, allow_blank=True)
    info = serializers.CharField(max_length=15, default='', allow_blank=True)

    class Meta:
        model = models.User
        fields = ['email', 'phone', 'gender', 'info']

    def update(self, instance: models.User, validated_data: dict):
        instance.email = validated_data['email']
        instance.phone = validated_data['phone']
        instance.gender = validated_data['gender']
        instance.info = validated_data['info']
        instance.save()
        return instance



# --------------------------------------- 模型序列化器 ---------------------------------------
class DiscernModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.DiscernModel
        fields = '__all__'


class DiscernTypeSerializer(serializers.ModelSerializer):
    discernmodel_set = DiscernModelSerializer(many=True)

    class Meta:
        model = models.DiscernType
        fields = '__all__'


# --------------------------------------- 历史记录序列化器 ---------------------------------------
class RecordSerializer(serializers.ModelSerializer):
    discernType = serializers.StringRelatedField()
    discernModel = serializers.StringRelatedField()

    class Meta:
        model = models.Record
        fields = ['id', 'image', 'date', 'result', 'discernType', 'discernModel']



# --------------------------------------- 识别物品详情序列化器 ---------------------------------------
class DetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Detail
        fields = ['label', 'info']