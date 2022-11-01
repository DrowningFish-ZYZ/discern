<template>
    <div id="account" :class="$store.state.settings.fontsize">
        <!-- 设置列表 -->
        <div class="settings">
            <router-link to="/user/account/reset/pwd" @click="active()">
                <div class="line">
                    <el-icon size="20px" class="line-img">
                        <Lock />
                    </el-icon>
                    <span class="line-text">重置密码</span>
                    <el-icon size="20px" class="link">
                        <ArrowRight />
                    </el-icon>
                </div>
            </router-link>

            <router-link to="/user/account/reset/sq" @click="active()">
                <div class="line last-line">
                    <el-icon size="20px" class="line-img">
                        <ChatDotRound />
                    </el-icon>
                    <span class="line-text">重置密保</span>
                    <el-icon size="20px" class="link">
                        <ArrowRight />
                    </el-icon>
                </div>
            </router-link>
        </div>
    </div>
</template>

<script>
import { ChatDotRound, Lock, ArrowRight } from '@element-plus/icons-vue'

export default {
    name: 'account',
    components: { ChatDotRound, Lock, ArrowRight },

    methods: {
        active() {
            this.$store.state.isback++
        }
    }
}
</script>

<style scoped>
/* ===================================== 布局 ===================================== */
/* 设置列表 */
#account {
    flex: 1;
    padding: 15px;
}

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

.link {
    position: absolute;
    right: 15px;
    color: gray;
}

.line-text {
    margin-left: 5px;
    flex: 1;
    padding: 8px 8px;
}

.last-line {
    border: none !important;
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
.pure .settings {
    box-shadow: 1px 2px 5px gray;
    border: 1px solid rgb(206, 202, 202);
}

.pure .user-box .user-name,
.pure .line-img,
.pure .line-text {
    color: black;
}
.pure .line {
    border-bottom: 1px solid rgb(190, 189, 189);
}

/* 黑夜 */
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