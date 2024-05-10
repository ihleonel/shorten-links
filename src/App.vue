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
  <div class="card">
    <div class="card-body">
      <h1 class="title">Shorten Link</h1>
      <input
        v-model="form.link"
        class="input"
        type="text"
        placeholder="Insert link"
      />
      <button
        class="submit"
        type="submit"
        title="Generate"
        @click.prevent="submit"
      >
        Generate
      </button>
    </div>
  </div>

</template>
