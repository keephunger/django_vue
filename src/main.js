import Vue from 'vue'
import App from '@/App.vue'
import "todomvc-app-css/index.css"
import "todomvc-common/base.css"
import "todomvc-common/base"
import store from '@/store' 
import router from '@/router'

Vue.config.productionTip = false

// Vue.use(VueRouter)

const vue = new Vue({
  router,
  store,
  render: h => h(App)
})

vue.$mount('#app')
