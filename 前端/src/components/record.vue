<template>
    <div id="record" :class="$store.state.settings.fontsize">
        <el-empty v-if="data == null" description="空空如也" />
        <div v-else class="record-box">

            <div class="record-item" v-for="item, index in data">

                <img :src='$store.state.baseIP + item.image' v-viewer />
                <div style="flex: 1; display: flex; align-items: center;"
                    @click="$router.push({ path: '/record/detail', query: { 'result': item.result, 'image': item.image } }); $store.state.isback++">
                    <span>{{ item.date }}</span>
                    <div @touchend.prevent="move(index)">
                        <span>{{ item.discernType }}</span>
                        <span>{{ item.discernModel }}</span>
                    </div>
                </div>

                <div class="delete">
                    <el-button type="text" style="color: red" @click="deleteRecord(item.id)">
                        <el-icon size="20px" class="link">
                            <Delete />
                        </el-icon>
                    </el-button>
                </div>
            </div>

        </div>
    </div>
</template>

<script>
import { Delete } from '@element-plus/icons-vue'
import utils from '@/utils'

export default {
    name: 'record',
    components: { Delete },
    data() {
        return {
            data: null,
        }
    },

    methods: {
        // 移动展示删除
        move(index) {
            let el = document.getElementsByClassName('record-item')[index]
            if (el.style.right == '50px') {
                el.style.right = '0px'
            } else {
                el.style.right = '50px'
            }
        },

        deleteRecord(id) {
            if (confirm("是否删除")) {
                utils.request('正在删除', { url: `record/${this.$store.state.user.id}/`, method: 'delete', headers: { token: this.$store.state.user.token }, data: {'recordID': id} },
                    res => {
                        this.data = res.data ? res.data : null
                        this.$forceUpdate()
                    }
                )
            }
        }
    },

    mounted() {
        utils.request('正在加载', { url: `record/${this.$store.state.user.id}/`, method: 'get', headers: { token: this.$store.state.user.token } },
            res => {
                this.data = res.data ? res.data : null
            }
        )
    }
}
</script>

<style scoped>
/* ============================== 布局 ============================== */
#record {
    flex: 1;
    display: flex;
    padding: 5px;
    overflow: hidden;
}

.el-empty {
    flex: 1;
}

.record-box {
    flex: 1;
    display: flex;
    flex-direction: column;
}

.record-item {
    margin-bottom: 5px;
    border-radius: 5px;
    display: flex;
    align-items: center;
    position: relative;

    transition: all 1.5s;
    -moz-transition: all 1.5s;
    -webkit-transition: all 1.5s;
    -o-transition: all 1.5s;
}

.record-item div>span {
    flex: 1;
    text-align: left;
    padding-left: 20px;
}

.record-item img {
    width: 70px;
    height: 50px;
    border-top-left-radius: 5px;
    border-bottom-left-radius: 5px;
    object-fit: cover;
    object-position: 50% 20%;
}

.record-item div>div span {
    display: flex;
    flex-direction: column;
    text-align: right;
    padding-right: 5px;
    /* flex-basis: 35%; */
}

.delete {
    position: absolute;
    right: -30px;
    /* background-color: red; */
    height: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
    color: red;
}

/* ============================== 字体大小 ============================== */
.big .record-item>span {
    font-size: 18px;
}

.median .record-item>span {
    font-size: 16px;
}

.small .record-item>span {
    font-size: 14px;
}

/* ============================== 配色 ============================== */
/* 白天 */
.pure .record-item {
    border: 1px solid gray;
    background-color: rgb(222, 222, 222);
}

.pure .record-item>span {
    color: orange;
}

.pure .record-item>div span {
    color: cadetblue;
    font-weight: 700;
}

.pure .record-item>div span:last-child {
    color: rgb(126, 126, 126);
}

/* 黑夜 */
.drak .record-item {
    border: 1px solid rgb(219, 211, 211);
    background-color: rgb(110, 104, 104);
}

.drak .record-item>span {
    color: rgb(233, 198, 131);
}

.drak .record-item>div span {
    color: rgb(128, 186, 188);
    font-weight: 700;
}

.drak .record-item>div span:last-child {
    color: rgb(189, 188, 188);
}
</style>