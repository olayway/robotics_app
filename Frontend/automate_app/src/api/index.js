import $axios from '../plugins/axios'

// AUTH ROUTES
export function login(credentials) {
  console.log('API: signing in')
  return $axios.post('/login', credentials)
}

export function refreshToken() {
  console.log('API: refreshing token')
  return $axios.get('/refresh')
}

export function register(userData) {
  console.log('API: registering new user', userData)
  return $axios.post('/register', userData)
}

export function logout() {
  console.log('API: signing out')
  return $axios.get('/logout')
}

// MAIN APP ROUTES
export function getUseCases(appliedFilters, currentPage = 1) {
  console.log('API: fetching filtered use-cases')
  const url = `/app/use-cases/${currentPage}`
  if (appliedFilters) {
    let params = new URLSearchParams()
    for (const [key, array] of Object.entries(appliedFilters)) {
      if (array) {
        array.forEach(value => params.append(key, value))
      }
    }
    return $axios.get(url, { params: params })
  } else {
    return $axios.get(url)
  }
}

export function getUserUseCases() {
  console.log("API: fetching user's use cases")
  return $axios.get('/profile/use-cases')
}

export function saveUseCase(useCaseData, useCaseId, csrf_access_token) {
  console.log('API: sending useCaseData to the server')
  const useCase = new FormData()
  for (let [key, value] of Object.entries(useCaseData)) {
    if (!['images', 'main_image'].includes(key)) {
      value = JSON.stringify(value)
      useCase.append(key, value)
    } else if (key == 'images' && useCaseData['images'] !== []) {
      for (let i = 0; i < value.length; i++) {
        useCase.append(`image${i}`, value[i])
      }
    } else if (key == 'main_image' && !!useCaseData['main_image']) {
      useCase.append(key, value)
    }
  }
  if (!useCaseId) {
    return $axios.put('/profile/use-cases', useCase, {
      headers: {
        'X-CSRF-TOKEN': csrf_access_token
      }
    })
  } else {
    return $axios.post(`/profile/use-cases/${useCaseId}`, useCase, {
      headers: {
        'X-CSRF-TOKEN': csrf_access_token
      }
    })
  }
}

export function deleteUseCase(useCaseId, csrf_access_token) {
  console.log(`API: deleting use case no ${useCaseId}`)
  return $axios.delete('/profile/use-cases', {
    headers: {
      'X-CSRF-TOKEN': csrf_access_token
    },
    data: { use_case_id: useCaseId }
  })
}

export function fetchUseCase(useCaseId) {
  console.log('API: fetching use case data from DB')
  return $axios.get(`/use-case/${useCaseId}`)
}

export function changeCaseStatus(case_id, status, csrf_access_token) {
  console.log('API: changing use case status')
  return $axios.post(
    `/profile/use-cases/${case_id}`,
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
  return $axios.get(`/profile/use-cases/${useCaseId}`)
}
