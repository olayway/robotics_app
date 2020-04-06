import Vue from 'vue'
import Vuex from 'vuex'

import { login, register, refreshToken, logout } from '@/api'
import { EventBus } from '@/utils'
import createPersistedState from 'vuex-persistedstate'
// import { refreshToken } from '../api'

Vue.use(Vuex)

export default new Vuex.Store({
  plugins: [
    createPersistedState({
      storage: window.sessionStorage
    })
  ],
  state: {
    userData: {},
    accessTokenExp: null,
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
    getUserData(state) {
      return state.userData
    },
    getIsAuthenticated(state) {
      const exp = new Date(state.accessTokenExp * 1000)
      const now = new Date()
      console.log('EXP', exp)
      console.log('NOW', now)
      return now < exp
    },
    getNavTiles(state) {
      return state.navTiles
    },
    getDrawerState(state) {
      return state.drawerState
    }
  },
  mutations: {
    setUserData(state, payload) {
      state.userData = payload
    },
    setAccessTokenExp(state, payload) {
      state.accessTokenExp = payload
    },
    setDrawerState(state) {
      state.drawerState = !state.drawerState
    }
  },
  actions: {
    login({ commit }, payload) {
      return login(payload)
        .then(response => {
          // if (response.status === 200) {
          const access_token_exp = response.data.access_token_exp
          commit('setUserData', payload)
          commit('setAccessTokenExp', access_token_exp)
          // }
        })
        .catch(error => {
          console.log('Error Authenticating:', error)
          // EventBus.$emit('failedAuthentication', error)
        })
    },
    register({ commit, dispatch }, userData) {
      commit('setUserData', { userData })
      return register(userData)
        .then(() => dispatch('login', userData))
        .catch(error => {
          console.log('Error Registering:', error)
          EventBus.$emit('failedRegistering', error)
        })
    },
    refreshToken({ commit, dispatch }) {
      return refreshToken()
        .then(response => {
          // if (response.status === 200) {
          const access_token_exp = response.data.access_token_exp
          commit('setAccessTokenExp', access_token_exp)
          // }
        })
        .catch(error => {
          dispatch('logout', error)
          console.log('Error refreshing token:', error)
          // EventBus.$emit('failedTokenRefresh', error)
        })
    },
    logout({ commit }) {
      return logout()
        .then(() => {
          commit('setUserData', {})
          commit('setAccessTokenExp', null)
        })
        .catch(error => {
          console.log('Error Logging out ???', error)
        })
    },
    setDrawerState(context) {
      context.commit('setDrawerState')
    }
  },
  modules: {}
})
