"""
# @Time    : 2022/10/29 21:54
# @Author  : violet
# @explain : 管理员管理
"""

from django.shortcuts import render, reverse, redirect
from django.contrib.auth import models
from ... import utils
from django.contrib import auth
from django.contrib.auth.decorators import login_required


@login_required
def admin_list(request):
    queryset = models.User.objects.all()
    return render(request, 'admin_list.html', {'queryset': queryset})


@login_required
def admin_add(request):
    if request.method == 'GET':
        form = utils.forms.AdminForm()
        return render(request, 'model_form.html', {'form': form, 'title': '新建管理员', 'post_url': reverse('admin_add')})

    # 对数据进行基础校验
    form = utils.forms.AdminForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect(reverse('admin_list'))

    return render(request, 'model_form.html', {'form': form, 'title': '新建管理员', 'post_url': reverse('admin_add')})


@login_required
def admin_delete(request, pk: int):
    models.User.objects.filter(pk=pk).delete()
    return redirect(reverse('admin_list'))


@login_required
def admin_update(request, pk: int):
    if request.method == 'GET':
        user = models.User.objects.filter(pk=pk).first()
        form = utils.forms.AdminUpdateForm(instance=user)
        return render(request, 'model_form.html',
                      {'form': form, 'title': '修改管理员', 'post_url': reverse('admin_update', kwargs={'pk': pk})})

    user = models.User.objects.filter(pk=pk).first()
    form = utils.forms.AdminUpdateForm(instance=user, data=request.POST)
    if form.is_valid():
        form.save()
        return redirect(reverse('admin_list'))

    return render(request, 'model_form.html',
                  {'form': form, 'title': '修改管理员', 'post_url': reverse('admin_update', kwargs={'pk': pk})})


def login(request):
    """ 登录视图 """
    if request.method == 'GET':
        return render(request, 'login.html')

    user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
    if user:
        auth.login(request, user)
        return redirect(reverse('user_list'))

    return render(request, 'login.html', {'message': '账户密码错误'})


def logout(request):
    """ 注销 """
    auth.logout(request)
    return redirect(reverse('login'))