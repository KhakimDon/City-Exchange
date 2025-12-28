<template>
  <div class="min-h-screen justify-between flex flex-col pb-8" style="font-family: 'Montserrat', sans-serif;">
    <div>
      <!-- Header -->
      <div class="px-4 pt-8">
        <h1 class="text-white text-[24px] font-semibold mb-2">Международные переводы за пару минут.</h1>

        <!-- Cityex24 Badge -->
        <div class="inline-block bg-[#26A17B] rounded-lg px-1 py-0 mb-8">
          <span class="text-black text-[24px] font-semibold">Cityex24</span>
        </div>
      </div>
    </div>
    <div class="overflow-x-hidden flex-1 flex flex-col justify-center">
      <!-- Icons Marquee (Left to Right) -->
      <div class=" mb-[8px] px-4">
        <div class="marquee-left-to-right flex gap-2">
          <!-- First set -->
          <div
            class="w-20 h-20 bg-[#1D2024] rounded-2xl flex items-center justify-center border-t-[#26292D] shadow-inner-block border-r-[#26292D] border-b-[#26292D] border-l-[#26292D] border flex-shrink-0 pattern-bg">
            <svg class="w-8 h-8 text-white" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                d="M12 6V4m0 2a2 2 0 100 4m0-4a2 2 0 110 4m-6 8a2 2 0 100-4m0 4a2 2 0 110-4m0 4v2m0-6V4m6 6v10m6-2a2 2 0 100-4m0 4a2 2 0 110-4m0 4v2m0-6V4" />
            </svg>
          </div>
          <div
            class="w-20 h-20 bg-[#26A17B] btn-shadow rounded-2xl flex items-center justify-center border-t-[#26292D]  border-r-[#26292D] border-b-[#26292D] border-l-[#26292D] border flex-shrink-0 pattern-bg">
            <svg width="30" height="30" viewBox="0 0 30 30" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path
                d="M23.75 8.75V5C23.75 4.66848 23.6183 4.35054 23.3839 4.11612C23.1495 3.8817 22.8315 3.75 22.5 3.75H6.25C5.58696 3.75 4.95107 4.01339 4.48223 4.48223C4.01339 4.95107 3.75 5.58696 3.75 6.25C3.75 6.91304 4.01339 7.54893 4.48223 8.01777C4.95107 8.48661 5.58696 8.75 6.25 8.75H25C25.3315 8.75 25.6495 8.8817 25.8839 9.11612C26.1183 9.35054 26.25 9.66848 26.25 10V15M26.25 15H22.5C21.837 15 21.2011 15.2634 20.7322 15.7322C20.2634 16.2011 20 16.837 20 17.5C20 18.163 20.2634 18.7989 20.7322 19.2678C21.2011 19.7366 21.837 20 22.5 20H26.25C26.5815 20 26.8995 19.8683 27.1339 19.6339C27.3683 19.3995 27.5 19.0815 27.5 18.75V16.25C27.5 15.9185 27.3683 15.6005 27.1339 15.3661C26.8995 15.1317 26.5815 15 26.25 15Z"
                stroke="white" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" />
              <path
                d="M3.75 6.25V23.75C3.75 24.413 4.01339 25.0489 4.48223 25.5178C4.95107 25.9866 5.58696 26.25 6.25 26.25H25C25.3315 26.25 25.6495 26.1183 25.8839 25.8839C26.1183 25.6495 26.25 25.3315 26.25 25V20"
                stroke="white" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" />
            </svg>

          </div>
          <div
            class="w-20 h-20 bg-[#1D2024] rounded-2xl flex items-center justify-center border-t-[#26292D] shadow-inner-block border-r-[#26292D] border-b-[#26292D] border-l-[#26292D] border flex-shrink-0 pattern-bg">
            <svg class="w-8 h-8 text-white" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                d="M3.055 11H5a2 2 0 012 2v1a2 2 0 002 2 2 2 0 012 2v2.945M8 3.935V5.5A2.5 2.5 0 0010.5 8h.5a2 2 0 012 2 2 2 0 104 0 2 2 0 012-2h1.064M15 20.488V18a2 2 0 012-2h3.064M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
            </svg>
          </div>
          <div
            class="w-20 h-20 bg-[#1D2024] rounded-2xl flex items-center justify-center border-t-[#26292D] shadow-inner-block border-r-[#26292D] border-b-[#26292D] border-l-[#26292D] border flex-shrink-0 pattern-bg">
            <svg class="w-8 h-8 text-white" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                d="M3 15a4 4 0 004 4h9a5 5 0 10-.1-9.999 5.002 5.002 0 10-9.78 2.096A4.001 4.001 0 003 15z" />
            </svg>
          </div>
          <!-- Duplicate set for seamless loop -->
          <div
            class="w-20 h-20 bg-[#1D2024] rounded-2xl flex items-center justify-center border-t-[#26292D] shadow-inner-block border-r-[#26292D] border-b-[#26292D] border-l-[#26292D] border flex-shrink-0 pattern-bg">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path
                d="M6.89761 18.1618C8.28247 19.3099 10.0607 20 12.0001 20C16.4184 20 20.0001 16.4183 20.0001 12C20.0001 11.431 19.9407 10.8758 19.8278 10.3404M6.89761 18.1618C5.12756 16.6944 4.00014 14.4789 4.00014 12C4.00014 7.58172 7.58186 4 12.0001 4C15.8494 4 19.0637 6.71853 19.8278 10.3404M6.89761 18.1618C8.85314 17.7147 11.1796 16.7828 13.526 15.4281C16.2564 13.8517 18.4773 12.0125 19.8278 10.3404M6.89761 18.1618C4.46844 18.7171 2.61159 18.5243 1.99965 17.4644C1.36934 16.3726 2.19631 14.5969 3.99999 12.709M19.8278 10.3404C21.0796 8.79041 21.5836 7.38405 21.0522 6.46374C20.5134 5.53051 19.0095 5.26939 16.9997 5.59929"
                stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" />
            </svg>

          </div>
          <div
            class="w-20 h-20 bg-[#1D2024] rounded-2xl flex items-center justify-center border-t-[#26292D] shadow-inner-block border-r-[#26292D] border-b-[#26292D] border-l-[#26292D] border flex-shrink-0 pattern-bg">
            <svg class="w-8 h-8 text-white" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                d="M3 10h18M7 15h1m4 0h1m-7 4h12a3 3 0 003-3V8a3 3 0 00-3-3H6a3 3 0 00-3 3v8a3 3 0 003 3z" />
            </svg>
          </div>
          <div
            class="w-20 h-20 bg-[#1D2024] rounded-2xl flex items-center justify-center border-t-[#26292D] shadow-inner-block border-r-[#26292D] border-b-[#26292D] border-l-[#26292D] border flex-shrink-0 pattern-bg">
            <svg class="w-8 h-8 text-white" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                d="M3.055 11H5a2 2 0 012 2v1a2 2 0 002 2 2 2 0 012 2v2.945M8 3.935V5.5A2.5 2.5 0 0010.5 8h.5a2 2 0 012 2 2 2 0 104 0 2 2 0 012-2h1.064M15 20.488V18a2 2 0 012-2h3.064M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
            </svg>
          </div>
          <div
            class="w-20 h-20 bg-[#1D2024] rounded-2xl flex items-center justify-center border-t-[#26292D] shadow-inner-block border-r-[#26292D] border-b-[#26292D] border-l-[#26292D] border flex-shrink-0 pattern-bg">
            <svg class="w-8 h-8 text-white" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                d="M3 15a4 4 0 004 4h9a5 5 0 10-.1-9.999 5.002 5.002 0 10-9.78 2.096A4.001 4.001 0 003 15z" />
            </svg>
          </div>
        </div>
      </div>

      <!-- Flags Marquee (Right to Left) -->
      <div class="overflow-x-hidden mb-[38px]">
        <div class="marquee-right-to-left flex gap-2">
          <!-- First set -->
          <div
            class="w-20 h-20 bg-[#1D2024] rounded-2xl flex items-center justify-center border-t-[#26292D] shadow-inner-block border-r-[#26292D] border-b-[#26292D] border-l-[#26292D] border flex-shrink-0 pattern-bg">
            <img src="@/assets/flags/image 2.png" alt="Кыргызстан" class="w-[23px] h-[23px] object-contain" />
          </div>
          <div
            class="w-20 h-20 bg-[#1D2024] rounded-2xl flex items-center justify-center border-t-[#26292D] shadow-inner-block border-r-[#26292D] border-b-[#26292D] border-l-[#26292D] border flex-shrink-0 pattern-bg">
            <img src="@/assets/flags/image 3.png" alt="Узбекистан" class="w-[23px] h-[23px] object-contain" />
          </div>
          <div
            class="w-20 h-20 bg-[#1D2024] rounded-2xl flex items-center justify-center border-t-[#26292D] shadow-inner-block border-r-[#26292D] border-b-[#26292D] border-l-[#26292D] border flex-shrink-0 pattern-bg">
            <img src="@/assets/flags/image 5.png" alt="ОАЭ" class="w-[23px] h-[23px] object-contain" />
          </div>
          <div
            class="w-20 h-20 bg-[#1D2024] rounded-2xl flex items-center justify-center border-t-[#26292D] shadow-inner-block border-r-[#26292D] border-b-[#26292D] border-l-[#26292D] border flex-shrink-0 pattern-bg">
            <img src="@/assets/flags/image 4.png" alt="Турция" class="w-[23px] h-[23px] object-contain" />
          </div>
          <div
            class="w-20 h-20 bg-[#1D2024] rounded-2xl flex items-center justify-center border-t-[#26292D] shadow-inner-block border-r-[#26292D] border-b-[#26292D] border-l-[#26292D] border flex-shrink-0 pattern-bg">
            <img src="@/assets/flags/image 6.png" alt="Саудовская Аравия" class="w-[23px] h-[23px] object-contain" />
          </div>
          <!-- Duplicate set for seamless loop -->
          <div
            class="w-20 h-20 bg-[#1D2024] rounded-2xl flex items-center justify-center border-t-[#26292D] shadow-inner-block border-r-[#26292D] border-b-[#26292D] border-l-[#26292D] border flex-shrink-0 pattern-bg">
            <img src="@/assets/flags/image 2.png" alt="Кыргызстан" class="w-[23px] h-[23px] object-contain" />
          </div>
          <div
            class="w-20 h-20 bg-[#1D2024] rounded-2xl flex items-center justify-center border-t-[#26292D] shadow-inner-block border-r-[#26292D] border-b-[#26292D] border-l-[#26292D] border flex-shrink-0 pattern-bg">
            <img src="@/assets/flags/image 3.png" alt="Узбекистан" class="w-[23px] h-[23px] object-contain" />
          </div>
          <div
            class="w-20 h-20 bg-[#1D2024] rounded-2xl flex items-center justify-center border-t-[#26292D] shadow-inner-block border-r-[#26292D] border-b-[#26292D] border-l-[#26292D] border flex-shrink-0 pattern-bg">
            <img src="@/assets/flags/image 5.png" alt="ОАЭ" class="w-[23px] h-[23px] object-contain" />
          </div>
          <div
            class="w-20 h-20 bg-[#1D2024] rounded-2xl flex items-center justify-center border-t-[#26292D] shadow-inner-block border-r-[#26292D] border-b-[#26292D] border-l-[#26292D] border flex-shrink-0 pattern-bg">
            <img src="@/assets/flags/image 4.png" alt="Турция" class="w-[23px] h-[23px] object-contain" />
          </div>
          <div
            class="w-20 h-20 bg-[#1D2024] rounded-2xl flex items-center justify-center border-t-[#26292D] shadow-inner-block border-r-[#26292D] border-b-[#26292D] border-l-[#26292D] border flex-shrink-0 pattern-bg">
            <img src="@/assets/flags/image 6.png" alt="Саудовская Аравия" class="w-[23px] h-[23px] object-contain" />
          </div>
        </div>
      </div>

      <!-- Countries List -->
      <div class="mb-8 max-w-[282px] mx-auto">
        <p class="text-white/60 text-sm text-center">
          Кыргызстан • Узбекистан • Турция • Дубай • Саудовская аравия
        </p>
      </div>
    </div>


    <!-- Bottom Button -->
    <div class="px-4">
      <button @click="openCountryDrawer"
        class="w-full btn-shadow h-14 bg-[#26A17B] rounded-full text-white font-semibold hover:bg-[#228B6D] active:bg-[#1F7A5F] transition-colors">
        Далее
      </button>
    </div>

    <!-- Country Selection Drawer -->
    <Transition name="drawer">
      <div v-if="showCountryDrawer" class="fixed inset-0 z-50 flex items-end" @click.self="closeCountryDrawer">
        <div class="drawer-backdrop absolute inset-0 bg-black/50" @click="closeCountryDrawer"></div>
        <div class="drawer-content bg-[#1D2024] rounded-t-3xl w-full max-h-[90vh] overflow-y-auto relative z-10"
          @click.stop>
          <!-- Header -->
          <div class="flex items-start justify-between pt-[22px] px-4">
            <div class="flex items-center gap-3 flex-1">
              <div>
                <h2 class="text-white text-[24px] font-medium">В какую страну нужно перевести деньги?</h2>
              </div>
            </div>
            <button @click="closeCountryDrawer" class="text-gray-400 hover:text-white">
              <svg class="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="white">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
              </svg>
            </button>
          </div>

          <!-- Content -->
          <div class="p-4">

            <!-- Countries List -->
            <div class="space-y-3 mb-6">
              <button v-for="country in countries" :key="country.code" @click="selectCountry(country.code)" :class="cn(
                'w-full relative flex items-center gap-3 h-[55px] border-[#26292D] border shadow-inner-block px-3 rounded-[16px] transition-colors',
                {
                  'bg-[#26A17B] bg-opacity-20 border border-[#26A17B]': selectedCountry === country.code,
                  'bg-[#1D2024] hover:bg-[#2A2D32]': selectedCountry !== country.code
                }
              )">
                <img :src="getFlagPath(country.flag)" :alt="country.name" class="h-[23px] w-[23px] object-contain" />
                <span class="text-white font-medium flex-1 text-left">{{ country.name }}</span>
                <img src="@/assets/svg/pattern/pattern.svg" alt="arrow-right"
                  class="absolute right-0 size-[55px] top-1/2 -translate-y-1/2">
                <svg v-if="selectedCountry === country.code" width="26" height="15" viewBox="0 0 26 19" fill="none"
                  xmlns="http://www.w3.org/2000/svg">
                  <path d="M24.5 1.5L8.6875 17.5L1.5 10.2273" stroke="#26A17B" stroke-width="3" stroke-linecap="round"
                    stroke-linejoin="round" />
                </svg>

              </button>
            </div>

            <div
              class="mb-6 pl-[12px] pt-[6px] pb-[8px] pr-[6px]  bg-[#26A17B]  border-[#26A17B] border-l-[4px]  bg-opacity-20 rounded-[4px]">
              <div class="flex items-start gap-[10px]">
                <p class="text-white text-[15px] font-[Roboto] opacity-80 leading-relaxed flex-1">
                  По международным переводам работаем с 08:00 до 20:00 по МС
                </p>
                <svg width="12" height="12" viewBox="0 0 12 12" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <path
                    d="M3.06801 7.70898C3.21287 7.33648 2.92566 6.95777 2.57177 6.77201C1.93461 6.43756 1.5 5.76953 1.5 5C1.5 3.89543 2.39543 3 3.5 3C4.60206 3 5.49594 3.89137 5.49999 4.99248C5.5 4.99499 5.50001 4.99749 5.50001 5C5.50001 6.54807 5.22855 7.67136 4.93202 8.43388C4.78422 8.81393 4.63168 9.10051 4.50706 9.30228C4.44482 9.40305 4.38972 9.48239 4.34589 9.54141C4.32399 9.57092 4.30491 9.59534 4.28919 9.6148C4.28287 9.62262 4.26705 9.64137 4.25789 9.65222C4.25564 9.65488 4.25259 9.6585 4.25259 9.6585C3.88891 10.0741 3.25715 10.1163 2.84151 9.75258C2.43082 9.39322 2.38481 8.77213 2.73463 8.35642L2.74007 8.34921C2.75094 8.33458 2.77396 8.3023 2.80547 8.25129C2.86835 8.14949 2.96581 7.97178 3.06801 7.70898Z"
                    fill="#26A17B" />
                  <path d="M4.25968 9.65032L4.25423 9.65663L4.25596 9.65464L4.25968 9.65032Z" fill="#26A17B" />
                  <path
                    d="M8.06801 7.70898C8.21287 7.33648 7.92566 6.95777 7.57177 6.77201C6.93461 6.43756 6.5 5.76953 6.5 5C6.5 3.89543 7.39543 3 8.5 3C9.60206 3 10.4959 3.89137 10.5 4.99248C10.5 4.99499 10.5 4.99749 10.5 5C10.5 6.54807 10.2286 7.67136 9.93202 8.43388C9.78422 8.81393 9.63168 9.10051 9.50706 9.30228C9.44482 9.40305 9.38972 9.48239 9.34589 9.54141C9.32399 9.57092 9.30491 9.59534 9.28919 9.6148C9.28287 9.62262 9.26705 9.64137 9.25789 9.65222C9.25564 9.65488 9.25259 9.6585 9.25259 9.6585C8.88891 10.0741 8.25715 10.1163 7.84151 9.75258C7.43082 9.39322 7.38481 8.77213 7.73463 8.35642L7.74007 8.34921C7.75094 8.33458 7.77396 8.3023 7.80547 8.25129C7.86835 8.14949 7.96581 7.97178 8.06801 7.70898Z"
                    fill="#26A17B" />
                  <path d="M9.25968 9.65032L9.25423 9.65663L9.25596 9.65464L9.25968 9.65032Z" fill="#26A17B" />
                </svg>

              </div>
            </div>

            <!-- Get Consultation Button -->
            <button @click="openPhoneDrawer" :disabled="!selectedCountry" :class="cn(
              'w-full h-14 bg-[#26292D] mb-4  rounded-full text-white font-semibold transition-colors',
              {
                'bg-[#26A17B] hover:bg-[#228B6D] btn-shadow active:bg-[#1F7A5F]': selectedCountry,
                'opacity-50 cursor-not-allowed': !selectedCountry
              }
            )">
              Далее
            </button>
          </div>
        </div>
      </div>
    </Transition>

    <!-- Phone Input Drawer -->
    <Transition name="drawer">
      <div v-if="showPhoneDrawer" class="fixed inset-0 z-[60] flex items-end" @click.self="closePhoneDrawer">
        <div class="drawer-backdrop absolute inset-0 bg-black/50" @click="closePhoneDrawer"></div>
        <div class="drawer-content bg-[#1D2024] rounded-t-3xl w-full max-h-[90vh] overflow-y-auto relative z-10"
          @click.stop>
          <!-- Header -->
          <div class="flex items-center justify-between p-4 border-b border-[#26292D]">
            <h2 class="text-white text-lg font-semibold">Номер для обратной связи</h2>
            <button @click="closePhoneDrawer" class="text-gray-400 hover:text-white">
              <svg class="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
              </svg>
            </button>
          </div>

          <!-- Content -->
          <div class="p-4">
            <div class="w-full relative">
              <label class="block text-[#26A17B] text-sm font-medium">
                Телефон <span class="text-[#26A17B]">*</span>
              </label>
              <div class="relative">
                <div class="absolute left-0 top-0 bottom-0 flex items-center pl-4 pointer-events-none z-10">
                  <span class="text-white/60 text-[22px]">+</span>
                </div>
                <input v-model="phoneNumber" type="tel" placeholder="7 (999) 123-45-67"
                  class="w-full bg-transparent font-normal text-white text-[22px] text-left placeholder:text-gray-500 focus:outline-none py-[14px] pl-8 relative z-0"
                  @input="handlePhoneInput" @blur="validatePhone" maxlength="18" />
                <div :class="cn(
                  'absolute bottom-0 left-[-16px] right-[-16px] h-[1px]',
                  {
                    'bg-red-500': phoneError,
                    'bg-[#8E8E93]/10': !phoneError
                  }
                )"></div>
              </div>
              <p v-if="phoneError" class="mt-2 text-sm text-red-500">{{ phoneError }}</p>
            </div>

            <button @click="submitCityex24Request" :disabled="!isPhoneValid || isSubmitting" :class="cn(
              'w-full h-14 bg-[#26A17B] rounded-full mb-4 text-white font-semibold mt-6 transition-colors',
              {
                'hover:bg-[#228B6D] btn-shadow active:bg-[#1F7A5F]': isPhoneValid && !isSubmitting,
                'opacity-50 bg-[#26292D] cursor-not-allowed': !isPhoneValid || isSubmitting
              }
            )">
              {{ isSubmitting ? 'Отправка...' : 'Получить консультацию' }}
            </button>
          </div>
        </div>
      </div>
    </Transition>

    <!-- Success Modal -->
    <Transition name="modal">
      <div v-if="showSuccessModal" class="fixed inset-0 z-[70] flex items-center justify-center bg-black/50 p-4"
        @click.self="closeSuccessModal">
        <div class="bg-[#1D2024] rounded-2xl p-6 w-full max-w-md relative" @click.stop>
          <!-- Success Icon -->
          <div class="flex justify-center mb-4">
            <img src="@/assets/svg/pattern/created.svg" alt="created" class="!h-[100px]">
          </div>

          <!-- Message -->
          <h2 class="text-white text-xl font-semibold text-center mb-2">Заявка отправлена!</h2>
          <p class="text-white/80 text-sm text-center mb-6">
            Мы свяжемся с вами в ближайшее время для уточнения деталей перевода.
          </p>

          <!-- Button -->
          <button @click="closeSuccessModal"
            class="w-full btn-shadow h-12 bg-[#26A17B] rounded-full text-white font-semibold hover:bg-[#228B6D] transition-colors">
            Понятно
          </button>
        </div>
      </div>
    </Transition>
  </div>
