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
    ]
  },
  getters: {
    navTiles(state) {
      return state.navTiles
    }
  },
  mutations: {},
  actions: {},
  modules: {}
})
