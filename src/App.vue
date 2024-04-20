<script setup>
import { reactive } from 'vue'
const form = reactive({
  link: null
})
const submit = async () => {
  try {
    const response = await fetch(`http://localhost:8000/shorter-url?link=${form.link}`, {
      method: 'GET'
    })
    const data = await response.json()
    console.log(data)
  } catch {
    console.log('error')
  }
}
</script>

<template>
  Shorten Link
  <form @submit.prevent="submit">
    <input
      v-model="form.link"
      type="text"
      placeholder="Insert link"
    />
    <button
      type="submit"
      title="Generate"
    >
      Generate
    </button>
  </form>
</template>