</template>

<script setup lang="ts">
import { ref, computed, onMounted, onBeforeUnmount } from 'vue'
import { useRouter } from 'vue-router'
import WebApp from '@twa-dev/sdk'
import { cn } from '@/utils/cn'
import { apiService } from '@/services/api'
import flag2 from '@/assets/flags/image 2.png'
import flag3 from '@/assets/flags/image 3.png'
import flag4 from '@/assets/flags/image 4.png'
import flag5 from '@/assets/flags/image 5.png'
import flag6 from '@/assets/flags/image 6.png'

const router = useRouter()

// Show Telegram native back button
onMounted(() => {
  if (WebApp.BackButton) {
    WebApp.BackButton.show()
    WebApp.BackButton.onClick(() => {
      if (showPhoneDrawer.value) {
        closePhoneDrawer()
      } else if (showCountryDrawer.value) {
        closeCountryDrawer()
      } else {
        router.push('/')
      }
    })
  }
})

onBeforeUnmount(() => {
  if (WebApp.BackButton) {
    WebApp.BackButton.hide()
    WebApp.BackButton.offClick(() => { })
  }
})

// Drawer states
const showCountryDrawer = ref(false)
const showPhoneDrawer = ref(false)
const showSuccessModal = ref(false)
const selectedCountry = ref<string | null>(null)
const phoneNumber = ref('')
const phoneError = ref('')
const isSubmitting = ref(false)

