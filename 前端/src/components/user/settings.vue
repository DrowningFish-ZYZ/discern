<template>
    <div id="set" :class="$store.state.settings.fontsize">
        <div class="box">
            <div class="header">
                <span>主题<span style="font-size: 12px; letter-spacing: 0px; color: gray;">【注意: 设置不能云端存储, 只能本地存储】</span></span>
                <el-icon class="icon" size="16px"><Switch /></el-icon>
            </div>
            <div class="context">
                <li @click="cutTheme(theme)" class="lis" v-for="theme in $store.state.settings.themes">
                    {{ theme }}
                    <el-icon size="16px" class="link" :class="theme==$store.state.settings.theme?'show':''"><Select /></el-icon>
                </li>
            </div>
        </div>

        <div class="box">
            <div class="header">
                <span>字体大小</span>
                <el-icon class="icon" size="16px"><Operation /></el-icon>
            </div>
            <div class="context">
                <li @click="cutFontSize(fontsize)" class="lis" v-for="fontsize in $store.state.settings.fontsizes">
                    {{ fontsize }}
                    <el-icon size="16px" class="link" :class="fontsize==$store.state.settings.fontsize?'show':''"><Select /></el-icon>
                </li>
            </div>
        </div>
    </div>
</template>

<script>
import { Select, Switch, Operation } from '@element-plus/icons-vue'

export default {
    name: 'settings',
    components: { Select, Switch, Operation },
    data() {
        return {
            lis: document.getElementsByClassName('lis')
        }
    },
    methods: {
        cutTheme(theme) {
            this.$store.state.settings.theme = theme
            document.getElementById('app').className = this.$store.state.settings.theme
            localStorage.theme = theme
        },

        cutFontSize(fontsize){
            this.$store.state.settings.fontsize = fontsize
            localStorage.fontsize = fontsize
        }
    }
}
</script>

<style scoped>
/* ===================================== 布局 ===================================== */
/* 设置列表 */
#set {
    width: 100%;
    padding: 10px;
}
.box{
    padding: 5px;
    border-radius: 5px;
    margin-bottom: 15px;
}
.header {
    display: flex;
    align-items: center;
    padding: 10px;
    position: relative;
    letter-spacing: 5px;
}
.icon{
    position: absolute;
    right: 10px;
}

.lis {
    display: flex;
    align-items: center;
    padding: 10px;
    position: relative;
}
.link {
    position: absolute;
    right: 10px;
    display: none;
}
.show{
    display: block;
}

/* ============================== 字体设置 ============================== */
.big .lis{
    font-size: 18px;
}
.median .lis{
    font-size: 16px;
}
.small .lis{
    font-size: 14px;
}

.big .header{
    font-size: 24px;
}
.median .header{
    font-size: 18px;
}
.small .header{
    font-size: 14px;
}


/* ===================================== 配色 ===================================== */
/* 纯白 */
.pure .box{
    box-shadow: 1px 2px 5px gray;
    border: 1px solid rgb(206, 202, 202);
    color: gray;
}
.pure .header{
    color: black;
    border-bottom: 1px solid gray;
}
.pure .show {
    color: black;
}

/* 黑夜 */
.drak .box {
    box-shadow: 1px 1px 10px rgb(210, 207, 207);
    border: 1px solid gainsboro;
    color: grey;
}
.drak .header{
    color: white;
    border-bottom: 1px solid white;
}
.drak .show {
    color: white;
}
</style>