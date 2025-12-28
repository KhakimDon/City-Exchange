import { defineStore } from 'pinia'
import WebApp from '@twa-dev/sdk'

export const useTelegramStore = defineStore('telegram', {
  state: () => ({
    isReady: false,
    user: WebApp.initDataUnsafe?.user || null,
    initData: WebApp.initData || '',
    platform: WebApp.platform || 'unknown',
    colorScheme: WebApp.colorScheme || 'light',
    themeParams: WebApp.themeParams || {}
  }),
  getters: {
    isAuthenticated: (state) => !!state.user,
    userId: (state) => state.user?.id || null,
    userName: (state) => {
      if (!state.user) return null
      return state.user.username || `${state.user.first_name} ${state.user.last_name || ''}`.trim()
    }
  },
  actions: {
    init() {
      if (typeof window !== 'undefined' && window.Telegram?.WebApp) {
        WebApp.ready()
        WebApp.expand()
        this.isReady = true
        this.user = WebApp.initDataUnsafe?.user || null
        this.initData = WebApp.initData || ''
        this.platform = WebApp.platform || 'unknown'
        this.colorScheme = WebApp.colorScheme || 'light'
        this.themeParams = WebApp.themeParams || {}
      }
    }
  }
})

