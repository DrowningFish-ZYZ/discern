from django.db import models


# Create your models here.
# ============================================================= 用户相关 =============================================================
class User(models.Model):
    """ 普通用户 """
    gender_choices = ((0, '男'), (1, '女'))

    username = models.CharField(verbose_name='用户名', unique=True, max_length=32)
    password = models.CharField(verbose_name='密码', max_length=32)
    gender = models.SmallIntegerField(verbose_name='性别', choices=gender_choices, default=0)
    phone = models.CharField(verbose_name='电话号码', max_length=11, default='')
    email = models.EmailField(verbose_name='邮箱', default='')
    headPortrait = models.CharField(verbose_name='头像', max_length=128, default='')
    sq = models.CharField(verbose_name='密保', max_length=32, default='')
    sqKey = models.CharField(verbose_name='密保密码', max_length=32, default='')
    info = models.CharField(verbose_name='个人简介', max_length=32, default='')
    delete = models.BooleanField(verbose_name='禁用', default=False)

    def __str__(self):
        return f'<id:{self.id}, username: {self.username}>'


# ============================================================= 识别模型相关 =============================================================
class DiscernType(models.Model):
    """ 识别大类, 如: 【基本识别，动漫识别...】 """

    label = models.CharField(verbose_name='识别类别名称', max_length=32, unique=True)

    def __str__(self):
        return self.label


class DiscernModel(models.Model):
    """ 识别大类对应的具体模型, 如: 【coco2018模型...】 """
    label = models.CharField(verbose_name='具体模型名称', max_length=32, default='', unique=True)
    name = models.CharField(verbose_name='模型内部名称', max_length=32)
    discernType = models.ForeignKey(DiscernType, on_delete=models.CASCADE, default='')

    def __str__(self):
        return self.label


class Record(models.Model):
    """ 识别历史记录 """
    image = models.CharField(verbose_name='识别完毕的图像', max_length=256)
    date = models.DateField(verbose_name='识别时间')
    user = models.ForeignKey(User, verbose_name='这条记录对应的用户', on_delete=models.CASCADE, default='')
    discernType = models.ForeignKey(DiscernType, verbose_name='识别类型', on_delete=models.CASCADE)
    discernModel = models.ForeignKey(DiscernModel, verbose_name='使用的模型', on_delete=models.CASCADE)
    result = models.CharField(max_length=256, verbose_name='识别结果')  # 猫 0.99,狗 0.99,猪 0.99,


class Detail(models.Model):
    """ 识别出的物体详细信息 """
    label = models.CharField(verbose_name='识别出的物体标签', max_length=32)
    info = models.TextField(verbose_name='详细描述')
