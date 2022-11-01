<template>
    <div id="detail">
        <img :src="$store.state.baseIP + $route.query.image" v-viewer>

        <div class="demo-collapse">
            <el-collapse v-model="activeNames" @change="handleChange">
                <el-collapse-item :title="item.label + ' ' + item.pro" :name="index" v-for="item, index in items">
                    <div>
                        {{ item.info }}
                    </div>
                </el-collapse-item>
            </el-collapse>
        </div>
    </div>
</template>

<script>
import utils from '@/utils'

export default {
    name: 'detail',
    data() {
        return {
            items: []
        }
    },

    mounted() {
        let key = []
        let arr = this.$route.query.result.split(',')
        arr = arr.splice(0, arr.length - 1)
        for (let i = 0; i < arr.length; i++) {
            let item = arr[i].split(' ')
            let label = item.splice(0, item.length - 1).join(' ')
            let pro = `${parseFloat(item[item.length - 1]) * 100}%`
            if (!key.includes(label)) {
                this.items.push({
                    label: label,
                    pro: pro,
                    info: '暂无数据，请等待管理员添加'
                })
                key.push(label)
            }
        }


        utils.request('正在加载', { url: `detail/?query=${this.$route.query.result}`, method: 'get', headers: { token: this.$store.state.user.token } },
            res => {
                let data = res.data;
                for (let i = 0; i < data.length; i++) {
                    for (let j = 0; j < this.items.length; j++) {
                        if (data[i].label == this.items[j].label) {
                            this.items[j].info = data[i].info
                            break
                        }
                    }
                }
            }
        )
    }
}
</script>

<style scoped>
#detail {
    flex: 1;
    display: flex;
    flex-direction: column;
    background-color: white;
}

#detail img {
    max-width: 100%;
    height: 300px;
    object-fit: contain;
}

.demo-collapse {
    padding: 5px 10px;
}

.el-collapse-item__content div {
    text-indent: 2em;
}
</style>