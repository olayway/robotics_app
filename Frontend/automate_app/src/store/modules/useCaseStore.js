export default {
  state: {
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
    getBasicInfo(state) {
      return state.useCaseData.basic_info
    },
    getContent(state) {
      return state.useCaseData.content
    }
  },
  mutations: {
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
}
