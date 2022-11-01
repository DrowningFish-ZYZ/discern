"""
# @Time    : 2022/10/20 13:46
# @Author  : violet
# @explain : api 1 路由管理
"""

from django.urls import path
from .views import user, index
from .views import admin

urlpatterns = [
    # ================================= 前端使用的视图路由 =====================================================
    # 用户登录与注册【无需 token 权限】
    path('login/', user.LoginAPIView.as_view()),  # 登录
    path('register/', user.RegisterAPIView.as_view()),  # 注册
    path('forget/password/<int:step>/', user.ForgetPasswordAPIView.as_view()),  # 忘记密码

    # 普通用户账户安全逻辑视图【需要 token 权限】
    path('reset/password/<int:pk>/', user.ResetPasswordAPIView.as_view()),  # 重置密码
    path('reset/sq/<int:pk>/', user.ResetSQAPIView.as_view()),  # 重置密保
    path('reset/portrait/<int:pk>/', user.ResetHeadPortraitAPIView.as_view()),  # 重置用户头像
    path('user/<int:pk>/', user.UserAPIView.as_view()),  # GET:获取用户详情, PUT:更改用户信息

    # 主页相关视图【需要 token 权限】
    path('model/', index.ModelAPIView.as_view()),  # 获取所有模型数据
    path('discern/<int:pk>/', index.DiscernAPIView.as_view()),  # 识别模型
    path('record/<int:pk>/', index.RecordAPIView.as_view()),  # GET: 根据用户ID获取所有对应历史记录, DELETE: 删除对应的记录
    path('detail/', index.DetailAPIView.as_view()),

    # ================================= 后台管理系统视图路由 =====================================================
    path('admin/login/', admin.admin.login, name="login"),
    path('admin/logout/', admin.admin.logout, name='logout'),

    # 用户管理
    path('admin/user/list/', admin.user.user_list, name='user_list'),
    path('admin/user/add/', admin.user.user_add, name='user_add'),
    path('admin/user/delete/<int:pk>/', admin.user.user_delete, name='user_delete'),
    path('admin/user/update/<int:pk>/', admin.user.user_update, name='user_update'),

    # 识别类型管理
    path('admin/discern/list/', admin.discern.discern_list, name='discern_list'),
    path('admin/discern/add/', admin.discern.discern_add, name='discern_add'),
    path('admin/discern/delete/<int:pk>/', admin.discern.discern_delete, name='discern_delete'),
    path('admin/discern/update/<int:pk>/', admin.discern.discern_update, name='discern_update'),

    # 识别模型管理
    path('admin/model/list/', admin.discernModel.model_list, name='model_list'),
    path('admin/model/add/', admin.discernModel.model_add, name='model_add'),
    path('admin/model/delete/<int:pk>/', admin.discernModel.model_delete, name='model_delete'),
    path('admin/model/update/<int:pk>/', admin.discernModel.model_update, name='model_update'),

    # 识别物品详情管理
    path('admin/detail/list/', admin.detail.detail_list, name='detail_list'),
    path('admin/detail/add/', admin.detail.detail_add, name='detail_add'),
    path('admin/detail/delete/<int:pk>/', admin.detail.detail_delete, name='detail_delete'),
    path('admin/detail/update/<int:pk>/', admin.detail.detail_update, name='detail_update'),

    # 管理员管理
    path('admin/list/', admin.admin.admin_list, name='admin_list'),
    path('admin/add/', admin.admin.admin_add, name='admin_add'),
    path('admin/delete/<int:pk>/', admin.admin.admin_delete, name='admin_delete'),
    path('admin/update/<int:pk>/', admin.admin.admin_update, name='admin_update'),
]
