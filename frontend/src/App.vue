<script setup>
import { reactive, ref } from 'vue'
import useShorten from './Composables/useShorten'
const form = reactive({
  link: null
})

const { shortener, isLoading } = useShorten()

const data = ref(null)
const submit = async () => {
  data.value = await shortener('http://localhost:8000/shorter-url', form)
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