// Countries data
const countries = [
  { code: 'kyrgyzstan', name: 'Кыргызстан', flag: flag3 },
  { code: 'uzbekistan', name: 'Узбекистан', flag: flag2 },
  { code: 'uae', name: 'ОАЭ', flag: flag5 },
  { code: 'turkey', name: 'Турция', flag: flag4 },
  { code: 'saudi_arabia', name: 'Саудовская Аравия', flag: flag6 },
]

const getFlagPath = (flag: string) => flag

const openCountryDrawer = () => {
  showCountryDrawer.value = true
}

const closeCountryDrawer = () => {
  showCountryDrawer.value = false
  selectedCountry.value = null
}

const selectCountry = (countryCode: string) => {
  selectedCountry.value = countryCode
}

const openPhoneDrawer = () => {
  if (selectedCountry.value) {
    showPhoneDrawer.value = true
  }
}

const closePhoneDrawer = () => {
  showPhoneDrawer.value = false
  phoneNumber.value = ''
  phoneError.value = ''
}

const closeSuccessModal = () => {
  showSuccessModal.value = false
  router.push('/')
}

// Format phone number as user types
const handlePhoneInput = (event: Event) => {
  const input = event.target as HTMLInputElement
  let value = input.value.replace(/\D/g, '') // Remove all non-digits

  // Limit to 11 digits (for Russian numbers)
  if (value.length > 11) {
    value = value.slice(0, 11)
  }

  // Format: 7 (999) 123-45-67
  let formatted = ''
  if (value.length > 0) {
    formatted = value[0]
    if (value.length > 1) {
      formatted += ' (' + value.slice(1, 4)
    }
    if (value.length >= 4) {
      formatted += ') ' + value.slice(4, 7)
    }
    if (value.length >= 7) {
      formatted += '-' + value.slice(7, 9)
    }
    if (value.length >= 9) {
      formatted += '-' + value.slice(9, 11)
    }
  }

  phoneNumber.value = formatted
  // Clear error when user starts typing
  if (phoneError.value) {
    validatePhone()
  }
}

