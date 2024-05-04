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
  <section class="form">
    <h2>Shorten Link</h2>
    <input
      v-model="form.link"
      type="text"
      placeholder="Insert link"
    />
    <button
      type="submit"
      title="Generate"
      @click.prevent="submit"
    >
      Generate
    </button>
  </section>
</template>
