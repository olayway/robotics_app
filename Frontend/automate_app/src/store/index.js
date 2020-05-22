import Vue from 'vue'
import Vuex from 'vuex'

import { login, register, refreshToken, logout, getUserUseCases } from '@/api'
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
    userUseCases: [],
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
    drawerState: false,
    useCaseData: {
      basic_info: {
        customer: '',
        applications: [],
        industry: '',
        country: '',
        company_size: ''
      },
      content: {
        article_title: '',
        article_sections: [{ title: '', content: '' }],
        bullet_points: [{ title: '', content: ['', '', ''] }]
      },
      mainImage: '',
      images: [],
      status: 'draft'
    }
  },
  getters: {
    getUserData(state) {
      return state.userData
    },
    getUserUseCases(state) {
      return state.userUseCases
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
    },
    getBasicInfo(state) {
      return state.useCaseData.basic_info
    },
    getContent(state) {
      return state.useCaseData.content
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
    setDrawerState(state) {
      state.drawerState = !state.drawerState
    },
    setIntervalID(state, payload) {
      state.intervalID = payload
    },
    clearInterval(state) {
      clearInterval(state.intervalID)
      state.intervalID = null
    },
    setBasicInfo(state, payload) {
      const useCaseData = state.useCaseData
      Object.assign(useCaseData, {
        basic_info: { ...useCaseData.basic_info, ...payload }
      })
    },
    setArticleTitle(state, payload) {
      state.useCaseData.content.article_title = payload
    },
    addNewSection(state) {
      var articleSectionsRef = state.useCaseData.content.article_sections
      const newSection = { title: '', content: '' }
      const articleSections = articleSectionsRef
      articleSections.push(newSection)
      articleSectionsRef = articleSections
    },
    deleteSection(state, payload) {
      var articleSections = state.useCaseData.content.article_sections
      articleSections.splice(payload, 1)
      state.useCaseData.content.article_sections = articleSections
    },
    setSectionData(state, { userInput, tabIndex }) {
      const sectionData = {
        ...state.useCaseData.content.article_sections[tabIndex],
        ...userInput
      }
      state.useCaseData.content.article_sections[tabIndex] = sectionData
    },
    addNewSectionBP(state) {
      var BPSectionsRef = state.useCaseData.content.bullet_points
      const newBPSection = { title: '', content: ['', '', ''] }
      const BPSections = BPSectionsRef
      BPSections.push(newBPSection)
      BPSectionsRef = BPSections
    },
    deleteSectionBP(state, payload) {
      console.log('BP TB REMOVED', payload)
      var BPSections = state.useCaseData.content.bullet_points
      BPSections.splice(payload, 1)
      state.useCaseData.content.bullet_points = BPSections
    },
    setSectionDataBP(state, { userInput, tabIndex }) {
      if (Object.keys(userInput)[0] == 'title') {
        const BPsectionData = {
          ...state.useCaseData.content.bullet_points[tabIndex],
          ...userInput
        }
        state.useCaseData.content.bullet_points[tabIndex] = BPsectionData
      } else {
        const { text, pointNo } = userInput.content
        state.useCaseData.content.bullet_points[tabIndex].content[
          pointNo
        ] = text
      }
    },
    uploadMainImage(state, file) {
      state.useCaseData.mainImage = file
    },
    uploadImage(state, files) {
      state.useCaseData.images = [...files]
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
          EventBus.$emit('failedRegistering', error)
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
          commit('setUserData', {})
          commit('setAccessTokenExp', null)
          commit('clearInterval')
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
    },
    setDrawerState({ commit }) {
      commit('setDrawerState')
    },
    setBasicInfo({ commit }, userInput) {
      console.log('userInput', userInput)
      commit('setBasicInfo', userInput)
    },
    setArticleTitle({ commit }, userInput) {
      console.log('userInput', userInput)
      commit('setArticleTitle', userInput)
    },
    addNewSection({ commit }) {
      commit('addNewSection')
    },
    deleteSection({ commit }, { tabIndex }) {
      console.log('delete tab number', tabIndex)
      commit('deleteSection', tabIndex)
    },
    setSectionData({ commit }, payload) {
      console.log('userInput', payload)
      commit('setSectionData', payload)
    },
    addNewSectionBP({ commit }) {
      commit('addNewSectionBP')
    },
    deleteSectionBP({ commit }, { tabIndex }) {
      console.log('delete tab number', tabIndex)
      commit('deleteSectionBP', tabIndex)
    },
    setSectionDataBP({ commit }, payload) {
      console.log('userInput', payload)
      commit('setSectionDataBP', payload)
    },
    uploadMainImage({ commit }, payload) {
      commit('uploadMainImage', payload)
    },
    uploadImage({ commit }, payload) {
      commit('uploadImage', payload)
    }
  }
})
