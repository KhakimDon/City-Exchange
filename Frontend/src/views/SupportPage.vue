<template>
  <div class="min-h-screen pb-8" style="font-family: 'Montserrat', sans-serif;">
    <div class="px-4 pt-6">
      <h1 class="text-white text-2xl font-bold mb-6">Поддержка</h1>

      <!-- Loading State -->
      <div v-if="isLoading" class="space-y-4">
        <div class="bg-[#1D2024] rounded-2xl p-4 border border-[#26292D]">
          <div class="space-y-3">
            <div class="shimmer-line h-4 w-full"></div>
            <div class="shimmer-line h-4 w-3/4"></div>
            <div class="shimmer-line h-4 w-5/6"></div>
          </div>
        </div>
      </div>

      <!-- Content -->
      <div v-else class="bg-[#1D2024] rounded-2xl p-4 border border-[#26292D]">
        <div class="text-white/80 text-sm leading-relaxed whitespace-pre-line">
          {{ messageText || 'Сообщение не настроено' }}
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, onBeforeUnmount } from 'vue'
import { useRouter } from 'vue-router'
import { apiService } from '@/services/api'
import WebApp from '@twa-dev/sdk'

const router = useRouter()

// Show Telegram native back button
onMounted(() => {
  if (WebApp.BackButton) {
    WebApp.BackButton.show()
    WebApp.BackButton.onClick(() => {
      router.push('/')
    })
  }
})

onBeforeUnmount(() => {
  if (WebApp.BackButton) {
    WebApp.BackButton.hide()
    WebApp.BackButton.offClick(() => { })
  }
})

const messageText = ref<string>('')
const isLoading = ref<boolean>(true)

const loadMessage = async () => {
  isLoading.value = true
  try {
    const response = await apiService.get<{ success: boolean; text: string }>(
      '/api/bot-message/?message_type=support'
    )

    if (response.data.success) {
      messageText.value = response.data.text || 'Сообщение не настроено'
    } else {
      messageText.value = 'Сообщение не настроено'
    }
  } catch (error) {
    console.error('Error loading message:', error)
    messageText.value = 'Сообщение не настроено'
  } finally {
    isLoading.value = false
  }
}

onMounted(() => {
  loadMessage()
})
</script>

<style scoped>
/* Shimmer effect */
.shimmer-line {
  background: linear-gradient(
    90deg,
    rgba(255, 255, 255, 0.05) 0%,
    rgba(255, 255, 255, 0.1) 50%,
    rgba(255, 255, 255, 0.05) 100%
  );
  background-size: 200% 100%;
  animation: shimmer 1.5s infinite;
  border-radius: 4px;
}

@keyframes shimmer {
  0% {
    background-position: -200% 0;
  }
  100% {
    background-position: 200% 0;
  }
}
</style>

