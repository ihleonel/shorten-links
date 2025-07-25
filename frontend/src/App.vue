<script setup>
import { reactive, ref } from 'vue'
import useShorten from './Composables/useShorten'
import InputText from './Components/InputText.vue';

const form = reactive({
  link: null
})

const { data, isLoading, error, shortener } = useShorten()

const submit = () => {
  shortener('http://localhost:8000/shorter-url', form)
}

const copy = () => {
  navigator.clipboard.writeText(data.value.shorted)
}

</script>

<template>
  <h1 class="title">Shorten URL</h1>
  <InputText
    v-model="form.link"
    placeholder="Insert URL"
    :error="error?.link"
  />
  <button
    class="submit"
    type="submit"
    title="Shorten"
    @click.prevent="submit"
  >
    Shorten
  </button>
  <button
    title="Copy"
    @click="copy"
  >
    Copy
  </button>
  <div class="result">
    <span v-if="isLoading">
      Shortening ...
    </span>
    <span v-else>
      {{ data?.shorted }}
    </span>
  </div>
</template>
