<template>
    <div id="user" :class="$store.state.settings.fontsize">
        <!-- 用户头像 -->
        <div class="user-box">
            <img :src="$store.state.baseIP + $store.state.user.headPortrait" v-viewer>
            <div>
                <router-link to="/user/info" @click="openback()">
                    <p class="user-name">
                        {{ $store.state.user.username }}
                        <el-icon v-if="$store.state.user.gender==1" size="12px" style="color: red">
                            <Female />
                        </el-icon>
                        <el-icon v-else size="12px" style="color: black">
                            <Male />
                        </el-icon>
                    </p>
                    <p class="user-sign">{{ $store.state.user.info }}</p>
                </router-link>
            </div>
            <el-icon size="20px" class="link">
                <ArrowRight />
            </el-icon>
        </div>

        <!-- 设置列表 -->
        <div class="settings">
            <router-link to="/user/settings" @click="openback()">
                <div class="line">
                    <el-icon size="20px" class="line-img">
                        <Setting />
                    </el-icon>
                    <span class="line-text">设置</span>
                    <el-icon size="20px" class="link">
                        <ArrowRight />
                    </el-icon>
                </div>
            </router-link>

            <router-link to="/user/account" @click="openback()">
                <div class="line">
                    <el-icon size="20px" class="line-img">
                        <Lock />
                    </el-icon>
                    <span class="line-text">账户安全</span>
                    <el-icon size="20px" class="link">
                        <ArrowRight />
                    </el-icon>
                </div>
            </router-link>

            <router-link to="/user/relase" @click="openback()">
                <div class="line last-line">
                    <el-icon size="20px" class="line-img">
                        <DocumentCopy />
                    </el-icon>
                    <span class="line-text">版本信息</span>
                    <el-icon size="20px" class="link">
                        <ArrowRight />
                    </el-icon>
                </div>
            </router-link>
        </div>

        <div class="foot">
            <el-button type="danger" round @click="logout()">登出</el-button>
        </div>
    </div>
</template>

<script>
import { Setting, DocumentCopy, ArrowRight, Lock, Female, Male } from '@element-plus/icons-vue'

export default {
    name: 'user',
    components: { Setting, DocumentCopy, ArrowRight, Lock, Female, Male },

    methods: {
        openback() {
            this.$store.state.isback++
        },
        
        logout() { // 退出登录
            // 重置 localsession
            let theme = localStorage.theme
            let fontsize = localStorage.fontsize
            localStorage.clear()
            localStorage.fontsize = fontsize
            localStorage.theme = theme
            localStorage.inpage = 1
            // 刷新整个界面
            location.reload()
        }
    }
}
</script>

<style scoped>
/* ===================================== 布局 ===================================== */
#user {
    flex: 1;
    display: flex;
    flex-direction: column;
    padding: 15px;
}

/* 头像 */
.user-box {
    display: flex;
    align-items: center;
    padding: 10px;
    border-radius: 5px;
    position: relative;
    margin-bottom: 15px;
}

.user-box img {
    width: 50px;
    height: 50px;
    border-radius: 50%;
    object-fit: cover;
    object-position: 50% 20%;
}

.user-box>div {
    margin-left: 12px;
    flex: 1;
}

.link {
    position: absolute;
    right: 15px;
    color: gray;
}

/* 设置列表 */
.settings {
    display: flex;
    padding: 5px 0px;
    border-radius: 5px;
    position: relative;
    flex-direction: column;
    justify-content: center;
}

.line {
    padding: 0px 0px 0px 15px;
    display: flex;
    align-items: center;
}

.line-text {
    margin-left: 5px;
    flex: 1;
    padding: 8px 8px;
}

.last-line {
    border: none !important;
}

.foot {
    flex: 1;
    position: relative;
}

.el-button--danger {
    position: absolute;
    bottom: 0px;
    width: 100%;
    padding: 20px;
}


.gender {
    position: absolute;
    left: 40px;
    top: 20px;
}

/* ============================== 字体设置 ============================== */
.big {
    font-size: 18px;
}

.median {
    font-size: 14px;
}

.small {
    font-size: 12px;
}

.big .user-box .user-name {
    font-size: 24px;
}

.big .user-box .user-sign {
    font-size: 12px;
}

.median .user-box .user-name {
    font-size: 20px;
}

.median .user-box .user-sign {
    font-size: 10px;
}

.small .user-box .user-name {
    font-size: 18px;
}

.small .user-box .user-sign {
    font-size: 8px;
}

/* ===================================== 配色 ===================================== */
/* 纯白 */
.pure .user-box,
.pure .settings {
    box-shadow: 1px 2px 5px gray;
    border: 1px solid rgb(206, 202, 202);
}

.pure .user-box .user-name,
.pure .line-img,
.pure .line-text {
    color: black;
}

.pure .user-box .user-sign {
    color: gray;
}

.pure .line {
    border-bottom: 1px solid rgb(190, 189, 189);
}

/* 黑夜 */
.drak .user-box,
.drak .settings {
    box-shadow: 1px 1px 10px rgb(210, 207, 207);
    border: 1px solid gainsboro;
}

.drak .user-name {
    color: white;
}

.drak .user-sign {
    color: rgb(199, 193, 193);
}

.drak .line-text,
.drak .line-img {
    color: rgb(199, 193, 193);
}

.drak .link {
    color: rgb(199, 193, 193);
}

.drak .line {
    border-bottom: 1px solid rgb(221, 221, 221);
}
</style>