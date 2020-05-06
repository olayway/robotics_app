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
    drawerState: false,
    useCaseData: {
      filter_tags: {
        company: '',
        applications: [],
        industry: '',
        country: '',
        company_size: ''
      },
      content: {
        article_title: '',
        // TODO update scraper -> Array<{title: String, content: String}>
        article_sections: [{ title: '', content: '' }],
        // TODO update scraper -> Array<{title: String, content: String}>
        bullet_points: [{ title: '', content: ['', '', ''] }]
      },
      images: []
    }
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
    },
    getBasicInfo(state) {
      return state.useCaseData.filter_tags
    },
    getContent(state) {
      return state.useCaseData.content
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
    },
    setBasicInfo(state, payload) {
      const useCaseData = state.useCaseData
      Object.assign(useCaseData, {
        filter_tags: { ...useCaseData.filter_tags, ...payload }
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
    }
  }
})
