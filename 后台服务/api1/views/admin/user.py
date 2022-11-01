"""
# @Time    : 2022/10/29 19:23
# @Author  : violet
# @explain : 用户管理
"""

from django.shortcuts import render, reverse, redirect
from django import http
from ... import utils, models
from django.contrib.auth.decorators import login_required


@login_required
def user_list(request: http.HttpRequest) -> http.HttpResponse:
    """ 获取所有用户 """
    queryset = models.User.objects.all()
    return render(request, 'user_list.html', {'queryset': queryset})


@login_required
def user_add(request: http.HttpRequest) -> http.HttpResponse:
    """ 新建用户 """
    if request.method == 'GET':
        form = utils.forms.UserModelForm()
        return render(request, 'model_form.html', {'form': form, 'title': '新建用户', 'post_url': reverse('user_add')})

    # 对数据进行基础校验
    form = utils.forms.UserModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect(reverse('user_list'))

    return render(request, 'model_form.html', {'form': form, 'title': '新建用户', 'post_url': reverse('user_add')})


@login_required
def user_delete(request: http.HttpRequest, pk: int) -> http.HttpResponse:
    """ 删除用户 """
    models.User.objects.filter(pk=pk).delete()
    return redirect(reverse('user_list'))


@login_required
def user_update(request: http.HttpRequest, pk: int) -> http.HttpResponse:
    """ 修改用户 """
    if request.method == 'GET':
        user = models.User.objects.filter(pk=pk).first()
        form = utils.forms.UserUpdateModelForm(instance=user)
        return render(request, 'model_form.html',
                      {'form': form, 'title': '修改用户', 'post_url': reverse('user_update', kwargs={'pk': pk})})

    user = models.User.objects.filter(pk=pk).first()
    form = utils.forms.UserUpdateModelForm(instance=user, data=request.POST)
    if form.is_valid():
        form.save()
        return redirect(reverse('user_list'))

    return render(request, 'model_form.html',
                  {'form': form, 'title': '修改用户', 'post_url': reverse('user_update', kwargs={'pk': pk})})
