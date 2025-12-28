<template>
  <div class="min-h-screen pb-8" style="font-family: 'Montserrat', sans-serif;">
    <div class="px-4 pt-6">
      <h1 class="text-white text-2xl font-bold mb-6">Все заявки</h1>

      <!-- Loading State with Shimmer -->
      <div v-if="isLoading" class="space-y-4">
        <div v-for="n in 3" :key="n" class="shimmer-card bg-[#1D2024] rounded-2xl p-4 border border-[#26292D]">
          <div class="space-y-3">
            <div class="flex items-center justify-between">
              <div class="shimmer-line h-6 w-32"></div>
              <div class="shimmer-line h-5 w-20"></div>
            </div>
            <div class="shimmer-line h-4 w-full"></div>
            <div class="shimmer-line h-4 w-3/4"></div>
            <div class="flex items-center gap-2 mt-2">
              <div class="shimmer-line h-4 w-16"></div>
              <div class="shimmer-line h-4 w-24"></div>
            </div>
          </div>
        </div>
      </div>

      <!-- Orders List -->
      <div v-else-if="orders.length > 0" class="space-y-4">
        <div
          v-for="order in orders"
          :key="order.id"
          class="bg-[#1D2024] rounded-2xl p-4 border border-[#26292D]"
        >
          <!-- Header -->
          <div class="flex items-center justify-between mb-3">
            <div class="flex items-center gap-2">
              <span class="text-[#26A17B] font-semibold">#{{ order.id }}</span>
              <span
                :class="cn(
                  'px-2 py-1 rounded text-xs font-medium',
                  {
                    'bg-[#FFBF00] bg-opacity-20 text-[#FFBF00]': order.status === 'pending',
                    'bg-green-500 bg-opacity-20 text-green-400': order.status === 'processed',
                    'bg-red-500 bg-opacity-20 text-red-400': order.status === 'cancelled',
                  }
                )"
              >
                {{ order.status_display }}
              </span>
            </div>
            <span class="text-white/60 text-sm">{{ formatDate(order.created_at) }}</span>
          </div>

          <!-- Order Type -->
          <div class="mb-2">
            <span class="text-white/80 text-sm">Тип: </span>
            <span class="text-white font-medium">{{ order.order_type_display }}</span>
          </div>

          <!-- Amount Info -->
          <div class="space-y-1 mb-3">
            <div class="flex items-center justify-between">
              <span class="text-white/60 text-sm">Сумма:</span>
              <span class="text-white font-medium">
                {{ formatAmount(order.amount) }} {{ order.order_type === 'buy' ? '₽' : 'USDT' }}
              </span>
            </div>
            <div class="flex items-center justify-between">
              <span class="text-white/60 text-sm">К получению:</span>
              <span class="text-[#26A17B] font-semibold">
                {{ formatAmount(order.amount_to_receive) }} {{ order.order_type === 'buy' ? 'USDT' : '₽' }}
              </span>
            </div>
            <div class="flex items-center justify-between">
              <span class="text-white/60 text-sm">Курс:</span>
              <span class="text-white/80 text-sm">{{ formatRate(order.exchange_rate) }}</span>
            </div>
          </div>

          <!-- User Info -->
          <div class="pt-3 border-t border-[#26292D]">
            <div class="text-white/60 text-xs mb-1">Ф.И.О: {{ order.full_name }}</div>
            <div class="text-white/60 text-xs truncate">Кошелек: {{ order.wallet_address }}</div>
          </div>
        </div>
      </div>

      <!-- Empty State -->
      <div v-else class="flex flex-col items-center justify-center py-12">
        <svg class="w-16 h-16 text-white/20 mb-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
            d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
        </svg>
        <p class="text-white/60 text-center">У вас пока нет заявок</p>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, onBeforeUnmount } from 'vue'
import { useRouter } from 'vue-router'
import { apiService } from '@/services/api'
import { cn } from '@/utils/cn'
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

interface Order {
  id: number
  order_type: 'buy' | 'sell'
  order_type_display: string
  amount: string
  exchange_rate: string
  amount_to_receive: string
  full_name: string
  wallet_address: string
  status: 'pending' | 'processed' | 'cancelled'
  status_display: string
  created_at: string
  updated_at: string
}

const orders = ref<Order[]>([])
const isLoading = ref<boolean>(true)

const formatAmount = (amount: string): string => {
  const num = parseFloat(amount)
  if (isNaN(num)) return amount
  return num.toFixed(2).replace('.', ',').replace(/\B(?=(\d{3})+(?!\d))/g, ' ')
}

const formatRate = (rate: string): string => {
  const num = parseFloat(rate)
  if (isNaN(num)) return rate
  return num.toFixed(4).replace('.', ',')
}

const formatDate = (dateString: string): string => {
  const date = new Date(dateString)
  const day = date.getDate().toString().padStart(2, '0')
  const month = (date.getMonth() + 1).toString().padStart(2, '0')
  const year = date.getFullYear()
  const hours = date.getHours().toString().padStart(2, '0')
  const minutes = date.getMinutes().toString().padStart(2, '0')
  return `${day}.${month}.${year} ${hours}:${minutes}`
}

const loadOrders = async () => {
  isLoading.value = true
  try {
    // Get telegram user ID
    const telegramUserId = WebApp.initDataUnsafe?.user?.id

    if (!telegramUserId) {
      console.warn('Telegram user ID not available')
      orders.value = []
      return
    }

    const response = await apiService.get<{ success: boolean; orders: Order[] }>(
      `/api/orders/user/?telegram_user_id=${telegramUserId}`
    )

    if (response.data.success) {
      orders.value = response.data.orders || []
    } else {
      console.error('Error loading orders:', response.data)
      orders.value = []
    }
  } catch (error) {
    console.error('Error loading orders:', error)
    orders.value = []
  } finally {
    isLoading.value = false
  }
}

onMounted(() => {
  loadOrders()
})
</script>

<style scoped>
/* Shimmer effect */
.shimmer-card {
  position: relative;
  overflow: hidden;
}

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
