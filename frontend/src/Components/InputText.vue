<script setup>
const props = defineProps({
  modelValue: String,
  error: Object,
})
const emit = defineEmits(['update:modelValue'])
</script>
<template>
  <input
    class="input"
    type="search"
    placeholder="Insert URL"
    :value="props.modelValue"
    @input="({target}) => emit('update:modelValue', target.value)"
  />
  <small>{{ error?.link }}</small>
</template>
