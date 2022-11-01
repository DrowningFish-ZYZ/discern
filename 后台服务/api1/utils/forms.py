"""
# @Time    : 2022/10/29 19:02
# @Author  : violet
# @explain : Django form 组件
"""

from django import forms
from django.contrib.auth.models import User
from .. import models, utils


# ================================================ 用户表单组件 ================================================
class UserModelForm(forms.ModelForm):
    username = forms.CharField(required=True, min_length=4, max_length=8)
    password = forms.CharField(required=True, min_length=4, max_length=15)
    headPortrait = forms.CharField(required=True, max_length=128)
    phone = forms.CharField(required=False)
    email = forms.CharField(required=False)
    info = forms.CharField(required=False)

    class Meta:
        model = models.User
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs = {'class': 'form-control', 'placeholder': field.label}
            if name == 'headPortrait': field.widget.attrs['value'] = '/static/user/default.jpg'
            if name == 'delete': field.widget.attrs['class'] = 'checkbox'

    def save(self, commit=True):
        self.instance.password = utils.password.md5(self.data['password'])
        self.instance.save()


class UserUpdateModelForm(forms.ModelForm):
    username = forms.CharField(required=True, min_length=4, max_length=8)
    headPortrait = forms.CharField(required=True, max_length=128)
    phone = forms.CharField(required=False)
    email = forms.CharField(required=False)
    info = forms.CharField(required=False)

    class Meta:
        model = models.User
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs = {'class': 'form-control', 'placeholder': field.label}
            if name == 'headPortrait': field.widget.attrs['value'] = '/static/user/default.jpg'
            if name == 'delete': field.widget.attrs['class'] = 'checkbox'
            if name == 'password': field.widget.attrs['readonly'] = "readonly"


# ================================================ 识别类型表单组件 ================================================
class DiscernTypeForm(forms.ModelForm):
    class Meta:
        model = models.DiscernType
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs = {'class': 'form-control', 'placeholder': field.label}


# ================================================ 识别模型表单组件 ================================================
class DiscernModelForm(forms.ModelForm):
    class Meta:
        model = models.DiscernModel
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs = {'class': 'form-control', 'placeholder': field.label}


# ================================================ 识别物品详情表单组件 ================================================
class DetailForm(forms.ModelForm):
    class Meta:
        model = models.Detail
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs = {'class': 'form-control', 'placeholder': field.label}


# ================================================ 管理员表单组件 ================================================
class AdminForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs = {'class': 'form-control', 'placeholder': field.label}

    def save(self, commit=True):
        User.objects.create_superuser(username=self.data['username'], password=self.data['password'], email=self.data['email'])


class AdminUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs = {'class': 'form-control', 'placeholder': field.label}
            if name == 'password': field.widget.attrs['readonly'] = "readonly"

    def save(self, commit=True):
        self.instance.username = self.data['username']
        self.instance.email = self.data['email']
        self.instance.save()