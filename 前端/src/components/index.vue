<template>
    <div id="index">
        <!-- 顶部 -->
        <div class="top">
            <el-select v-model="model" placeholder="识别类型" :popper-append-to-body="false">
                <el-option-group v-for="group in options" :key="group.label" :label="group.label">

                    <el-option v-for="item in group.discernmodel_set" :key="item.value" :label="item.label"
                        :value="item.id" />

                </el-option-group>
            </el-select>
        </div>

        <!-- 中间图像展示 -->
        <div class="index-box" id="index-box">
            <el-carousel v-if="$store.state.index.imgFile?true:false" :interval="4000" :height="imgHeight" :autoplay="false">
                <el-carousel-item v-for="item in $store.state.index.imgs">
                    <img :src="item" v-viewer />
                </el-carousel-item>
            </el-carousel>
        </div>

        <!-- 底部按钮区域 [浮动] -->
        <div class="index-bottom">
            <div class="index-bottom-box">
                <input type="file" id="file" accept="image/*" style="display: none;" @change="getPicture($event)" />
                <el-button type="primary" circle @click="callFile()">
                    <el-icon size="25px">
                        <PictureRounded />
                    </el-icon>
                </el-button>
                <el-button type="success" circle @click="discern()">
                    <el-icon size="25px">
                        <View />
                    </el-icon>
                </el-button>
            </div>
        </div>
    </div>
</template>

<script>
import { View, PictureRounded } from '@element-plus/icons-vue'
import { ElMessage } from 'element-plus'
import utils from '@/utils'

export default {
    name: 'index',
    components: { View, PictureRounded },
    data() {
        return {
            imgHeight: '',
            model: '',
            options: []
        }
    },

    methods: {
        callFile() { document.getElementById('file').click() },
        // 获取图片
        getPicture(e) {
            let src = window.URL.createObjectURL(e.target.files[0]);
            this.$store.state.index.imgs = []
            this.$store.state.index.imgs.push(src)
            this.$store.state.index.imgFile = e.target.files[0]
        },
        discern() {
            if(!this.$store.state.index.imgFile){
                ElMessage({message: '请选择图片!', type: 'warning'})
                return 
            }else if(!this.model){
                ElMessage({message: '请选择模型!', type: 'warning'})
                return 
            }

            // 1.准备数据
            let formdata = new FormData()
            formdata.append('image', this.$store.state.index.imgFile, this.$store.state.index.imgFile.name)
            formdata.append('model', this.model)
            // 2. 识别图像
            utils.request('正在识别', {timeout: 20000, url: `discern/${this.$store.state.user.id}/`, method: 'post', headers: {token: this.$store.state.user.token}, data: formdata},
                res => {
                    // 将获取到的响应图片加入到本地显示
                    this.$store.state.index.imgs.push(`${this.$store.state.baseIP}${res.data}`)
                    this.$store.state.index.imgs = this.$store.state.index.imgs.reverse()
                    // 刷新组件
                    this.$forceUpdate()
                }
            )
        },
    },

    mounted() {
        // 获取模型数据
        this.imgHeight = `${document.getElementById('index-box').clientHeight - 30}px`
        utils.request('正在加载', {url: 'model/', method: 'get', headers: {token: this.$store.state.user.token}},
            res => {
                this.options = res.data
            }
        )

    }
}
</script>

<style scoped>
/* ============================== 布局 ============================== */
#index {
    flex: 1;
    padding: 15px;
    display: flex;
    flex-direction: column;
}

.top {
    margin-bottom: 10px;
}

.index-box {
    flex-basis: 85%;
    padding: 5px 5px;
    overflow: hidden;
}

.index-box img {
    max-height: 100%;
    max-width: 100%;
    border-radius: 5px;
}

.index-bottom {
    flex: 1;
    position: relative;
}

.index-bottom-box {
    position: absolute;
    bottom: 0;
    width: 100%;
    display: flex;
    justify-content: space-around;
}

button {
    width: 40px;
    height: 40px;
}

.el-select {
    width: 100%;
}
.el-carousel__item {
    height: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
}
.el-carousel,
.el-carousel__container {
    height: 100% !important;
}

/* ============================== 字体大小 ============================== */
.big {
    font-size: 16px;
}

.median {
    font-size: 12px;
}

.small {
    font-size: 10px;
}

/* ============================== 主题 ============================== */
/* 主题 - 黑夜【drak】 */
.drak .index-bottom-box {
    background-color: #cfc9c940;
    padding: 5px 0px;
    border-radius: 5px;
    border: 1px solid rgb(146, 144, 144);
    box-shadow: 2px 2px 10px rgb(187, 186, 186);
}

.drak .index-box img {
    box-shadow: 1px 1px 10px rgb(182, 177, 177);
}
.drak .el-select /deep/ .el-input__wrapper {
    background-color: rgba(128, 128, 128, 0.095);
}


/* 主题 - 白天【pure】 */
.pure .index-bottom-box {
    background-color: #95959540;
    padding: 5px 0px;
    border-radius: 5px;
    border: 1px solid rgb(146, 144, 144);
    box-shadow: 2px 2px 10px rgb(187, 186, 186);
}

.pure .index-box img {
    box-shadow: 1px 1px 10px rgb(100, 92, 92);
}
</style>