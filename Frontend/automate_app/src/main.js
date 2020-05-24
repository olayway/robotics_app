import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'

import VueCookies from 'vue-cookies'
import vuetify from './plugins/vuetify'

Vue.config.productionTip = false

Vue.use(VueCookies)

// Vue.directive('click-outside', {
//   bind: function(el, binding, vnode) {
//     // console.log(binding.arg)
//     el.clickOutsideEvent = function(event) {
//       // console.log(el == event.target)
//       // console.log(el.contains(event.target))
//       if (event.target.classList[0] === 'v-overlay__scrim') {
//         vnode.context[binding.expression](event)
//       }
//     }
//     document.body.addEventListener('click', el.clickOutsideEvent)
//   },
//   unbind: function(el) {
//     document.body.removeEventListener('click', el.clickOutsideEvent)
//   }
// })

new Vue({
  router,
  store,
  vuetify,
  render: h => h(App)
}).$mount('#app')
