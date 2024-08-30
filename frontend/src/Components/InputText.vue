<script setup>
import { defineProps, defineEmits, computed } from 'vue'

const props = defineProps({
  modelValue: String,
  placeholder: String,
  error: String
})

const emit = defineEmits(['update:modelValue'])

const inputClass = computed(() => {
  let cls = 'input'
  if (props.error !== undefined) {
    cls = `${cls} has-error`
  }
  return cls
})
</script>
<template>
  <input
    type="text"
    :class="inputClass"
    :value="props.modelValue"
    :placeholder="props.placeholder"
    @input="event => {emit('update:modelValue', event.target.value)}"
  >
  <p><small class="error">{{ props.error }}</small></p>
</template>
