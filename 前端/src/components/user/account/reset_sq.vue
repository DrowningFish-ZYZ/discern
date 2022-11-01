<template>
    <div id="reset-sq">
        <div v-show="isshow">
            <div class="reset-sq-header">原密保与答案</div>
            <div class="reset-input">
                <input placeholder="原密保" v-model="formdata.oldSq" />
            </div>
            <div class="reset-input">
                <input placeholder="原密保答案" v-model="formdata.oldSqKey" />
            </div>

            <div class="reset-sq-header" style="margin-top: 25px;">新密保与答案</div>
            <div class="reset-input">
                <input placeholder="新密保" v-model="formdata.newSq" />
            </div>
            <div class="reset-input">
                <input placeholder="新密保答案" v-model="formdata.newSqKey" />
            </div>

            <div class="reset-pwd-bottom">
                <el-button type="warning" @click="resetSq()">重置密保</el-button>
            </div>
        </div>

        <el-col :sm="12" :lg="12" class="reset-pwd-result" v-show="!isshow">
            <el-result icon="success" title="密保重置成功">
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
    name: 'resetSq',
    data() {
        return {
            isshow: true,
            formdata: {
                oldSq: '',
                oldSqKey: '',
                newSq: '',
                newSqKey: ''
            }
        }
    },

    methods: {
        resetSq() {
            if (this.formdata.oldSq && this.formdata.oldSqKey && this.formdata.newSq && this.formdata.newSqKey) {
                if (this.formdata.newSq.length >= 4 && this.formdata.newSq.length <= 15 && this.formdata.newSqKey.length >= 4 && this.formdata.newSqKey.length <= 15) {

                    utils.request('正在重置', { url: `reset/sq/${this.$store.state.user.id}/`, method: 'post', headers: { token: this.$store.state.user.token }, data: this.formdata },
                        res => {
                            this.isshow = false
                        }
                    )

                } else {
                    ElMessage({
                        message: '请填写 4 - 15 位的字符!',
                        type: 'warning'
                    })
                }
            } else {
                ElMessage({
                    message: '请全部填写!',
                    type: 'error'
                })
            }
        }
    }
}
</script>

<style scoped>
#reset-sq {
    flex: 1;
    display: flex;
    flex-direction: column;
    padding: 15px;
}

.reset-sq-header {
    color: rgb(55, 50, 50);
    font-size: 14px;
    margin-bottom: 10px;
    letter-spacing: 1px;
}

.reset-input {
    display: flex;
    align-items: center;
    justify-content: center;
}

.reset-input div {
    font-size: 12px;
    line-height: 40px;
    color: #909399;
}

.reset-input input {
    flex: 1;
    border: none;
    text-indent: 1em;
    border-bottom: 1px solid #dcdfe6;
    line-height: 40px;
    outline: none;
    background-color: transparent;
    border-radius: 0px;
}

.reset-pwd-bottom {
    margin-top: 15px;
    display: flex;
    padding: 20px 15px;
    justify-content: end;
}

.reset-pwd-result {
    flex: 1;
    display: flex;
    justify-content: center;
    align-items: center;
}

.drak .reset-input input,
.drak .reset-sq-header {
    color: ghostwhite;
}
</style>
