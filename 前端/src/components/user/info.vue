<template>
    <div id="info">
        <div class="info-header">
            <h3>
                {{ $store.state.user.username }}
                <el-icon v-if="$store.state.user.gender == 1" size="15px" style="color: red; margin-left: 5px;">
                    <Female />
                </el-icon>

                <el-icon v-else size="15px" style="color: aqua; margin-left: 5px;">
                    <Male />
                </el-icon>
            </h3>
            <span>{{ $store.state.user.info }}</span>
            <el-button class="edit" type="text" @click="openEdit()">
                <el-icon size="25px">
                    <Edit />
                </el-icon>
            </el-button>
        </div>

        <div class="info-img">
            <input type="file" id="file" accept="image/*" style="display: none;" @change="getPicture($event)" />
            <img :src="$store.state.baseIP + $store.state.user.headPortrait" @click='updateImg()' />
            <span>点击修改头像</span>
        </div>

        <div class="info-box">
            <div class="info-item">
                <label>邮箱</label>
                <p>{{ $store.state.userDetail.email }}</p>
            </div>
            <div class="info-item">
                <label>电话</label>
                <p>{{ $store.state.userDetail.phone }}</p>
            </div>
        </div>
    </div>
</template>

<script>
import { Edit, Female, Male } from '@element-plus/icons-vue'
import utils from '@/utils'

export default {
    name: 'info',
    components: { Edit, Female, Male },
    methods: {
        openEdit() {
            this.$store.state.isback++
            this.$router.push('/user/info/edit')
        },
        updateImg() {
            document.getElementById('file').click()
        },
        getPicture(e) {
            // 修改头像
            let file = e.target.files[0]
            let formdata = new FormData()
            formdata.append('image', file, file.name)
            let requestObj = {
                url: `reset/portrait/${this.$store.state.user.id}/`,
                method: 'post',
                headers: { 'Content-Type': 'multipart/form-data', 'token': this.$store.state.user.token },
                data: formdata
            }
            utils.request('正在修改', requestObj,
                res => {
                    this.$store.state.user.headPortrait = res.data.headPortrait
                    localStorage.headPortrait = res.data.headPortrait
                    this.$forceUpdate()
                }
            )
        }
    },

    mounted() {
        // 如果 this.$sotre.state.userDetail 里没有数据，那么便向后端请求
        if (!this.$store.state.userDetail.email) {
            utils.request('加载中', { url: `user/${this.$store.state.user.id}/`, method: 'get', headers: { token: this.$store.state.user.token } },
                res => {
                    this.$store.state.userDetail.email = res.data.email ? res.data.email : '暂无'
                    this.$store.state.userDetail.phone = res.data.phone ? res.data.phone : '暂无'
                }
            )
        }
    }
}
</script>

<style scoped>
#info {
    flex: 1;
    position: relative;
    display: flex;
    flex-direction: column;
}

.info-header {
    background-image: url(../../assets/3.jpg);
    height: 120px;
    border-bottom: 1px solid grey;
    padding: 15px;
    color: white;
    letter-spacing: 1px;
    position: relative;
}

.info-header h3 {
    display: flex;
    align-items: center;
}

.info-header span {
    font-size: 10px;
    color: rgb(192, 183, 183);
}

.info-box {
    padding: 45px;
    margin-top: 25px;
}

.info-item {
    display: flex;
    align-items: center;
    justify-content: center;
    margin-bottom: 10px;
}

.info-item label {
    font-size: 14px;
    flex-basis: 30%;
}

.info-item p {
    flex: 1;
    padding: 5px 0px;
    font-size: 14px;
}

.edit {
    position: absolute;
    right: 10px;
    top: 10px;
    color: white;
}

.info-img {
    width: 100%;
    display: flex;
    justify-content: center;
    position: absolute;
    flex-direction: column;
    align-items: center;
    top: 100px;
}

.info-img span {
    font-size: 12px;
    margin-top: 5px;
}

.info-img img {
    width: 75px;
    height: 75px;
    object-fit: cover;
    object-position: 50% 20%;
    border-radius: 50%;

}

/* ===================================== 配色 ===================================== */
/* 纯白 */
.pure .info-item {
    border-bottom: 1px solid black;
}

.pure img {
    border: 2px solid black;
}

/* 纯白 */
.drak .info-item {
    border-bottom: 1px solid grey;
    color: rgb(214, 208, 208);
}

.drak img {
    border: 2px solid white;
}

.drak .info-img {
    color: gray;
}
</style>