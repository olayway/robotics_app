import axios from 'axios'

export function addNewUseCase(useCase, jwt) {
  return axios.post('/use-cases', useCase, {
    headers: { Authorization: `Bearer: ${jwt}` }
  })
}

export function authenticate(credentials) {
  return axios.post('/login', credentials)
}

export function register(userData) {
  return axios.post('/register', userData)
}
