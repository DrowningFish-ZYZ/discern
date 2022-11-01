<template>
    <div id="bottom" :class="$store.state.settings.fontsize">
        <div class="btn" @click="active(0)" :class="$store.state.inpage==0?'active':''">
            <router-link to="/record">
                <el-icon size="24px"><List /></el-icon>
                <p>历史</p>
            </router-link>
        </div>

        <div class="btn" @click="active(1)" :class="$store.state.inpage==1?'active':''">
            <router-link to="/">
                <el-icon size="24px"><Grid /></el-icon>
                <p>识别</p>
            </router-link>
        </div>

        <div class="btn" @click="active(2)" :class="$store.state.inpage==2?'active':''">
            <router-link to="/user">
                <el-icon size="24px"><UserFilled /></el-icon>
                <p>我的</p>
            </router-link>
        </div>
    </div>
</template>

<script>
import {Grid, List, UserFilled} from '@element-plus/icons-vue'

export default {
    name: 'bottom',
    components: {Grid, List, UserFilled},

    methods: {
        active(index){
            this.$store.state.inpage = index
            this.$store.state.isback = 0
            localStorage.inpage = index
        }
    }
}
</script>

<style scoped>
/* ============================== 布局 ============================== */
#bottom{
    display: flex;
    align-items: center;
    justify-content: space-around;
    padding: 15px 10px;
}
a{
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-decoration: none;
    
}

/* ============================== 字体设置 ============================== */


/* ============================== 主题 ============================== */
/* 主题 - 纯白 */
.pure #bottom{
    background-color: rgb(240, 240, 240);
}
.pure a{
    color: gray;
}
.pure .active a{
    color: black;
}


/* 主题 - 黑夜 */
.drak #bottom{
    background-color: #393D49;
}
.drak a{
    color: #888888;
}
.drak .active a{
    color: white;
}
.drak a:active{
    background-color: white;
}
</style>