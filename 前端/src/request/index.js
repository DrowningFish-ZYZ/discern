import axios from 'axios'
import store from '@/store'

const API = axios.create({
    baseURL: `${store.state.baseIP}/api/1/`,  // 前缀IP
    timeout: 5000  // 超时时间,
})

export default API