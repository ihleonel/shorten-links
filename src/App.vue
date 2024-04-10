<script setup>
import { reactive } from 'vue'
const form = reactive({
  link: ''
})
const submit = () => {
  console.log(form.link)
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
