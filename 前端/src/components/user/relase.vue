<template>
    <div id="relase">
        <div class="relase-box">
            <h2><i>Discern Version</i></h2>
            <h3>2.1</h3>
        </div>

        <div class="relase-bottom">
            <span>本产品由 <span style="color: sandybrown">violet</span> 独立创作</span>
            <span>版权所有归 <span style="color: sandybrown">violet</span> &copy</span>
        </div>
    </div>
</template>

<script>
import {Setting, DocumentCopy, ArrowRight} from '@element-plus/icons-vue'

export default {
    name: 'relase',
    components: {Setting, DocumentCopy, ArrowRight}
}
</script>

<style scoped>
/* ===================================== 布局 ===================================== */
/* 设置列表 */
#relase{
    flex: 1;
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
    position: relative;
}
.relase-box{
    width: 300px;
    height: 300px;
    border-radius: 50%;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
}
.relase-box h3{
    margin: 15px;
}
.relase-box h2{
    letter-spacing: 1.5px;
}
.relase-bottom{
    position: absolute;
    bottom: 15px;
    display: flex;
    flex-direction: column;
    text-align: center;
    font-size: 12px;
    letter-spacing: 1px;
}

@keyframes sun{
    100%{
        background-position: -400% 0;
    }
}


/* ===================================== 配色 ===================================== */
/* 纯白 */
.pure .relase-box{
    background: linear-gradient(90deg,#3f535c,#45313c,#454330,#3f5e6d);
    background-size: 400%;
    animation: sun 12s infinite;
}
.pure .relase-box{
    color: rgb(254, 112, 112);
}
.pure .relase-bottom{
    color: gray;
}

/* 黑夜 */
.drak .relase-box{
    color: aliceblue;
}
.drak .relase-bottom{
    color: grey;
}
</style>