import axios from 'axios'

// export function addNewUseCase(useCase) {
//   return axios.post('/api/use-cases', useCase, { withCredentials: true })
// }

export function login(credentials) {
  console.log('API: handle login')
  return axios.post('/api/login', credentials, { withCredentials: true })
}

export function refreshToken() {
  console.log('API: handle refreshing token')
  return axios.get('/api/refresh', { withCredentials: true })
}

export function register(userData) {
  console.log('API: handle user signup', userData)
  return axios.post('/api/register', userData, {
    withCredentials: true
  })
}

export function logout() {
  console.log('API: handle user logout')
  // logout & revoke access token
  return axios
    .get('/api/profile/logout', { withCredentials: true })
    .then(() => {
      // revoke refresh token
      return axios.get('/api/refresh/remove', { withCredentials: true })
    })
}

export function getUserUseCases() {
  console.log("API: get user's use cases")
  return axios.get('/api/profile/use-cases', { withCredentials: true })
}
