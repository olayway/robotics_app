import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    navTiles: [
      { title: 'Home', subtitles: [] },
      { title: 'About', subtitles: [] },
      { title: 'Learn', subtitles: ['Tutorials', 'Articles', 'Courses'] },
      { title: 'Subscribe', subtitles: [] },
      { title: 'Contact', subtitles: [] }
    ],
    drawerState: false
  },
  getters: {
    navTiles(state) {
      return state.navTiles
    },
    drawerState(state) {
      return state.drawerState
    }
  },
  mutations: {
    toggleDrawer(state) {
      state.drawerState = !state.drawerState
    }
  },
  actions: {
    toggleDrawer(context) {
      context.commit('toggleDrawer')
    }
  },
  modules: {}
})
