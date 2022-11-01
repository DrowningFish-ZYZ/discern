# discern
手机App图像识别软件

## 1.介绍
### 1.1.前端介绍
- 前端框架基于Vue
- UI使用Element-UI
- 使用 axios 来连接后台服务器
- 使用 vuex + localStorage 混合缓存本地信息
- 使用 vue-router 来跳转页面
- 使用 vue-viewer 来实现图像预览

### 1.2.后端介绍
- 后端框架基于Django
- 使用 django-rest-framework 来实现前后端分离系列化操作
- 使用 corsheaders 来实现跨域操作
- 使用 django-rest-framework-jwt 来实现 jwt 用户认证密钥的签发
- 使用 rest-framework 的 APIView 来实现 API 身份校验，限流操作
- 使用 django 自带的模板语法 + forms 组件 + auth 认证实现后台管理系统【UI 使用 bootstrap】

### 1.3.识别介绍
- 深度学习框架使用 tensorflow 
- 目标识别算法使用 yolov3

## 2.大体界面
### 2.1.前端
