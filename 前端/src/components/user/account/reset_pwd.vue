<template>
    <div id="reset-pwd">
        <div class="reset-input" v-show="isshow">
            <div>旧密码</div>
            <input placeholder="Please input" v-model='formdata.oldPassword' />
        </div>

        <div class="reset-input" v-show="isshow">
            <div>新密码</div>
            <input placeholder="Please input" v-model='formdata.newPassword' />
        </div>

        <div class="reset-pwd-bottom" v-show="isshow">
            <el-button type="warning" @click="resetPassword()">重置密码</el-button>
        </div>


        <el-col :sm="12" :lg="12" class="reset-pwd-result" v-show="!isshow">
            <el-result icon="success" title="密码重置成功">
                <template #extra>
                    <el-button type="primary" @click="$router.go(-1); $store.state.isback--">返回</el-button>
                </template>
            </el-result>
        </el-col>

    </div>
</template>

<script>
import utils from '@/utils'
import { ElMessage } from 'element-plus'

export default {
    name: 'resetPwd',
    data() {
        return {
            isshow: true,
            formdata: {
                newPassword: '',
                oldPassword: ''
            }
        }
    },

    methods: {
        resetPassword() {
            if (this.formdata.newPassword && this.formdata.oldPassword) {
                if (this.formdata.newPassword.length >= 4 && this.formdata.newPassword.length <= 8) {

                    utils.request('正在重置', { url: `reset/password/${this.$store.state.user.id}/`, method: 'post', headers: { token: this.$store.state.user.token }, data: this.formdata },
                        res => {
                            this.isshow = false
                        }
                    )

                } else {
                    ElMessage({
                        message: '密码是 4 - 8 位的字符',
                        type: 'warning'
                    })
                }
            } else {
                ElMessage({
                    message: '请全部填写完毕',
                    type: 'error'
                })
            }
        }
    }
}
</script>

<style scoped>
#reset-pwd {
    flex: 1;
    padding: 15px;
    display: flex;
    flex-direction: column;
}

.reset-pwd-result {
    flex: 1;
    display: flex;
    justify-content: center;
    align-items: center;
}

div {
    margin-bottom: 2px;
}

.reset-pwd-bottom {
    margin-top: 15px;
    display: flex;
    padding: 20px 15px;
    justify-content: end;
}

.reset-input {
    display: flex;
    align-items: center;
    justify-content: center;
}

.reset-input div {
    /* background-color: #f5f7fa; */
    font-size: 12px;
    line-height: 40px;
    color: #909399;
}

.reset-input input {
    flex: 1;
    margin-left: 2em;
    padding-left: 1em;
    border: none;
    ;
    border-bottom: 1px solid #dcdfe6;
    line-height: 40px;
    outline: none;
    background-color: transparent;
    border-radius: 0px;
}

.drak .reset-input input {
    color: ghostwhite;
}
</style>
