import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import vuetify from './plugins/vuetify'
import axios from 'axios'
import VueAxios from 'vue-axios'
import VueCookies from 'vue-cookies'

// import './assets/css/main.css'
Vue.prototype.$axios = axios
Vue.config.productionTip = false

axios.defaults.baseURL = 'http://localhost:5000'
axios.defaults.withCredentials = true

Vue.use(VueAxios, axios, VueCookies)

Vue.directive('click-outside', {
  bind: function(el, binding, vnode) {
    // console.log(binding.arg)
    el.clickOutsideEvent = function(event) {
      // console.log(el == event.target)
      // console.log(el.contains(event.target))
      if (event.target.classList[0] === 'v-overlay__scrim') {
        vnode.context[binding.expression](event)
      }
    }
    document.body.addEventListener('click', el.clickOutsideEvent)
  },
  unbind: function(el) {
    document.body.removeEventListener('click', el.clickOutsideEvent)
  }
})

new Vue({
  router,
  store,
  vuetify,
  render: h => h(App)
}).$mount('#app')
