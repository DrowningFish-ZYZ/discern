<template>
    <div id="register">
        <h4 class="logo" @click="login()"><i>注册</i></h4>

        <el-form ref="form" :model="fromdata" label-position="right" label-width="55px" style="max-width: 460px"
            :rules="rules">
            <el-form-item label="账户" prop="username">
                <el-input placeholder="账户" v-model='fromdata.username' />
            </el-form-item>

            <el-form-item label="密码" prop="password">
                <el-input type="password" placeholder="密码" v-model='fromdata.password' />
            </el-form-item>

            <el-form-item label="号码" prop="phone">
                <el-input placeholder="手机号码" v-model='fromdata.phone' />
            </el-form-item>

            <el-form-item label="邮箱" prop="email">
                <el-input placeholder="邮箱地址" v-model='fromdata.email' />
            </el-form-item>

            <el-form-item label="简介" prop="info">
                <el-input placeholder="个性简介" v-model='fromdata.info' />
            </el-form-item>

            <el-form-item label="密保" prop="sq">
                <el-input placeholder="密保" v-model='fromdata.sq' />
            </el-form-item>
            <el-form-item label="解答" prop="sqKey">
                <el-input placeholder="密保解答" v-model='fromdata.sqKey' />
            </el-form-item>

            <el-form-item label="性别" prop="gender">
                <el-select-v2 v-model="fromdata.gender" placeholder="性别" :options="genderOptions" />
            </el-form-item>

            <el-form-item label="头像">
                <el-upload action="#" list-type="picture-card" :auto-upload="false" :multiple="false"
                    :on-change="change" :on-exceed="exceed" accept=".jpg,.png" :limit="1">
                    <el-icon>
                        <Plus />
                    </el-icon>
                </el-upload>
            </el-form-item>

            <el-form-item>
                <el-button type="primary" @click="register('form')">注册</el-button>
                <el-button @click="$router.push('/login')">登录</el-button>
            </el-form-item>
        </el-form>
    </div>
</template>

<script>
import { DArrowRight, User, Lock, Plus } from '@element-plus/icons-vue'
import utils from '@/utils'

export default {
    name: 'register',
    components: { DArrowRight, User, Lock, Plus },
    data() {
        return {
            // 校验数据
            rules: {
                username: [
                    { 'required': true, 'message': '这是必须的' },
                    { 'max': 8, 'min': 4, 'message': '必须是 4 - 8 位字符' }
                ],
                password: [
                    { 'required': true, 'message': '这是必须的' },
                    { 'max': 8, 'min': 4, 'message': '必须是 4 - 8 位字符' }
                ],
                sq: [
                    { 'required': true, 'message': '这是必须的' },
                    { 'max': 15, 'min': 4, 'message': '必须是 4 - 15 位字符' }
                ],
                sqKey: [
                    { 'required': true, 'message': '这是必须的' },
                    { 'max': 15, 'min': 4, 'message': '必须是 4 - 15 位字符' }
                ],

                gender: [{ 'required': true, 'message': '这是必须的', 'trigger': 'change' }],
                info: [{ 'max': 15, 'min': 4, 'message': '必须是 4 - 15 位字符' }],
                phone: [{ 'pattern': /^(13[0-9]|14[579]|15[0-3,5-9]|16[6]|17[0135678]|18[0-9]|19[89])\d{8}$/, 'message': '格式不正确' }],
                email: [{ 'pattern': /^([a-zA-Z0-9_-])+@([a-zA-Z0-9_-])+((.[a-zA-Z0-9_-]{2,3}){1,2})$/, 'message': '格式不正确' }],
            },

            genderOptions: [{ 'value': 0, 'label': '男' }, { 'value': 1, 'label': '女' }],
            file: null,
            // 表单数据
            fromdata: {
                gender: '',  // 性别
                phone: '',  // 电话
                email: '',  // 邮箱
                username: '',  // 用户名
                password: '',  // 密码
                sq: '',  // 密保问题
                sqKey: '',  // 密保答案
                info: ''  // 简介
            }
        }
    },

    methods: {
        register(formEl) {
            this.$refs[formEl].validate((valid) => {
                if (valid) {
                    // 封装数据
                    let data = new FormData()
                    for (let item in this.fromdata) { data.append(item, this.fromdata[item]) }
                    if (this.file) { data.append('image', this.file, this.file.name) }
                    // 发起请求
                    utils.request('正在注册', { url: 'register/', method: 'post', headers: { 'Content-Type': 'multipart/form-data' }, data: data },
                        res => {
                            // 注册完毕前往登录界面
                            this.$router.push('/login')
                        }
                    )
                } else { return false }
            });
        },

        change(uploadFile, uploadFiles) {
            // upload 组件选中文件成功后触发
            this.file = uploadFile.raw
        },
        exceed(files, uploadFiles) {
            // upload 组件选中文件失败后触发
            ElMessage({
                message: '用户头像已选择',
                type: 'warning',
            })
        }
    }
}
</script>

<style scoped>
#register {
    flex: 1;
    display: flex;
    flex-direction: column;
    padding: 20px 15px;
}

.logo {
    text-align: center;
    margin-bottom: 20px;
    letter-spacing: 2px;
}

/* ===================================== 配色 ===================================== */
</style>