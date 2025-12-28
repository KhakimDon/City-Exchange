<template>
  <label class="flex items-start gap-3 cursor-pointer">
    <input
      type="checkbox"
      :checked="modelValue"
      :disabled="disabled"
      class="sr-only"
      @change="$emit('update:modelValue', ($event.target as HTMLInputElement).checked)"
    />
    <div
      :class="cn(
        'w-5 h-5 rounded border-2 flex items-center justify-center flex-shrink-0 transition-colors mt-0.5',
        {
          'bg-[#26A17B] border-[#26A17B]': modelValue,
          'bg-transparent border-gray-600': !modelValue,
          'opacity-50 cursor-not-allowed': disabled
        }
      )"
    >
      <svg
        v-if="modelValue"
        class="w-3 h-3 text-white"
        fill="none"
        viewBox="0 0 24 24"
        stroke="currentColor"
      >
        <path
          stroke-linecap="round"
          stroke-linejoin="round"
          stroke-width="3"
          d="M5 13l4 4L19 7"
        />
      </svg>
    </div>
    <span class="text-white text-sm leading-tight">
      <slot />
    </span>
  </label>
</template>

<script setup lang="ts">
import { cn } from '@/utils/cn'

interface Props {
  modelValue: boolean
  disabled?: boolean
}

withDefaults(defineProps<Props>(), {
  disabled: false
})

defineEmits<{
  'update:modelValue': [value: boolean]
}>()
</script>

