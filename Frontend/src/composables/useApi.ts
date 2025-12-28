import { ref, type Ref } from 'vue'
import type { ApiResponse } from '@/types'

export function useApi<T>() {
  const data: Ref<T | null> = ref(null)
  const loading = ref(false)
  const error: Ref<string | null> = ref(null)

  const execute = async (apiCall: () => Promise<ApiResponse<T>>) => {
    loading.value = true
    error.value = null
    try {
      const response = await apiCall()
      data.value = response.data
      return response
    } catch (err) {
      error.value = err instanceof Error ? err.message : 'An error occurred'
      throw err
    } finally {
      loading.value = false
    }
  }

  return {
    data,
    loading,
    error,
    execute
  }
}

