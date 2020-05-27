import Vue from 'vue'
import Vuex from 'vuex'
// import router from '../router'
import cloneDeep from 'lodash/cloneDeep'

// import { EventBus } from '@/utils'
import createPersistedState from 'vuex-persistedstate'
import userDataStore from './modules/userDataStore'
import appStore from './modules/appStore'
import useCaseStore from './modules/useCaseStore'

Vue.use(Vuex)

export const initialStoreModules = {
  user: userDataStore,
  app: appStore,
  case: useCaseStore
}

export default new Vuex.Store({
  plugins: [
    createPersistedState({
      storage: window.sessionStorage,
      paths: ['app', 'user']
    })
  ],
  modules: cloneDeep(initialStoreModules),
  mutations: {
    resetState(state) {
      console.log('reseting state')
      for (const [key, value] of Object.entries(initialStoreModules)) {
        state[key] = value.state
      }
    },
    resetUseCase(state) {
      console.log('reseting use case data')
      console.log(initialStoreModules.case.state)
      state.case = initialStoreModules.case.state
    }
  }
})
