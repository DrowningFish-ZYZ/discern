<template>
    <div id="edit">
        <el-form ref="form" :model="fromdata" label-position="right" label-width="55px" style="max-width: 460px"
            :rules="rules" v-show="isshow">
            <el-form-item label="号码" prop="phone">
                <el-input placeholder="手机号码" v-model='fromdata.phone' />
            </el-form-item>

            <el-form-item label="邮箱" prop="email">
                <el-input placeholder="邮箱地址" v-model='fromdata.email' />
            </el-form-item>

            <el-form-item label="简介" prop="info">
                <el-input placeholder="个性简介" v-model='fromdata.info' />
            </el-form-item>

            <el-form-item label="性别" prop="gender">
                <el-select-v2 v-model="fromdata.gender" placeholder="性别" :options="genderOptions" />
            </el-form-item>

            <el-form-item>
                <el-button type="primary" @click="update('form')">更改</el-button>
                <el-button @click="$router.go(-1); $store.state.isback--">取消</el-button>
            </el-form-item>
        </el-form>

        <div class="reset-pwd-result" v-show="!isshow">
            <el-col :sm="12" :lg="6">
                <el-result icon="success" title="重置成功">
                    <template #extra>
                        <el-button type="primary" @click="$router.go(-1); $store.state.isback--">返回</el-button>
                    </template>
                </el-result>
            </el-col>
        </div>
    </div>
</template>

<script>
import utils from '@/utils'

export default {
    name: 'edit',
    data() {
        return {
            isshow: true,
            rules: {
                gender: [{ 'required': true, 'message': '这是必须的', 'trigger': 'change' }],
                info: [{ 'max': 15, 'min': 4, 'message': '必须是 4 - 15 位字符' }],
                phone: [{ 'pattern': /^(13[0-9]|14[579]|15[0-3,5-9]|16[6]|17[0135678]|18[0-9]|19[89])\d{8}$/, 'message': '格式不正确' }],
                email: [{ 'pattern': /^([a-zA-Z0-9_-])+@([a-zA-Z0-9_-])+((.[a-zA-Z0-9_-]{2,3}){1,2})$/, 'message': '格式不正确' }],
            },
            genderOptions: [{ 'value': '0', 'label': '男' }, { 'value': '1', 'label': '女' }],
            fromdata: {
                phone: this.$store.state.userDetail.phone != '暂无' ? this.$store.state.userDetail.phone : '',
                email: this.$store.state.userDetail.email != '暂无' ? this.$store.state.userDetail.email : '',
                info: this.$store.state.user.info,
                gender: `${this.$store.state.user.gender}`,
            }
        }
    },

    methods: {
        update(formEl) {
            this.$refs[formEl].validate((valid) => {
                if (valid) {
                    utils.request('正在修改', { url: `user/${this.$store.state.user.id}/`, method: 'put', headers: { token: this.$store.state.user.token }, data: this.fromdata },
                        res => {
                            // 重置本地数据 [localStorage & store]
                            localStorage.info = res.data.info
                            localStorage.gender = res.data.gender
                            this.$store.state.user.info = res.data.info
                            this.$store.state.user.gender = res.data.gender
                            this.$store.state.userDetail.email = res.data.email
                            this.$store.state.userDetail.phone = res.data.phone
                            // 给予提示
                            this.isshow = false
                        }
                    )
                } else { return false }
            });
        }
    }
}
</script>

<style scoped>
#edit {
    flex: 1;
    padding: 20px 15px;
    display: flex;
    flex-direction: column;
}

.reset-pwd-result {
    flex: 1;
    display: flex;
    justify-content: center;
    align-items: center;
}
</style>

