<template>
  <Header v-if='$store.state.user.id?true:false' />

  <div id="main">
    <router-view></router-view>
  </div>

  <Bottom v-if='$store.state.user.id?true:false' />
</template>

<script>
import Bottom from './components/bottom.vue'
import Header from './components/header.vue'

export default {
  name: 'App',
  components: { Header, Bottom },

  mounted() {
    // 初始化主题
    document.getElementById('app').className = this.$store.state.settings.theme
  },
}

// 阻止放大
window.onload = function () {
  document.addEventListener('touchstart', function (event) {
    if (event.touches.length > 1) {
      event.preventDefault()
    }
  })
  document.addEventListener('gesturestart', function (event) {
    event.preventDefault()
  })
}

</script>

<style>
/* ============================== 布局 ============================== */
* {
  margin: 0;
  padding: 0;
}

#app,
html,
body {
  width: 100%;
  height: 100%;
}

#app {
  display: flex;
  flex-direction: column;
}

#main {
  flex: 1;
  display: flex;
  overflow-y: auto;
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
.drak #main {
  /* background-image: linear-gradient(to right, #434343 0%, black 100%); */
  background-color: #434343;
}

/* ============================== 总体 ============================== */
a {
  text-decoration: none;
}
</style>
