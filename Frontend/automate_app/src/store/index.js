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
    intervalID: null,
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
      console.log('EXP:', new Date(payload * 1000))
    },
    setDrawerState(state) {
      state.drawerState = !state.drawerState
    },
    setIntervalID(state, payload) {
      state.intervalID = payload
    },
    clearInterval(state) {
      clearInterval(state.intervalID)
      state.intervalID = null
    }
  },
  actions: {
    login({ commit, dispatch }, payload) {
      return login(payload)
        .then(response => {
          // if (response.status === 200) {
          const access_token_exp = response.data.access_token_exp
          commit('setUserData', payload)
          commit('setAccessTokenExp', access_token_exp)
          const now = new Date()
          const exp = new Date(access_token_exp * 1000)
          const interval = exp - now - 30000
          const intervalID = setInterval(() => {
            dispatch('refreshToken')
          }, interval)
          commit('setIntervalID', intervalID)
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
        .then(response => {
          commit('setUserData', {})
          commit('setAccessTokenExp', null)
          commit('clearInterval')
          console.log(response.data.msg)
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
