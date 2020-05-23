export default {
  state: {
    navTiles: [
      { title: 'Home', subtitles: [], path: '/' },
      { title: 'Why Automate', subtitles: [] },
      // {
      //   title: 'Learn',
      //   subtitles: ['Tutorials', 'Articles', 'Courses']
      // },
      // { title: 'Subscribe', subtitles: [] },
      { title: 'Contact', subtitles: [] }
    ]
  },
  getters: {
    getNavTiles(state) {
      return state.navTiles
    }
  },
  mutations: {},
  actions: {}
}
