import axios from 'axios'

// export function addNewUseCase(useCase) {
//   return axios.post('/api/use-cases', useCase, { withCredentials: true })
// }

export function login(credentials) {
  console.log('API: handle login')
  return axios.post('/token/auth', credentials, { withCredentials: true })
}

export function refreshToken() {
  console.log('API: handle refreshing token')
  return axios.get('/token/refresh', { withCredentials: true })
}

export function register(userData) {
  console.log('API: handle user signup', userData)
  return axios.post('/token/register', userData, { withCredentials: true })
}

export function logout() {
  console.log('API: handle user logout')
  return axios
    .get('/token/remove-refresh', { withCredentials: true })
    .then(response => {
      console.log('API: refresh token revoked', response.data.msg)
      return axios.get('/token/remove', { withCredentials: true })
    })
}
