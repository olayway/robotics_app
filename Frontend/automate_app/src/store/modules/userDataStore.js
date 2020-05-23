import { login, register, refreshToken, logout, getUserUseCases } from '@/api'

export default {
  state: {
    userData: {},
    userUseCases: [],
    accessTokenExp: null,
    intervalID: null
  },
  getters: {
    getUserData(state) {
      return state.userData
    },
    getUserUseCases(state) {
      return (...indexes) => state.userUseCases.slice(...indexes)
    },
    getIsAuthenticated(state) {
      const exp = new Date(state.accessTokenExp * 1000)
      const now = new Date()
      return now < exp
    }
  },
  mutations: {
    setUserData(state, payload) {
      state.userData = payload
    },
    setUserUseCases(state, payload) {
      state.userUseCases = payload
    },
    setAccessTokenExp(state, payload) {
      state.accessTokenExp = payload
      console.log('EXP:', new Date(payload * 1000))
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
    login({ commit, dispatch }, { username, password }) {
      return login({ username, password })
        .then(response => {
          // if (response.status === 200) {
          const accessTokenExp = response.data.access_token_exp
          const companyName = response.data.company_name
          commit('setUserData', { username, companyName })
          commit('setAccessTokenExp', accessTokenExp)
          const now = new Date()
          const exp = new Date(accessTokenExp * 1000)
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
    register({ dispatch }, userData) {
      return register(userData)
        .then(() => dispatch('login', userData))
        .catch(error => {
          console.log('Error Registering:', error)
          // EventBus.$emit('failedRegistering', error)
        })
    },
    refreshToken({ commit, dispatch }) {
      return refreshToken()
        .then(response => {
          // if (response.status === 200) {
          const accessTokenExp = response.data.access_token_exp
          commit('setAccessTokenExp', accessTokenExp)
          // }
        })
        .catch(error => {
          dispatch('logout', error)
          console.log('Error refreshing token:', error)
          // EventBus.$emit('failedTokenRefresh', error)
        })
    },
    logout({ commit }) {
      console.log('LOGGING OUT')
      return logout()
        .then(response => {
          console.log('RESPONSE DATA MSG', response.data.msg)
          // commit('setUserData', {})
          // commit('setAccessTokenExp', null)
          commit('clearInterval')
          commit('resetState')
        })
        .catch(error => {
          console.log('Error Logging out ???', error)
        })
    },
    setUserUseCases({ commit }) {
      getUserUseCases()
        .then(response => {
          commit('setUserUseCases', response.data.your_use_cases)
        })
        .catch(error => console.log("Error fetching user's use cases:", error))
    }
  }
}
