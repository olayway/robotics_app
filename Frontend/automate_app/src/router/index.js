import Vue from 'vue'
import VueRouter from 'vue-router'
import store from '@/store'
import Home from '../views/Home.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/about',
    name: 'About',
    component: () =>
      import(/* webpackChunkName: "about" */ '../views/About.vue')
  },
  {
    path: '/learn',
    name: 'Learn',
    component: () =>
      import(/* webpackChunkName: "learn" */ '../views/Learn.vue')
  },
  {
    path: '/use-case/:id',
    name: 'UseCase',
    component: () =>
      import(/* webpackChunkName: "use-case" */ '../views/UseCase.vue')
  },
  {
    path: '/register',
    name: 'Register',
    component: () =>
      import(/* webpackChunkName: "register" */ '../views/Register.vue')
  },
  {
    path: '/login',
    name: 'Login',
    component: () =>
      import(/* webpackChunkName: "login" */ '../views/Login.vue')
  },
  {
    path: '/user-panel',
    name: 'UserPanel',
    beforeEnter(to, from, next) {
      if (!store.getters.getIsAuthenticated) {
        console.log('not authenticated')
        next('/login')
      } else {
        console.log('redir to user panel')
        store.dispatch('setUserUseCases')
        next()
      }
    },
    component: () =>
      import(/* webpackChunkName: "user-panel" */ '../views/UserPanel.vue')
  },
  {
    path: '/new-case',
    name: 'NewUseCase',
    beforeEnter(to, from, next) {
      if (!store.getters.getIsAuthenticated) {
        console.log('not authenticated')
        next('/login')
      } else {
        console.log('redir to user panel')
        next()
      }
    },
    component: () =>
      import(/* webpackChunkName: "new-use-case" */ '../views/NewUseCase.vue')
  },
  {
    path: '/settings',
    name: 'Settings',
    component: () =>
      import(/* webpackChunkName: "settings" */ '../views/Settings.vue')
  }
]

export default new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})
