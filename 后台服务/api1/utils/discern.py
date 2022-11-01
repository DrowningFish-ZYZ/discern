"""
# @Time    : 2022/10/26 19:05
# @Author  : violet
# @explain : 识别模块
"""

from django.core.files.uploadedfile import UploadedFile
from PIL import Image
from yolo import utils, predict
from django.conf import settings
from .. import models
import uuid


def start(image: UploadedFile, model: models.DiscernModel) -> tuple:
    """
    识别上传的图片
    :param image: 要识别的图片
    :param model: 选择的模型
    :return: 识别完毕后的图像存储位置, 识别结果
    """

    # 1.根据 model 构建对应的模型，然后识别上传图像并保存
    image = Image.open(image)
    pred = predict.Predict(
        classes=utils.load_classes(f'{settings.YOLO_DIR}/infos/{model.name}_classes.txt'),
        anchors=utils.load_anchors(f'{settings.YOLO_DIR}/infos/anchors.txt'),
        model_path=f'{settings.YOLO_DIR}/models_t/{model.name}_weights.h5',
        font_path=f'{settings.YOLO_DIR}/font/msyh.ttc'
    )
    image = pred.image(image)

    # 2.创建一个独一无二的名字，并保存图像
    filename = str(uuid.uuid4()).split('-')[-1] + '.jpg'
    if pred.label != '': image.save(f'{settings.MY_DISCERN_UPLOAD_PATH}\\{filename}')
    return f'/static/discern/{filename}', pred.label