const validatePhone = () => {
  const phone = phoneNumber.value.replace(/\D/g, '') // Get only digits
  if (!phone) {
    phoneError.value = 'Обязательное поле'
  } else if (phone.length < 10) {
    phoneError.value = 'Введите полный номер телефона'
  } else if (phone.length > 11) {
    phoneError.value = 'Неверный формат телефона'
  } else {
    phoneError.value = ''
  }
}

const isPhoneValid = computed(() => {
  const phone = phoneNumber.value.replace(/\D/g, '') // Get only digits
  return phone.length >= 10 && phone.length <= 11 && !phoneError.value
})

const submitCityex24Request = async () => {
  if (!isPhoneValid.value || isSubmitting.value || !selectedCountry.value) return

  validatePhone()
  if (!isPhoneValid.value) return

  isSubmitting.value = true

  try {
    // Get telegram user ID (optional)
    const telegramUserId = WebApp.initDataUnsafe?.user?.id

    // Create request payload - send clean phone number (digits only)
    let cleanPhone = phoneNumber.value.replace(/\D/g, '')
    
    
    // Format phone: if starts with 7, add +, otherwise add +7

    const requestData: Record<string, unknown> = {
      country: selectedCountry.value,
      contact_phone: `+${cleanPhone}`,
    }

    // Add telegram_user_id if available
    if (telegramUserId) {
      requestData.telegram_user_id = telegramUserId
    }

    // Add user name if available
    const user = WebApp.initDataUnsafe?.user
    if (user?.first_name) {
      requestData.contact_first_name = user.first_name
    }
    if (user?.last_name) {
      requestData.contact_last_name = user.last_name
    }

    // Create Cityex24 transfer
    const response = await apiService.post<{ success: boolean; error?: string; transfer_id?: number }>('/api/cityex24/', requestData)

    if (response.data.success) {
      // Close drawers and show success modal
      closePhoneDrawer()
      closeCountryDrawer()
      showSuccessModal.value = true
    } else {
      alert(response.data.error || 'Ошибка при создании заявки')
    }
  } catch (error) {
    console.error('Error creating Cityex24 transfer:', error)
    alert('Ошибка при создании заявки. Попробуйте позже.')
  } finally {
    isSubmitting.value = false
  }
}
</script>

