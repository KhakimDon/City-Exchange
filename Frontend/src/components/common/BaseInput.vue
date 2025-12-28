<template>
  <div class="w-full relative">
    <label v-if="label" class="block text-[#26A17B] text-sm font-medium">
      {{ label }}
      <span v-if="required" class="text-[#26A17B]">*</span>
    </label>
    <div class="relative">
      <input
        :type="type"
        :value="modelValue"
        :placeholder="placeholder"
        :disabled="disabled"
        :class="cn(
          'w-full bg-transparent font-normal text-white text-[22px] text-left placeholder:text-gray-500 focus:outline-none py-[14px]',
          {
            'opacity-50 cursor-not-allowed': disabled
          }
        )"
        @input="$emit('update:modelValue', ($event.target as HTMLInputElement).value)"
        @blur="$emit('blur', $event)"
      />
    </div>
    <p v-if="error" class="pb-2 text-sm text-red-500">{{ error }}</p>
    <div v-if="line" class="absolute bottom-[0px] left-[-16px] right-[-16px] h-[1px] bg-[#8E8E93]/10"></div>
  </div>

</template>

<script setup lang="ts">
import { cn } from '@/utils/cn'

interface Props {
  modelValue: string | number
  label?: string
  placeholder?: string
  type?: string
  required?: boolean
  disabled?: boolean
  error?: string
  line?: boolean
}

withDefaults(defineProps<Props>(), {
  type: 'text',
  required: false,
  disabled: false,
  line: true
})

defineEmits<{
  'update:modelValue': [value: string | number]
  blur: [event: FocusEvent]
}>()
</script>

