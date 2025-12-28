<template>
  <div class="pt-10">
    <!-- Welcome Block -->
     <img src="@/assets/svg/pattern/pattern.svg" alt="pattern" class="absolute h-[133px] w-[133px] top-[2px] right-2" />
    <div class="relative bgpattern px-[26px] flex overflow-hidden">
      <!-- Content -->
        <!-- Text Content -->
        <div class="flex-1 pr-4 z-10">
          <h1 class="text-[26px] font-bold text-white mb-0.5" style="font-family: 'Montserrat', sans-serif;">
            City Exchange
          </h1>
          <p class="text-[12px] text-[#ACADAF]  leading-tight" style="font-family: 'Roboto', sans-serif;">
            Добро пожаловать в City Exchange. Выберите одну из услуг, чтобы продолжить
          </p>
        </div>
        
        <!-- Tether Icon -->
        <div class="flex-shrink-0 mr-5 z-10">
          <svg width="56" height="56" viewBox="0 0 56 56" fill="none" xmlns="http://www.w3.org/2000/svg">
            <g clip-path="url(#clip0_63_16441)">
              <path d="M28 56C12.536 56 0 43.464 0 28C0 12.536 12.536 0 28 0C43.464 0 56 12.536 56 28C56 43.464 43.464 56 28 56Z" fill="#26A17B"/>
              <path fill-rule="evenodd" clip-rule="evenodd" d="M24.6365 30.4203V30.4169C24.829 30.4309 25.8212 30.4903 28.035 30.4903C29.8025 30.4903 31.0467 30.4379 31.4842 30.4169V30.4221C38.2882 30.1229 43.3667 28.9381 43.3667 27.5206C43.3667 26.1048 38.2882 24.9201 31.4842 24.6156V29.2426C31.0397 29.2741 29.7657 29.3493 28.0052 29.3493C25.893 29.3493 24.8342 29.2619 24.6365 29.2444V24.6191C17.8465 24.9218 12.7802 26.1066 12.7802 27.5206C12.7802 28.9381 17.8465 30.1193 24.6365 30.4203ZM24.6365 24.1379V19.9974H15.162V13.6833H40.9587V19.9974H31.4842V24.1361C39.1842 24.4896 44.975 26.0156 44.975 27.8426C44.975 29.6696 39.1842 31.1938 31.4842 31.5491V44.8176H24.6365V31.5456C16.9487 31.1921 11.172 29.6678 11.172 27.8426C11.172 26.0173 16.9487 24.4931 24.6365 24.1379Z" fill="white"/>
            </g>
            <defs>
              <clipPath id="clip0_63_16441">
                <rect width="56" height="56" fill="white" transform="matrix(-1 0 0 1 56 0)"/>
              </clipPath>
            </defs>
          </svg>
        </div>
    </div>
    
    <!-- Exchange Rates Block -->
    <div class="mt-10">
      <div class="flex gap-4">
        <!-- Buy Column -->
        <div class="flex-1 flex flex-col items-center justify-center">
          <div class="text-white text-base">Купить</div>
          <div class="rate-container">
            <Transition name="rate-fade" mode="out-in">
              <div v-if="isLoadingRates" key="loading" class="shimmer-rate text-[32px] font-semibold" style="font-family: -apple-system, 'SF Pro Rounded', system-ui, sans-serif;">
                <span class="shimmer-text">00,00</span>
              </div>
              <div v-else key="rate" class="text-[#26A17B] text-[32px] font-semibold rate-shadow" style="font-family: -apple-system, 'SF Pro Rounded', system-ui, sans-serif;">
                {{ buyRate || '—' }}
              </div>
            </Transition>
          </div>
          <div class="text-[#707579] w-[max-content] text-[17px]">за 1 USDT</div>
        </div>
        
        <!-- Sell Column -->
        <div class="flex-1  flex flex-col items-center justify-center">
          <div class="text-white text-base">Продать</div>
          <div class="rate-container">
            <Transition name="rate-fade" mode="out-in">
              <div v-if="isLoadingRates" key="loading" class="shimmer-rate text-[32px] font-semibold" style="font-family: -apple-system, 'SF Pro Rounded', system-ui, sans-serif;">
                <span class="shimmer-text">00,00</span>
              </div>
              <div v-else key="rate" class="text-[#26A17B] text-[32px] font-semibold rate-shadow" style="font-family: -apple-system, 'SF Pro Rounded', system-ui, sans-serif;">
                {{ sellRate || '—' }}
              </div>
            </Transition>
          </div>
          <div class="text-[#707579] w-[max-content] text-[17px]">за 1 USDT</div>
        </div>
      </div>
    </div>
    
    <!-- Service Blocks -->
    <div class="mt-6 space-y-4">
      <!-- Buy/Sell USDT Block -->
      <router-link to="/buy-sell" class="service-block block">
        <div class="circle"></div>
        <div class="flex items-center justify-between h-full">
          <div class="">
            <h3 class="text-white text-lg font-bold mb-1" style="font-family: 'Montserrat', sans-serif;">Купить/Продать USDT</h3>
            <p class="text-gray-400 text-sm">Оформление заявки на покупку USDT</p>
          </div>
          <div class="-mr-8">
            <img src="@/assets/svg/blocks/купить продать.svg" alt="Buy/Sell" class="w-[140px] h-[115px]" />
          </div>
        </div>
      </router-link>
      
      <!-- AML Check Block -->
      <div class="service-block">
        <div class="circle"></div>
        <div class="flex items-center justify-between h-full">
          <div class="">
            <h3 class="text-white text-lg font-bold mb-1" style="font-family: 'Montserrat', sans-serif;">AML Проверка</h3>
            <p class="text-gray-400 text-sm">Проверка прозрачности вашего кошелька</p>
          </div>
          <div class="-mr-8">
            <img src="@/assets/svg/blocks/aml.svg" alt="AML" class="w-[140px] h-[115px]" />
          </div>
        </div>
      </div>
      
      <!-- Cityex24 Block -->
      <router-link to="/cityex24" class="service-block block">
        <div class="circle"></div>
        <div class="flex items-center justify-between h-full">
          <div class="">
            <h3 class="text-white text-lg font-bold mb-1" style="font-family: 'Montserrat', sans-serif;">Cityex24</h3>
            <p class="text-gray-400 text-sm">Совершай международные платежи с Cityex24</p>
          </div>
          <div class="-mr-8">
            <img src="@/assets/svg/blocks/cityex24.svg" alt="Cityex24" class="w-[140px] h-[115px]" />
          </div>
        </div>
      </router-link>
      <div class="h-[20px]"></div>
    </div>
    
    <!-- Rest of content -->
    <div class="container mx-auto px-4">
      <div class="grid gap-6">
        <!-- Content here -->
      </div>
    </div>
  </div>
