import {createStore} from 'vuex'

localStorage.theme = localStorage.theme?localStorage.theme:'pure'
localStorage.fontsize = localStorage.fontsize?localStorage.fontsize:'median'
localStorage.inpage = localStorage.inpage?localStorage.inpage:1

export default createStore({
    state: {
        // baseIP: 'https://violetapi.cn',
        baseIP: 'http://127.0.0.1:8000',
        // baseIP: 'http://192.168.190.1:8000',
 
        // 设置配置【需在后端获取】
        settings: {
            themes: ['pure', 'drak'],  // 主题选项
            theme: localStorage.getItem('theme'),  // 当前主题
            fontsizes: ['big', 'median', 'small'],  // 字体选项
            fontsize: localStorage.getItem('fontsize')  // 默认选中字体
        },

        // 识别主页需要用到的数据【需在后端获取】
        index: {
            imgFile: null, // 主页选中图像文件
            imgs: [''],  // 主页显示识别图像的 src
        },

        // 页面切换
        isback: 0, // 页面返回纵深
        inpage: localStorage.getItem('inpage'),  // 当前所在页面下标

        // 用户信息
        user: {
            username: localStorage.getItem('username'),  // 用户名
            id: localStorage.getItem('id'),  // 用户ID
            token: localStorage.getItem('token'),  // token 密钥
            headPortrait: localStorage.getItem('headPortrait'),  // 用户头像
            gender: localStorage.getItem('gender'),  // 用户性别
            info: localStorage.getItem('info')  // 用户简介
        },
        // 用户详情
        userDetail: {
            email: '',
            phone: ''
        }
    }
})