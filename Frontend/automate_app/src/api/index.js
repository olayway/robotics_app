import axios from 'axios'

// export function addNewUseCase(useCase) {
//   return axios.post('/api/use-cases', useCase)
// }

export function login(credentials) {
  console.log('API: handle login')
  return axios.post('/api/login', credentials)
}

export function refreshToken() {
  console.log('API: handle refreshing token')
  return axios.get('/api/refresh')
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
  return axios.get('/api/profile/logout').then(() => {
    // revoke refresh token
    return axios.get('/api/refresh/remove')
  })
}

export function getUserUseCases() {
  console.log("API: get user's use cases")
  return axios.get('/api/profile/use-cases')
}

export function saveUseCase(useCaseData, csrf_access_token) {
  console.log('API: sending useCaseData to the server')
  const useCase = new FormData()
  for (let [key, value] of Object.entries(useCaseData)) {
    if (!['images', 'mainImage'].includes(key)) {
      value = JSON.stringify(value)
      useCase.append(key, value)
    } else if (key == 'images' && useCaseData['images'] !== []) {
      for (let i = 0; i < value.length; i++) {
        useCase.append(`image${i}`, value[i])
      }
    } else if (key == 'mainImage' && !!useCaseData['mainImage']) {
      useCase.append(key, value)
    }
  }
  return axios.post('/api/profile/use-cases', useCase, {
    headers: {
      'X-CSRF-TOKEN': csrf_access_token
    }
  })
}
