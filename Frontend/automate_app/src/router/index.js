import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import store from '@/store'

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
    path: '/use-case',
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
      if (!store.getters.isAuthenticated) {
        console.log('not authenticated')
        next('/login')
      } else {
        next()
      }
    },
    component: () =>
      import(/* webpackChunkName: "user-panel" */ '../views/UserPanel.vue')
  },
  {
    path: '/new-usecase',
    name: 'NewUseCase',
    component: () =>
      import(/* webpackChunkName: "new-usecase" */ '../views/NewUseCase.vue')
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
