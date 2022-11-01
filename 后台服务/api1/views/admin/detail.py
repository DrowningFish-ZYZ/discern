"""
# @Time    : 2022/10/29 21:37
# @Author  : violet
# @explain : 识别物品详情管理
"""

from django.shortcuts import render, reverse, redirect
from django import http
from ... import utils, models
from django.contrib.auth.decorators import login_required


@login_required
def detail_list(request):
    """ 获取所有详情 """
    queryset = models.Detail.objects.all()
    return render(request, 'detail_list.html', {'queryset': queryset})


@login_required
def detail_add(request):
    """ 添加详情 """
    if request.method == 'GET':
        form = utils.forms.DetailForm()
        return render(request, 'model_form.html', {'form': form, 'title': '新建识别详情', 'post_url': reverse('detail_add')})

    # 对数据进行基础校验
    form = utils.forms.DetailForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect(reverse('detail_list'))

    return render(request, 'model_form.html', {'form': form, 'title': '新建识别类型', 'post_url': reverse('detail_add')})


@login_required
def detail_delete(request, pk: int):
    """ 删除详情 """
    models.Detail.objects.filter(pk=pk).delete()
    return redirect(reverse('detail_list'))


@login_required
def detail_update(request, pk: int):
    if request.method == 'GET':
        user = models.Detail.objects.filter(pk=pk).first()
        form = utils.forms.DetailForm(instance=user)
        return render(request, 'model_form.html',
                      {'form': form, 'title': '修改详情', 'post_url': reverse('detail_update', kwargs={'pk': pk})})

    user = models.Detail.objects.filter(pk=pk).first()
    form = utils.forms.DetailForm(instance=user, data=request.POST)
    if form.is_valid():
        form.save()
        return redirect(reverse('detail_list'))

    return render(request, 'model_form.html',
                  {'form': form, 'title': '修改详情', 'post_url': reverse('detail_update', kwargs={'pk': pk})})
