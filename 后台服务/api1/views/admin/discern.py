"""
# @Time    : 2022/10/29 20:43
# @Author  : violet
# @explain : 识别类型管理
"""

from django.shortcuts import render, reverse, redirect
from django import http
from ... import utils, models
from django.contrib.auth.decorators import login_required


@login_required
def discern_list(request: http.HttpRequest) -> http.HttpResponse:
    """ 获取所有识别类型 """
    queryset = models.DiscernType.objects.all().order_by('id')
    return render(request, 'discern_list.html', {'queryset': queryset})


@login_required
def discern_add(request: http.HttpRequest) -> http.HttpResponse:
    """ 新建识别类型 """
    if request.method == 'GET':
        form = utils.forms.DiscernTypeForm()
        return render(request, 'model_form.html', {'form': form, 'title': '新建识别类型', 'post_url': reverse('discern_add')})

    # 对数据进行基础校验
    form = utils.forms.DiscernTypeForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect(reverse('discern_list'))

    return render(request, 'model_form.html', {'form': form, 'title': '新建识别类型', 'post_url': reverse('discern_add')})


@login_required
def discern_delete(request: http.HttpRequest, pk: int) -> http.HttpResponse:
    """ 删除识别类型 """
    models.DiscernType.objects.filter(pk=pk).delete()
    return redirect(reverse('discern_list'))


@login_required
def discern_update(request: http.HttpRequest, pk: int) -> http.HttpResponse:
    """ 修改识别类型 """
    if request.method == 'GET':
        discern = models.DiscernType.objects.filter(pk=pk).first()
        form = utils.forms.DiscernTypeForm(instance=discern)
        return render(request, 'model_form.html',
                      {'form': form, 'title': '修改识别类型', 'post_url': reverse('discern_update', kwargs={'pk': pk})})

    discern = models.DiscernType.objects.filter(pk=pk).first()
    form = utils.forms.DiscernTypeForm(instance=discern, data=request.POST)
    if form.is_valid():
        form.save()
        return redirect(reverse('discern_list'))

    return render(request, 'model_form.html', {'form': form, 'title': '新建识别类型', 'post_url': reverse('discern_add')})
