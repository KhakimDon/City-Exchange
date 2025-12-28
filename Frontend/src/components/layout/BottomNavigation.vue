<template>
  <nav class="fixed bottom-0 left-0 right-0 bg-[#1D2024] z-50 pb-4 rounded-t-3xl overflow-hidden border-t border-[#373A3E]">
    <div class="container mx-auto px-4">
      <div class="flex justify-around items-center h-16">
        <router-link
          v-for="item in navigationItems"
          :key="item.name"
          :to="item.name === 'referral' ? '#' : item.path"
          @click.prevent="handleNavigationClick(item)"
          :class="cn(
            'flex flex-col items-center justify-center flex-1 h-full transition-colors relative',
            {
              'text-white': isActive(item.path),
              'text-gray-400 hover:text-gray-300': !isActive(item.path)
            }
          )"
        >
          <!-- SVG паттерн на заднем фоне -->
          <div class="absolute left-0 right-0 -top-5 bottom-0 pointer-events-none overflow-hidden">
            <svg
              class="w-full h-full opacity-30"
              viewBox="0 0 80 80"
              fill="none"
              xmlns="http://www.w3.org/2000/svg"
              preserveAspectRatio="xMidYMid slice"
            >
              <path opacity="0.16" d="M1.25 1.25L78.75 78.75M78.75 1.25L1.25 78.75M27.499 0V80M39.9985 0V80M52.4998 0V80M80 27.5002L0 27.5002M80 39.9996L0 39.9996M80 52.5008L0 52.5008M65 40C65 53.8071 53.8071 65 40 65C26.1929 65 15 53.8071 15 40C15 26.1929 26.1929 15 40 15C53.8071 15 65 26.1929 65 40ZM52.5 40C52.5 46.9036 46.9036 52.5 40 52.5C33.0964 52.5 27.5 46.9036 27.5 40C27.5 33.0964 33.0964 27.5 40 27.5C46.9036 27.5 52.5 33.0964 52.5 40Z" stroke="url(#paint0_radial_pattern)" stroke-width="0.5"/>
              <defs>
                <radialGradient id="paint0_radial_pattern" cx="0" cy="0" r="1" gradientUnits="userSpaceOnUse" gradientTransform="translate(40 40) rotate(90) scale(40)">
                  <stop stop-color="white"/>
                  <stop offset="0.5" stop-color="white" stop-opacity="0.25"/>
                  <stop offset="1" stop-color="white" stop-opacity="0"/>
                </radialGradient>
              </defs>
            </svg>
          </div>
          
          <!-- Иконка: Все заявки -->
          <svg
            v-if="item.icon === 'orders'"
            :class="cn('w-6 h-6 mb-1 relative z-10', {
              'opacity-100': isActive(item.path),
              'opacity-70': !isActive(item.path)
            })"
            viewBox="0 0 24 24"
            fill="none"
            xmlns="http://www.w3.org/2000/svg"
          >
            <path d="M4 17H10M4 12H13M18 11V19M18 19L21 16M18 19L15 16M4 7H16" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
          </svg>
          
          <!-- Иконка: Рефералка -->
          <svg
            v-else-if="item.icon === 'referral'"
            :class="cn('w-6 h-6 mb-1 relative z-10', {
              'opacity-100': isActive(item.path),
              'opacity-70': !isActive(item.path)
            })"
            viewBox="0 0 24 24"
            fill="none"
            xmlns="http://www.w3.org/2000/svg"
          >
            <path d="M3 15.0002V16.8C3 17.9201 3 18.4798 3.21799 18.9076C3.40973 19.2839 3.71547 19.5905 4.0918 19.7822C4.5192 20 5.07899 20 6.19691 20H21.0002M3 15.0002V5M3 15.0002L6.8534 11.7891L6.85658 11.7865C7.55366 11.2056 7.90288 10.9146 8.28154 10.7964C8.72887 10.6567 9.21071 10.6788 9.64355 10.8584C10.0105 11.0106 10.3323 11.3324 10.9758 11.9759L10.9822 11.9823C11.6357 12.6358 11.9633 12.9635 12.3362 13.1153C12.7774 13.2951 13.2685 13.3106 13.7207 13.1606C14.1041 13.0334 14.4542 12.7275 15.1543 12.115L21 7" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
          </svg>
          
          <!-- Иконка: Поддержка -->
          <svg
            v-else-if="item.icon === 'support'"
            :class="cn('w-6 h-6 mb-1 relative z-10', {
              'opacity-100': isActive(item.path),
              'opacity-70': !isActive(item.path)
            })"
            viewBox="0 0 24 24"
            fill="none"
            xmlns="http://www.w3.org/2000/svg"
          >
            <path d="M19 11C19 7.13401 15.866 4 12 4C8.13401 4 5 7.13401 5 11M16 14.5V16.5C16 16.9647 16 17.197 16.0384 17.3902C16.1962 18.1836 16.8165 18.8041 17.6099 18.9619C17.8031 19.0003 18.0353 19.0003 18.5 19.0003C18.9647 19.0003 19.197 19.0003 19.3902 18.9619C20.1836 18.8041 20.8036 18.1836 20.9614 17.3902C20.9999 17.197 21 16.9647 21 16.5V14.5C21 14.0353 20.9999 13.8026 20.9614 13.6094C20.8036 12.816 20.1836 12.1962 19.3902 12.0384C19.197 12 18.9647 12 18.5 12C18.0353 12 17.8031 12 17.6099 12.0384C16.8165 12.1962 16.1962 12.816 16.0384 13.6094C16 13.8026 16 14.0353 16 14.5ZM8 14.5V16.5C8 16.9647 7.99986 17.197 7.96143 17.3902C7.80361 18.1836 7.18352 18.8041 6.39014 18.9619C6.19694 19.0003 5.96469 19.0003 5.50004 19.0003C5.03539 19.0003 4.80306 19.0003 4.60986 18.9619C3.81648 18.8041 3.19624 18.1836 3.03843 17.3902C3 17.197 3 16.9647 3 16.5V14.5C3 14.0353 3 13.8026 3.03843 13.6094C3.19624 12.816 3.81648 12.1962 4.60986 12.0384C4.80306 12 5.03539 12 5.50004 12C5.9647 12 6.19694 12 6.39014 12.0384C7.18352 12.1962 7.80361 12.816 7.96143 13.6094C7.99986 13.8026 8 14.0353 8 14.5Z" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
          </svg>
          
          <!-- Иконка: О нас -->
          <svg
            v-else-if="item.icon === 'about'"
            :class="cn('w-6 h-6 mb-1 relative z-10', {
              'opacity-100': isActive(item.path),
              'opacity-70': !isActive(item.path)
            })"
            viewBox="0 0 24 24"
            fill="none"
            xmlns="http://www.w3.org/2000/svg"
          >
            <path d="M6.89761 18.1618C8.28247 19.3099 10.0607 20 12.0001 20C16.4184 20 20.0001 16.4183 20.0001 12C20.0001 11.431 19.9407 10.8758 19.8278 10.3404M6.89761 18.1618C5.12756 16.6944 4.00014 14.4789 4.00014 12C4.00014 7.58172 7.58186 4 12.0001 4C15.8494 4 19.0637 6.71853 19.8278 10.3404M6.89761 18.1618C8.85314 17.7147 11.1796 16.7828 13.526 15.4281C16.2564 13.8517 18.4773 12.0125 19.8278 10.3404M6.89761 18.1618C4.46844 18.7171 2.61159 18.5243 1.99965 17.4644C1.36934 16.3726 2.19631 14.5969 3.99999 12.709M19.8278 10.3404C21.0796 8.79041 21.5836 7.38405 21.0522 6.46374C20.5134 5.53051 19.0095 5.26939 16.9997 5.59929" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
          </svg>
          
          <span class="text-xs font-medium relative z-10">{{ item.label }}</span>
        </router-link>
      </div>
    </div>
  </nav>

  <!-- Referral Development Bottom Sheet -->
  <Transition name="drawer">
    <div v-if="showReferralSheet" class="fixed inset-0 z-[60] flex items-end" @click.self="closeReferralSheet">
      <div class="drawer-backdrop absolute inset-0 bg-black/50" @click="closeReferralSheet"></div>
      <div class="drawer-content bg-[#1D2024] rounded-t-3xl w-full max-h-[90vh] overflow-y-auto relative z-10"
        @click.stop>
        <!-- Header -->
        <div class="flex items-center justify-between p-4 border-b border-[#26292D]">
          <h2 class="text-white text-lg font-semibold">Рефералка</h2>
          <button @click="closeReferralSheet" class="text-gray-400 hover:text-white">
            <svg class="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
            </svg>
          </button>
        </div>

        <!-- Content -->
        <div class="p-6">
          <div class="text-white/80 text-base leading-relaxed text-center">
            Пока этот пункт в разработке, сообщим когда будет готово
          </div>
        </div>
      </div>
    </div>
  </Transition>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { cn } from '@/utils/cn'

