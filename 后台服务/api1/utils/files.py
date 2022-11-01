"""
# @Time    : 2022/10/20 20:36
# @Author  : violet
# @explain : 文件处理
"""

from django.core.files.uploadedfile import UploadedFile
from django.conf import settings
from .. import models
import os
import time


def saveHeadPortrait(image: UploadedFile, user: models.User):
    """
    保存用户头像
    :param image: 用户头像
    :param user: 用户
    :return: 【username_time.now_headPortrait.jpg】
    """

    # 1.删除原有用户头像
    if user.headPortrait != '/static/user/default.jpg':
        if os.path.isfile(f'{settings.BASE_DIR}' + user.headPortrait):
            os.remove(f'{settings.BASE_DIR}' + user.headPortrait)

    # suffix = image.name.split('.')[-1]
    suffix = 'jpg'
    filename = f'{user.username}_{str(time.time()).split(".")[0]}_headPortrait.{suffix}'
    filepath = f'{settings.MY_USER_UPLOAD_PATH}\\{filename}'

    with open(filepath, 'wb') as fp:
        for chunk in image.chunks():
            fp.write(chunk)

    return f'/static/user/{filename}'