</template>

<style>
.rate-shadow {
  text-shadow: 
    0px 0px 18px rgba(38, 161, 123, 0.3),
    0px 0px 60px rgba(38, 161, 123, 1);
}

/* Shimmer effect for loading rates */
.shimmer-rate {
  width: 100px;
  height: 48px;
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
}

.shimmer-text {
  color: #26A17B;
  opacity: 0.4;
  position: relative;
  overflow: hidden;
}

.shimmer-text::after {
  content: '';
  position: absolute;
  top: 0;
  left: -100%;
  width: 100%;
  height: 100%;
  background: linear-gradient(
    90deg,
    transparent,
    rgba(255, 255, 255, 0.4),
    transparent
  );
  animation: shimmer 1.5s infinite;
}

@keyframes shimmer {
  0% {
    left: -100%;
  }
  100% {
    left: 100%;
  }
}

/* Rate container with fixed height to prevent layout shift */
.rate-container {
  min-height: 40px;
  display: flex;
  align-items: center;
  justify-content: center;
}

/* Smooth fade transition for rate loading */
.rate-fade-enter-active,
.rate-fade-leave-active {
  transition: opacity 0.4s ease, transform 0.4s ease;
}

.rate-fade-enter-from {
  opacity: 0;
  transform: translateY(-10px);
}

.rate-fade-leave-to {
  opacity: 0;
  transform: translateY(10px);
}

.service-block {
  position: relative;
  height: 120px;
  margin-left: 18px;
  margin-right: 18px;
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 22px;
  overflow: hidden;
  padding: 20px;
  background-color: #1D2024;
}
.circle {
  width: 128px;
  height: 128px;
  border-radius: 50%;
  left: 10px;
  filter: blur(100px);
  top: 50%;
  transform: translateY(-50%);
  position: absolute;
  background-color:rgba(38, 161, 122, 0.62);
}
</style>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { apiService } from '@/services/api'

const buyRate = ref<string>('')
const sellRate = ref<string>('')
const isLoadingRates = ref<boolean>(true)

// Format rate with comma as decimal separator
const formatRate = (rate: string | number): string => {
  if (!rate) return ''
  const num = typeof rate === 'string' ? parseFloat(rate) : rate
  if (isNaN(num)) return ''
  return num.toFixed(2).replace('.', ',') + '₽'
}

// Load exchange rates from backend
const loadExchangeRates = async () => {
  isLoadingRates.value = true
  try {
    const response = await apiService.get<{ success: boolean; rates: Array<{ currency_from: string; currency_to: string; rate: string }> }>('/api/exchange-rates/')
    if (response.data.success && response.data.rates) {
      // Find buy rate: RUB -> USDT (сколько RUB нужно заплатить за 1 USDT)
      const buyRateObj = response.data.rates.find(r => 
        r.currency_from === 'Руб' && r.currency_to === 'USDT'
      )
      // Find sell rate: USDT -> RUB (сколько RUB получишь за 1 USDT)
      const sellRateObj = response.data.rates.find(r => 
        r.currency_from === 'USDT' && r.currency_to === 'Руб'
      )
      
      // If not found in direct direction, try reverse and invert
      if (!buyRateObj) {
        const reverseBuy = response.data.rates.find(r => 
          r.currency_from === 'USDT' && r.currency_to === 'Руб'
        )
        if (reverseBuy) {
          // Invert: if USDT -> RUB rate is X, then RUB -> USDT is 1/X
          buyRate.value = formatRate(1 / parseFloat(reverseBuy.rate))
        }
      } else {
        buyRate.value = formatRate(buyRateObj.rate)
      }
      
      if (!sellRateObj) {
        const reverseSell = response.data.rates.find(r => 
          r.currency_from === 'RUB' && r.currency_to === 'USDT'
        )
        if (reverseSell) {
          // Invert: if RUB -> USDT rate is X, then USDT -> RUB is 1/X
          sellRate.value = formatRate(1 / parseFloat(reverseSell.rate))
        }
      } else {
        sellRate.value = formatRate(sellRateObj.rate)
      }
    }
  } catch (error) {
    console.error('Error loading exchange rates:', error)
    // Keep default values or show error
  } finally {
    isLoadingRates.value = false
  }
}

onMounted(() => {
  loadExchangeRates()
})
</script>
