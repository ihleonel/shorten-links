import { ref } from 'vue'

const useShorten = () => {
  const error = ref(null)
  const data = ref(null)
  const isLoading = ref(false)

  const shortener = async (url, payload) => {
    if (isLoading.value === true) {
      return
    }
    error.value = null
    data.value = null
    isLoading.value = true
    try {
      const response = await fetch(url, {
        method: 'POST',
        body: JSON.stringify(payload),
        headers: {
          'Content-Type': 'application/json'
        }
      })
      const json = await response.json()

      if (response.status === 400) {
        error.value = json.errors
      }
      if (response.status === 201) {
        data.value = json
      }
    } catch (err) {
      console.error(err)
    } finally {
      isLoading.value = false
    }
  }
  return { data, isLoading, error, shortener }
}

export default useShorten
