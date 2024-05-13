<script setup>
import { reactive, ref } from 'vue'
const form = reactive({
  link: null
})

const data = ref(null)
const isLoading = ref(false)
const submit = async () => {
  isLoading.value = true
  try {
    const response = await fetch('http://localhost:8000/shorter-url', {
      method: 'POST',
      body: JSON.stringify(form),
      headers: {
        'Content-Type': 'application/json'
      }
    })
    data.value = await response.json()
  } catch {
    console.log('error')
  } finally {
    isLoading.value = false
  }
}
</script>

<template>
  <div class="card">
    <div class="card-body">
      <h1 class="title">Shorten URL</h1>
      <input
        v-model="form.link"
        class="input"
        type="search"
        placeholder="Insert URL"
      />
      <button
        class="submit"
        type="submit"
        title="Shorten"
        @click.prevent="submit"
      >
        Shorten
      </button>
      <div class="result">
        <span v-if="isLoading">
          Shortening ...
        </span>
        <span v-else>
          {{ data?.shorted }}
        </span>
      </div>
    </div>
  </div>

</template>
