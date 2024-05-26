import { ref } from 'vue'

const useShorten = () => {
  const error = ref(null)
  const isLoading = ref(false)
  const shortener = async (url, payload) => {
    isLoading.value = true
    let data = null
    try {
      const response = await fetch(url, {
        method: 'POST',
        body: JSON.stringify(payload),
        headers: {
          'Content-Type': 'application/json'
        }
      })
      data = await response.json()
    } catch (e) {
      error.value = e
    } finally {
      isLoading.value = false
    }
    return data
  }
  return { shortener, isLoading, error }
}

export default useShorten