<style scoped>
.marquee-left-to-right {
  animation: marquee-left-to-right 20s linear infinite;
}

.marquee-right-to-left {
  animation: marquee-right-to-left 20s linear infinite;
}

@keyframes marquee-left-to-right {
  0% {
    transform: translateX(0);
  }

  100% {
    transform: translateX(-50%);
  }
}

@keyframes marquee-right-to-left {
  0% {
    transform: translateX(-50%);
  }

  100% {
    transform: translateX(0);
  }
}

.pattern-bg {
  background-image: url('@/assets/svg/pattern/pattern.svg');
  background-repeat: no-repeat;
  background-position: center;
  background-size: 80px 80px;
}

.btn-shadow {
  box-shadow: 0 4px 64px 0 rgba(38, 161, 123, 0.3), 0 4px 128px rgba(38, 161, 123, 0.3);
}

.shadow-inner-block {
  box-shadow: inset 0 1px 0px rgba(255, 255, 255, 0.167);
}

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

/* Modal animations */
.modal-enter-active,
.modal-leave-active {
  transition: opacity 0.3s ease;
}

.modal-enter-active>div,
.modal-leave-active>div {
  transition: transform 0.3s ease, opacity 0.3s ease;
}

.modal-enter-from,
.modal-leave-to {
  opacity: 0;
}

.modal-enter-from>div,
.modal-leave-to>div {
  transform: scale(0.9);
  opacity: 0;
}

.modal-enter-to>div,
.modal-leave-from>div {
  transform: scale(1);
  opacity: 1;
}
</style>
