export default {
  state: {
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
    getNavTiles(state) {
      return state.navTiles
    },
    getDrawerState(state) {
      return state.drawerState
    }
  },
  mutations: {
    setDrawerState(state) {
      state.drawerState = !state.drawerState
    }
  },
  actions: {
    setDrawerState({ commit }) {
      commit('setDrawerState')
    }
  }
}
