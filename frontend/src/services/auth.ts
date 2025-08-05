import api from './api'

export interface LoginData {
  email: string
  password: string
}

export interface RegisterData {
  username: string
  email: string
  password: string
}

export interface User {
  id: string
  username: string
  email: string
  is_admin: boolean
  created_at: string
  updated_at: string
}

export interface AuthResponse {
  access_token: string
  token_type: string
}

export const authService = {
  async login(data: LoginData): Promise<AuthResponse> {
    const response = await api.post('/auth/login', data)
    return response.data
  },

  async register(data: RegisterData): Promise<User> {
    const response = await api.post('/auth/register', data)
    return response.data
  },

  async getCurrentUser(): Promise<User> {
    const response = await api.get('/auth/me')
    return response.data
  },

  async getUsers(): Promise<User[]> {
    const response = await api.get('/admin/users')
    return response.data
  }
} 