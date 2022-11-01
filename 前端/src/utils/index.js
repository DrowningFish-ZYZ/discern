import { ElMessage, ElLoading } from 'element-plus'
import axios from '@/request'

export default {
    /**
     * 错误提示
     * @param {*} response response 对象
     */
    message(response) {
        // 如果没有响应对象，那么便是网络或服务器异常
        if (!response) {
            ElMessage({
                message: '服务器无响应',
                type: 'error'
            })
            return false
        }

        // 如果是数据错误之类的后端都会返回 400 错误，并给予 message 提示
        if (response.status == 400) {
            ElMessage({
                message: response.data.message,
                type: 'error'
            })

            // 如果是限流操作会返回 429 错误，并给与 detail 提示
        } else if (response.status == 429) {
            ElMessage({
                message: '请一分钟后再尝试',
                type: 'warning'
            })

            // 如果是用户 token 认证失效会返回 401 错误，并给与 detail 提示
        } else if (response.status == 401) {
            ElMessage({
                message: '登录认证失效, 请重新登录',
                type: 'warning'
            })

            // 如果是服务器异常
        } else {
            ElMessage({
                message: '服务器出错啦！',
                type: 'warning'
            })
        }
    },

    /**
     * 请求耗时操作
     * @param {string} text 提示文本
     * @param {object} requestObj 请求对象 {url, method, data, headers}
     * @param {function} thenFun 成功后要执行的操作 res => {}
     */
    async request(text, requestObj, thenFun) {
        let loading = ElLoading.service({
            lock: true,
            text: text,
            background: 'rgba(0, 0, 0, 0.7)',
        })

        // 发起请求
        axios.request(requestObj)
        .then(res => {
            thenFun(res)
            loading.close()
        })
        .catch(res => {
            this.message(res.response)
            loading.close()
        })
    }
}