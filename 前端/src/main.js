import { createApp } from 'vue'
import ElementPlus from 'element-plus' 
import 'element-plus/dist/index.css'

import 'viewerjs/dist/viewer.css'
import VueViewer from 'v-viewer'

import App from './App.vue'
import router from './router'
import store from './store'
import axios from './request'

const app = createApp(App)
app.config.globalProperties.$axios = axios
app.use(router)
app.use(store)
app.use(ElementPlus)
app.use(VueViewer)
app.mount('#app')