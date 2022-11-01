"""
# @Time    : 2022/10/29 21:12
# @Author  : violet
# @explain : 识别模型管理
"""

from django.shortcuts import render, reverse, redirect
from django import http
from ... import utils, models
from django.contrib.auth.decorators import login_required


@login_required
def model_list(request: http.HttpRequest) -> http.HttpResponse:
    """ 获取所有识别模型 """
    queryset = models.DiscernModel.objects.all()
    return render(request, 'model_list.html', {'queryset': queryset})


@login_required
def model_add(request: http.HttpRequest) -> http.HttpResponse:
    """ 添加识别模型 """
    if request.method == 'GET':
        form = utils.forms.DiscernModelForm()
        return render(request, 'model_form.html', {'form': form, 'title': '添加识别模型', 'post_url': reverse('model_add')})

    form = utils.forms.DiscernModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect(reverse('model_list'))

    return render(request, 'model_form.html', {'form': form, 'title': '添加识别模型', 'post_url': reverse('model_add')})


@login_required
def model_delete(request: http.HttpRequest, pk: int) -> http.HttpResponse:
    """ 删除识别模型 """
    models.DiscernModel.objects.filter(pk=pk).delete()
    return redirect(reverse('model_list'))


@login_required
def model_update(request: http.HttpRequest, pk: int) -> http.HttpResponse:
    """ 修改识别模型 """
    if request.method == 'GET':
        item = models.DiscernModel.objects.filter(pk=pk).first()
        form = utils.forms.DiscernModelForm(instance=item)
        return render(request, 'model_form.html',
                      {'form': form, 'title': '修改识别模型', 'post_url': reverse('model_update', kwargs={'pk': pk})})

    item = models.DiscernModel.objects.filter(pk=pk).first()
    form = utils.forms.DiscernModelForm(instance=item, data=request.POST)
    if form.is_valid():
        form.save()
        return redirect(reverse('model_list'))

    return render(request, 'model_form.html',
                  {'form': form, 'title': '修改识别模型', 'post_url': reverse('model_update', kwargs={'pk': pk})})
