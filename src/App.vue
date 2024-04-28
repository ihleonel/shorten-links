<script setup>
import { reactive } from 'vue'
const form = reactive({
  link: null
})
const submit = async () => {
  try {
    const response = await fetch('http://localhost:8000/shorter-url/', {
      method: 'POST',
      body: JSON.stringify(form),
      headers: {
        'Content-Type': 'application/json'
      }
    })
    const data = await response.json()
    console.log(data)
  } catch {
    console.log('error')
  }
}
</script>

<template>
  <h2>Shorten Link</h2>
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
