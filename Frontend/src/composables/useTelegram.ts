import { onMounted } from 'vue'
import WebApp from '@twa-dev/sdk'

export function useTelegram() {
  onMounted(() => {
    WebApp.ready()
    WebApp.expand()
  })

  const close = () => {
    WebApp.close()
  }

  const sendData = (data: string) => {
    WebApp.sendData(data)
  }

  const showAlert = (message: string, callback?: () => void) => {
    WebApp.showAlert(message, callback)
  }

  const showConfirm = (message: string, callback?: (confirmed: boolean) => void) => {
    WebApp.showConfirm(message, callback)
  }

  const showPopup = (params: Parameters<typeof WebApp.showPopup>[0], callback?: Parameters<typeof WebApp.showPopup>[1]) => {
    WebApp.showPopup(params, callback)
  }

  const openLink = (url: string, options?: Parameters<typeof WebApp.openLink>[1]) => {
    WebApp.openLink(url, options)
  }

  const openTelegramLink = (url: string) => {
    WebApp.openTelegramLink(url)
  }

  const openInvoice = (url: string, callback?: (status: string) => void) => {
    WebApp.openInvoice(url, callback)
  }

  return {
    WebApp,
    close,
    sendData,
    showAlert,
    showConfirm,
    showPopup,
    openLink,
    openTelegramLink,
    openInvoice,
    initData: WebApp.initData,
    initDataUnsafe: WebApp.initDataUnsafe,
    version: WebApp.version,
    platform: WebApp.platform,
    colorScheme: WebApp.colorScheme,
    themeParams: WebApp.themeParams,
    isExpanded: WebApp.isExpanded,
    viewportHeight: WebApp.viewportHeight,
    viewportStableHeight: WebApp.viewportStableHeight,
    headerColor: WebApp.headerColor,
    backgroundColor: WebApp.backgroundColor,
    isClosingConfirmationEnabled: WebApp.isClosingConfirmationEnabled,
    BackButton: WebApp.BackButton,
    MainButton: WebApp.MainButton,
    HapticFeedback: WebApp.HapticFeedback,
    CloudStorage: WebApp.CloudStorage,
    BiometricManager: WebApp.BiometricManager
  }
}

