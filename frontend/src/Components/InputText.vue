<script setup>
import { defineProps, defineEmits } from 'vue'

const props = defineProps({
  modelValue: String,
  placeholder: String
})
const emit = defineEmits(['update:modelValue'])
</script>
<template>
  <input
    type="text"
    class="input"
    :value="props.modelValue"
    :placeholder="props.placeholder"
    @input="event => {emit('update:modelValue', event.target.value)}"
  >
</template>
