<template>
  <div class="min-h-screen flex items-center justify-center bg-gradient-to-br from-primary-50 to-blue-50 py-12 px-4 sm:px-6 lg:px-8">
    <div class="max-w-md w-full space-y-8">
      <!-- Header -->
      <div class="text-center">
        <div class="mx-auto h-12 w-12 flex items-center justify-center rounded-full bg-primary-100">
          <svg class="h-8 w-8 text-primary-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M18 9v3m0 0v3m0-3h3m-3 0h-3m-2-5a4 4 0 11-8 0 4 4 0 018 0zM3 20a6 6 0 0112 0v1H3v-1z"></path>
          </svg>
        </div>
        <h2 class="mt-6 text-3xl font-extrabold text-gray-900">
          Create your account
        </h2>
        <p class="mt-2 text-sm text-gray-600">
          Or
          <router-link to="/login" class="font-medium text-primary-600 hover:text-primary-500">
            sign in to your existing account
          </router-link>
        </p>
      </div>

      <!-- Error Alert -->
      <div v-if="error" class="alert alert-error animate-fade-in">
        <div class="flex">
          <svg class="w-5 h-5 text-red-400 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path>
          </svg>
          {{ error }}
        </div>
      </div>

      <!-- Register Form -->
      <form @submit.prevent="handleRegister" class="mt-8 space-y-6">
        <div class="space-y-4">
          <div>
            <label for="username" class="form-label">Username</label>
            <input
              id="username"
              v-model="form.username"
              type="text"
              class="form-input"
              required
              placeholder="Enter your username"
            />
          </div>
          
          <div>
            <label for="email" class="form-label">Email address</label>
            <input
              id="email"
              v-model="form.email"
              type="email"
              class="form-input"
              required
              placeholder="Enter your email"
            />
          </div>
          
          <div>
            <label for="password" class="form-label">Password</label>
            <input
              id="password"
              v-model="form.password"
              type="password"
              class="form-input"
              required
              placeholder="Enter your password"
              minlength="6"
            />
            <p class="mt-1 text-xs text-gray-500">Must be at least 6 characters long</p>
          </div>
        </div>

        <div>
          <button 
            type="submit" 
            class="group relative w-full flex justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-primary-600 hover:bg-primary-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-primary-500 disabled:opacity-50 disabled:cursor-not-allowed transition-colors duration-200"
            :disabled="loading"
          >
            <span v-if="loading" class="absolute left-0 inset-y-0 flex items-center pl-3">
              <svg class="animate-spin h-5 w-5 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
                <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
              </svg>
            </span>
            <span v-else class="absolute left-0 inset-y-0 flex items-center pl-3">
              <svg class="h-5 w-5 text-primary-500 group-hover:text-primary-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M18 9v3m0 0v3m0-3h3m-3 0h-3m-2-5a4 4 0 11-8 0 4 4 0 018 0zM3 20a6 6 0 0112 0v1H3v-1z"></path>
              </svg>
            </span>
            {{ loading ? 'Creating account...' : 'Create account' }}
          </button>
        </div>
      </form>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, reactive } from 'vue'
import { useRouter } from 'vue-router'
import { useAuthStore } from '@/stores/auth'

const router = useRouter()
const authStore = useAuthStore()

const loading = ref(false)
const error = ref('')

const form = reactive({
  username: '',
  email: '',
  password: ''
})

const handleRegister = async () => {
  loading.value = true
  error.value = ''
  
  try {
    await authStore.register(form)
    // After successful registration, redirect to login
    router.push('/login')
  } catch (err) {
    error.value = err instanceof Error ? err.message : 'Registration failed'
  } finally {
    loading.value = false
  }
}
</script> 