interface NavigationItem {
  name: string
  path: string
  label: string
  icon: 'orders' | 'referral' | 'support' | 'about'
}

const navigationItems: NavigationItem[] = [
  {
    name: 'orders',
    path: '/orders',
    label: 'Все заявки',
    icon: 'orders'
  },
  {
    name: 'referral',
    path: '/referral',
    label: 'Рефералка',
    icon: 'referral'
  },
  {
    name: 'support',
    path: '/support',
    label: 'Поддержка',
    icon: 'support'
  },
  {
    name: 'about',
    path: '/about',
    label: 'О нас',
    icon: 'about'
  }
]

const route = useRoute()
const router = useRouter()
const showReferralSheet = ref(false)

const isActive = (path: string): boolean => {
  return route.path === path
}

const handleNavigationClick = (item: NavigationItem) => {
  if (item.name === 'referral') {
    showReferralSheet.value = true
  } else {
    router.push(item.path)
  }
}

const closeReferralSheet = () => {
  showReferralSheet.value = false
}
</script>

<style scoped>
/* Drawer animations */
.drawer-enter-active,
.drawer-leave-active {
  transition: opacity 0.3s ease;
}

.drawer-enter-active .drawer-backdrop,
.drawer-leave-active .drawer-backdrop {
  transition: opacity 0.3s ease;
}

.drawer-enter-active .drawer-content,
.drawer-leave-active .drawer-content {
  transition: transform 0.3s ease;
}

.drawer-enter-from,
.drawer-leave-to {
  opacity: 0;
}

.drawer-enter-from .drawer-backdrop,
.drawer-leave-to .drawer-backdrop {
  opacity: 0;
}

.drawer-enter-from .drawer-content,
.drawer-leave-to .drawer-content {
  transform: translateY(100%);
}

.drawer-enter-to .drawer-content,
.drawer-leave-from .drawer-content {
  transform: translateY(0);
}
</style>
