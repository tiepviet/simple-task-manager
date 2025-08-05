import { defineStore } from 'pinia'
import { ref, computed } from 'vue'
import { authService, type User, type LoginData, type RegisterData } from '@/services/auth'

export const useAuthStore = defineStore('auth', () => {
  const user = ref<User | null>(null)
  const token = ref<string | null>(localStorage.getItem('access_token'))

  const isAuthenticated = computed(() => !!token.value)
  const isAdmin = computed(() => user.value?.is_admin || false)

  const login = async (credentials: LoginData) => {
    try {
      const response = await authService.login(credentials)
      token.value = response.access_token
      localStorage.setItem('access_token', response.access_token)
      
      // Get user info
      const userInfo = await authService.getCurrentUser()
      user.value = userInfo
      localStorage.setItem('user', JSON.stringify(userInfo))
      
      return userInfo
    } catch (error) {
      throw error
    }
  }

  const register = async (userData: RegisterData) => {
    try {
      const newUser = await authService.register(userData)
      return newUser
    } catch (error) {
      throw error
    }
  }

  const logout = () => {
    user.value = null
    token.value = null
    localStorage.removeItem('access_token')
    localStorage.removeItem('user')
  }

  const initializeAuth = async () => {
    if (token.value) {
      try {
        const userInfo = await authService.getCurrentUser()
        user.value = userInfo
      } catch (error) {
        logout()
      }
    }
  }

  return {
    user,
    token,
    isAuthenticated,
    isAdmin,
    login,
    register,
    logout,
    initializeAuth
  }
}) 