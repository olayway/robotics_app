import axios from 'axios'

// export default {
//   install(Vue) {
//     Vue.prototype.$axios = axios.create({
//       baseURL: 'http://localhost:5000',
//       withCredentials: true
//     })
//   }
// }

const $axios = axios.create({
  baseURL: 'http://localhost:5000',
  withCredentials: true
})

export default $axios
