<template>
  <div class="min-h-screen bg-[#181B20]" :class="{ 'pb-16': shouldShowBottomNav }">
    <AppHeader v-if="shouldShowHeader" />
    <router-view />
    <BottomNavigation v-if="shouldShowBottomNav" />
  </div>
</template>

<script setup lang="ts">
import { computed } from 'vue'
import { useRoute } from 'vue-router'
import BottomNavigation from './BottomNavigation.vue'
import AppHeader from './AppHeader.vue'

interface Props {
  showBottomNav?: boolean
}

const props = withDefaults(defineProps<Props>(), {
  showBottomNav: true
})

const route = useRoute()

const shouldShowBottomNav = computed(() => {
  if (!props.showBottomNav) return false
  // Hide bottom nav on specific pages if needed
  const hideNavRoutes = ['/aml', '/cityex24', '/buy-sell', '/orders']
  return !hideNavRoutes.includes(route.path)
})

const shouldShowHeader = computed(() => {
  // Hide header on specific pages
  const hideHeaderRoutes = ['/cityex24', '/orders']
  return !hideHeaderRoutes.includes(route.path)
})
</script>

