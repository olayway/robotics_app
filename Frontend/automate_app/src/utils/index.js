import Vue from 'vue'

export const EventBus = new Vue()

export function isValidJWT(jwt) {
  if (!jwt || jwt.split('.').length < 3) {
    return false
  }
  console.log('before json parse', jwt)
  const data = JSON.parse(atob(jwt.split('.')[1]))
  console.log('after json parse', data)
  const exp = new Date(data.exp * 1000)
  const now = new Date()
  return now < exp
}
