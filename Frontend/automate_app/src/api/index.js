import $axios from '../plugins/axios'

export function login(credentials) {
  console.log('API: handle login')
  return $axios.post('/api/login', credentials)
}

export function refreshToken() {
  console.log('API: handle refreshing token')
  return $axios.get('/api/refresh')
}

export function register(userData) {
  console.log('API: handle user signup', userData)
  return $axios.post('/api/register', userData)
}

export function logout() {
  console.log('API: handle user logout')
  // logout & revoke access token
  return $axios.get('/api/profile/logout').then(() => {
    // revoke refresh token
    return $axios.get('/api/refresh/remove')
  })
}

export function getUserUseCases() {
  console.log("API: get user's use cases")
  return $axios.get('/api/profile/use-cases')
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
  return $axios.put('/api/profile/use-cases', useCase, {
    headers: {
      'X-CSRF-TOKEN': csrf_access_token
    }
  })
}

export function deleteUseCase(useCaseId, csrf_access_token) {
  console.log(`API: deleting use case no ${useCaseId}`)
  return $axios.delete('/api/profile/use-cases', {
    headers: {
      'X-CSRF-TOKEN': csrf_access_token
    },
    data: { use_case_id: useCaseId }
  })
}

export function fetchUseCase(useCaseId) {
  console.log('API: fetching use case data from DB')
  return $axios.get(`/api/use-case/${useCaseId}`)
}

export function getUseCases(appliedFilters, currentPage = 1) {
  console.log('API: fetching filtered use-cases')
  console.log('CURRENT PAGE', currentPage)
  console.log('APPLIED FILTERS', appliedFilters)
  var params = new URLSearchParams()
  params.append('page_num', currentPage)
  if (appliedFilters) {
    for (const [key, array] of Object.entries(appliedFilters)) {
      if (array) {
        array.forEach(value => params.append(key, value))
      }
    }
  }
  return $axios.get('/api/main/use-cases', { params: params })
}

export function changeCaseStatus(case_id, status, csrf_access_token) {
  console.log('API: changing use case status')
  return $axios.post(
    `/api/profile/use-cases/${case_id}`,
    { status_update: status },
    {
      headers: {
        'X-CSRF-TOKEN': csrf_access_token
      }
    }
  )
}

export function getUserUseCase(useCaseId) {
  console.log('API: fetching USER use case data from DB')
  return $axios.get(`/api/profile/use-cases/${useCaseId}`)
}
