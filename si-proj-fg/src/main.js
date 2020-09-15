import Vue from 'vue'
import App from './App.vue'
import store from './store'
import config from '@/config'
import iView from 'iview';
import 'iview/dist/styles/iview.css';
// import Vuex from 'vuex'
// Vue.use(Vuex);

import router from './router/index.js'
Vue.use(iView);

Vue.config.productionTip = false
/**
 * @description 全局注册应用配置
 */
Vue.prototype.$config = config

import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap';


import 'assets/css/icofont.css'
import 'assets/css/style.css'

new Vue({
  render: h => h(App),
  // 挂载路由
  router,
  store,
}).$mount('#app')
