<template>
    <div id="header" :class="$store.state.settings.fontsize">
        <el-icon @click="back()" size="24px" class="active" :class="$store.state.isback!=0?'':'noback'"><ArrowLeft /></el-icon>
        <span>{{ $route.meta.title }}</span>
        <el-badge :is-dot="ismessage" class="item active">
            <!-- <el-icon size="24px"><Message /></el-icon> -->
        </el-badge>
    </div>
</template>

<script>
// import { tsImportEqualsDeclaration } from '@babel/types'
import {ArrowLeft, Message} from '@element-plus/icons-vue'

export default {
    name: 'header',
    components: {ArrowLeft, Message},
    data(){
        return {
            ismessage: false,  // 是否存在最新公告
            page: ['历史', '识别', '我的']
        }
    },

    methods: {
        messages(){
            alert("公告")
        },

        back(){
            this.$router.go(-1)
            this.$store.state.isback--
        }
    }
}
</script>

<style scoped>
/* ============================== 布局 ============================== */
#header{
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 10px;
}
.item{
    width: 24px;
    height: 24px;
}
.noback{
    visibility: hidden;
}


/* ============================== 字体大小 ============================== */
.big{
    font-size: 20px;
}
.median{
    font-size: 16px;
}
.small{
    font-size: 14px;
}


/* ============================== 主题 ============================== */
/* 配色 - 纯白 */
.pure #header{
    background-color: rgb(240, 240, 240);
}

/* 配色 - 黑夜 */
.drak #header{
    background-color: #393D49;
    color: #888
}
.drak .active:active{
    background-color: white;
}
</style>