import Vue from 'vue'
import Vuex from 'vuex'

import { authenticate, register } from '@/api'
import { isValidJWT, EventBus } from '@/utils'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    userData: {},
    jwt: '',
    navTiles: [
      { title: 'Home', subtitles: [] },
      { title: 'Why Automate', subtitles: [] },
      {
        title: 'Learn',
        subtitles: ['Tutorials', 'Articles', 'Courses']
      },
      { title: 'Subscribe', subtitles: [] },
      { title: 'Contact', subtitles: [] }
    ],
    drawerState: false
  },
  getters: {
    isAuthenticated(state) {
      return isValidJWT(state.jwt)
    },
    navTiles(state) {
      return state.navTiles
    },
    drawerState(state) {
      return state.drawerState
    }
  },
  mutations: {
    setUserData(state, payload) {
      console.log('setUserData payload =', payload)
      state.userData = payload
    },
    setJwtToken(state, payload) {
      console.log('setJwtToken payload =', payload)
      localStorage.token = payload
      state.jwt = payload
    },
    toggleDrawer(state) {
      state.drawerState = !state.drawerState
    }
  },
  actions: {
    login(context, credentials) {
      context.commit('setUserData', credentials)
      return authenticate(credentials)
        .then(response =>
          context.commit('setJwtToken', response.data.access_token)
        )
        .catch(error => {
          console.log('Error Authenticating:', error)
          EventBus.$emit('failedAuthentication', error)
        })
    },
    register(context, userData) {
      context.commit('setUserData', { userData })
      return register(userData)
        .then(context.dispatch('login', userData))
        .catch(error => {
          console.log('Error Registering:', error)
          EventBus.$emit('failedRegistering', error)
        })
    },
    toggleDrawer(context) {
      context.commit('toggleDrawer')
    }
  },
  modules: {}
})
