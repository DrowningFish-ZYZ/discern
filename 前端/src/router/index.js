import {createRouter, createWebHashHistory} from 'vue-router'
import store from '@/store'

const routers = [
    // ==================================== 主路由 ====================================
    {
        path: '/',
        component: () => import('../components/index.vue'),
        meta: {title: '识别'}
    },
    {
        path: '/user',
        component: () => import('../components/user.vue'),
        meta: {title: '我的'}
    },
    {
        path: '/record',
        component: () => import('../components/record.vue'),
        meta: {title: '历史'}
    },
    {
        path: '/login',
        component: () => import('../components/login.vue')
    },


    // ==================================== 其它路由 ====================================
    // 用户界面子路由
    {
        path: '/user/settings',
        component: () => import('../components/user/settings.vue'),
        meta: {'title': '设置'}
    },
    {
        path: '/user/relase',
        component: () => import('../components/user/relase.vue'),
        meta: {'title': '版本信息'}
    },

    {
        path: '/user/info',
        component: () => import('../components/user/info.vue'),
        meta: {'title': '详情'}
    },
        {
            path: '/user/info/edit',
            component: () => import('../components/user/info/edit.vue'),
            meta: {'title': '编辑'}
        },

    {
        path: '/user/account',
        component: () => import('../components/user/account.vue'),
        meta: {'title': '账户安全'}
    },
        {
            path: '/user/account/reset/pwd',
            component: () => import('../components/user/account/reset_pwd'),
            meta: {'title': '重置密码'}
        },
        {
            path: '/user/account/reset/sq',
            component: () => import('../components/user/account/reset_sq'),
            meta: {'title': '重置密保'}
        },
        

    // 登录界面子路由
    {
        path: '/login/register',
        component: () => import('../components/login/register.vue')
    },
    {
        path: '/login/forget',
        component: () => import('../components/login/forget.vue')
    },


    // 历史记录界面子路由
    {
        path: '/record/detail',
        component: () => import('../components/record/detail.vue'),
        meta: {'title': '详情'}
    }
]


// 设置全局拦截钩子
const router = createRouter({
    history: createWebHashHistory(),
    routes: routers
})
router.beforeEach((to, from, next) => {
    if(to.path == '/login' || to.path == '/login/register' || to.path == '/login/forget'){
        next()
    }else if(!store.state.user.id){
        next('/login')
    }

    next()
})

export default router