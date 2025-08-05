import api from './api'

export interface Task {
  id: string
  title: string
  detail?: string
  status: string
  due_date?: string
  priority: number
  owner_id: string
  created_at: string
  updated_at: string
}

export interface TaskCreate {
  title: string
  detail?: string
  due_date?: string
  priority: number
}

export interface TaskUpdate {
  title?: string
  detail?: string
  status?: string
  due_date?: string
  priority?: number
}

export interface TaskStatusUpdate {
  status: string
}

export interface TaskFilters {
  status?: string
  priority?: number
  due_before?: string
}

export const taskService = {
  async getTasks(filters: TaskFilters = {}): Promise<Task[]> {
    const params = new URLSearchParams()
    Object.entries(filters).forEach(([key, value]) => {
      if (value !== undefined) {
        params.append(key, value.toString())
      }
    })
    
    const response = await api.get(`/tasks?${params.toString()}`)
    return response.data
  },

  async getTask(id: string): Promise<Task> {
    const response = await api.get(`/tasks/${id}`)
    return response.data
  },

  async createTask(data: TaskCreate): Promise<Task> {
    const response = await api.post('/tasks', data)
    return response.data
  },

  async updateTask(id: string, data: TaskUpdate): Promise<Task> {
    const response = await api.put(`/tasks/${id}`, data)
    return response.data
  },

  async updateTaskStatus(id: string, status: string): Promise<Task> {
    const response = await api.patch(`/tasks/${id}/status`, { status })
    return response.data
  },

  async deleteTask(id: string): Promise<void> {
    await api.delete(`/tasks/${id}`)
  },

  async getAllTasks(filters: { user_id?: string; status?: string } = {}): Promise<Task[]> {
    const params = new URLSearchParams()
    Object.entries(filters).forEach(([key, value]) => {
      if (value !== undefined) {
        params.append(key, value.toString())
      }
    })
    
    const response = await api.get(`/admin/tasks?${params.toString()}`)
    return response.data
  }
} 