<script setup>
import { defineProps, defineEmits } from 'vue'

const props = defineProps({
  modelValue: String
})
const emit = defineEmits(['update:modelValue'])
</script>
<template>
  <input
    type="text"
    :value="props.modelValue"
    @input="event => {emit('update:modelValue', event.target.value)}"
  >
</template>
