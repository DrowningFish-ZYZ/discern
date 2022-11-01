<template>
    <div id="forget">
        <el-steps :active="active" finish-status="success">
            <el-step title="账户" />
            <el-step title="密保" />
            <el-step title="密码" />
        </el-steps>

        <!-- 账户 -->
        <div class="forget-box" v-show="active == 0">
            <el-form ref="form1" style="max-width: 460px" :rules="rules" label-width="55px" label-position="right"
                :model="formdata1">
                <el-form-item label="账户" prop="username">
                    <el-input placeholder="你的账户" v-model='formdata1.username' />
                </el-form-item>

                <el-form-item>
                    <el-button type="primary" @click="next1('form1')">下一步</el-button>
                    <el-button type="info" @click="$router.push('/login')">取消</el-button>
                </el-form-item>
            </el-form>
        </div>

        <!-- 密保 -->
        <div class="forget-box" v-show="active == 1">
            <el-form ref="form2" style="max-width: 460px" :rules="rules" label-width="55px" label-position="right"
                :model="formdata2">
                <p style="color: gray; text-align: center; margin-bottom: 15px; font-size: 14px;">
                    密保问题: {{ formdata2.sq }}
                </p>

                <el-form-item label="密保" prop="sqKey">
                    <el-input placeholder="密保答案" v-model='formdata2.sqKey' />
                </el-form-item>

                <el-form-item>
                    <el-button type="primary" @click="next2('form2')">下一步</el-button>
                    <el-button type="info" @click="$router.push('/login')">取消</el-button>
                </el-form-item>
            </el-form>
        </div>

        <!-- 修改密码 -->
        <div class="forget-box" v-show="active == 2">
            <el-form ref="form3" style="max-width: 460px" :rules="rules" label-width="55px" label-position="right"
                :model="formdata3">
                <p style="color: gray; text-align: center; margin-bottom: 15px; font-size: 14px;">
                    重置密码
                </p>

                <el-form-item label="密码" prop="password">
                    <el-input placeholder="重置密码" v-model='formdata3.password' />
                </el-form-item>

                <el-form-item>
                    <el-button type="primary" @click="next3('form3')">确定</el-button>
                    <el-button type="info" @click="$router.push('/login')">取消</el-button>
                </el-form-item>
            </el-form>
        </div>

        <!-- 修改完毕，提醒返回 -->
        <div class="forget-box" v-show="active == 3">
            <el-col :sm="12" :lg="6">
                <el-result icon="success" title="重置成功" :sub-title="'你的新密码为:' + formdata3.password">
                    <template #extra>
                        <el-button type="primary" @click="$router.push('/login')">返回</el-button>
                    </template>
                </el-result>
            </el-col>
        </div>
    </div>
</template>

<script>
import { Edit, Picture, UploadFilled } from '@element-plus/icons-vue'
import utils from '@/utils'

export default {
    name: 'forgetPassword',
    components: { Edit, Picture, UploadFilled },
    data() {
        return {
            rules: {
                username: [{ 'required': true, 'message': '这是必须的' }],
                sqKey: [{ 'required': true, 'message': '这是必须的' }],
                password: [
                    { 'required': true, 'message': '这是必须的' },
                    { 'max': 8, 'min': 4, 'message': '4 - 8 位字符' }
                ]
            },

            formdata1: { username: '' },
            formdata2: { sq: '', sqKey: '', username: '' },
            formdata3: { password: '', sqKey: '', username: '', sq: '' },
            active: 0
        }
    },

    methods: {
        next1(form) {
            this.$refs[form].validate((valid) => {
                if (valid) {
                    // 1.根据账户，在后台获取对应的密保
                    utils.request('校验中', { url: 'forget/password/1/', method: 'post', data: this.formdata1 }, 
                        res => {
                            this.formdata2.sq = res.data.sq
                            this.active++
                        }
                    )
                }
            })
        },

        next2(form) {
            this.$refs[form].validate((valid) => {
                if (valid) {
                    // 2.根据账户与密保答案前往后台匹配
                    this.formdata2.username = this.formdata1.username
                    utils.request('校验中', { url: 'forget/password/2/', method: 'post', data: this.formdata2 }, 
                        res => {
                            this.active++
                        }
                    )
                }
            })
        },

        next3(form) {
            this.$refs[form].validate((valid) => {
                if (valid) {
                    // 3.匹配成功，将账户，密保，新密码发往后台重置
                    this.formdata3.username = this.formdata2.username
                    this.formdata3.sq = this.formdata2.sq
                    this.formdata3.sqKey = this.formdata2.sqKey
                    utils.request('校验中', { url: 'forget/password/3/', method: 'post', data: this.formdata3 }, 
                        res => {
                            this.active++
                        }
                    )
                }
            })
        }
    }
}
</script>

<style scoped>
#forget {
    flex: 1;
    padding: 20px;
}

.forget-box {
    padding-top: 50px;
}
</style>