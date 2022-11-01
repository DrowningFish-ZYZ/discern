<template>
    <div id="login">
        <h3 class="logo"><i>DISCERN</i></h3>

        <div class="input">
            <div>
                <el-icon size="25px">
                    <User />
                </el-icon>
            </div>
            <input :placeholder="userpl" v-model='user.username' maxlength="11" />
        </div>

        <div class="input">
            <div>
                <el-icon size="25px">
                    <Lock />
                </el-icon>
            </div>
            <input type="password" :placeholder="passpl" v-model='user.password' maxlength="16" />
        </div>

        <el-checkbox v-model="checked"><span>我已经阅读并同意</span><a href="">服务协议</a></el-checkbox>

        <button @click="login()">
            <el-icon size="30px" style="color: whitesmoke">
                <DArrowRight />
            </el-icon>
        </button>
 
        <ul>
            <li>
                <router-link to="/login/forget">忘记密码</router-link>
            </li>
            <li>
                <router-link to="/login/register">注册用户</router-link>
            </li>
        </ul>
    </div>
</template>

<script>
import { DArrowRight, User, Lock } from '@element-plus/icons-vue'
import utils from '@/utils'

export default {
    name: 'login',
    components: { DArrowRight, User, Lock },
    data() {
        return {
            user: {
                username: '',
                password: '',
            },
            checked: true,
            userpl: '账户',
            passpl: '密码',
            all: true,
        }
    },

    methods: {
        login() {
            if (!(this.user.username && this.user.password)) {
                this.userpl = '请填写'
                this.passpl = '请填写'
            } else if (!this.checked) {
                ElMessage.error('你必须同意协议才能登录')
            } else {
                // 发起请求
                utils.request('正在登录', { method: 'post', url: 'login/', dataType: 'json', data: this.user },
                    response => {
                        // 封装数据到 localStorage 和 store
                        for (let item in response.data) {
                            localStorage.setItem(item, response.data[item])
                            this.$store.state.user[item] = response.data[item]
                        }
                        // 前往主页
                        this.$router.push('/')
                    }
                )
            }
        }
    }
}
</script>

<style scoped>
#login {
    flex: 1;
    padding-top: 10%;
    display: flex;
    align-items: center;
    flex-direction: column;
    position: relative;
    background-color: white;
}

.logo {
    padding: 25px;
    letter-spacing: 5px;
    color: #304352;
    margin-bottom: 20px;
    font-size: 26px;
}

.input {
    display: flex;
    justify-content: center;
    align-items: center;
    background-color: rgba(128, 128, 128, 0.095);
    border-radius: 25px;
    padding: 20px 25px;
    margin-bottom: 10px;
}

.input div {
    display: flex;
    justify-content: center;
    align-items: center;
}

.input input {
    flex-basis: 40%;
    margin-left: 10px;
    border: none;
    outline: none;
    background-color: transparent;
    text-indent: 1em;
    font-size: 20px;
    letter-spacing: 2px;
}

span,
a {
    color: gray;
    font-size: 14px;
}

a {
    color: #409eff;
}

button {
    display: flex;
    align-items: center;
    width: 50px;
    height: 50px;
    padding: 40px;
    text-align: center;
    justify-content: center;
    border-radius: 50%;
    border: 1px solid gray;
    margin-top: 40px;
    background-image: linear-gradient(to top, #48c6ef 0%, #6f86d6 100%);
}

ul {
    position: absolute;
    bottom: 0;
    padding-bottom: 25px;
    margin-bottom: 15px;
    display: flex;
    justify-content: center;
    align-items: center;
}

li {
    list-style: none;
    border-right: 1px solid grey;
    padding: 0px 20px;
    font-size: 12px;
}

li a {
    color: black;
}

li:last-child {
    border: none;
}

/* ===================================== 配色 ===================================== */
</style>