import { defineStore } from 'pinia'
import { ref, computed } from 'vue'
import { taskService, type Task, type TaskCreate, type TaskUpdate, type TaskFilters } from '@/services/tasks'

export const useTaskStore = defineStore('tasks', () => {
  const tasks = ref<Task[]>([])
  const loading = ref(false)
  const error = ref<string | null>(null)

  const todoTasks = computed(() => tasks.value.filter(task => task.status === 'todo'))
  const doneTasks = computed(() => tasks.value.filter(task => task.status === 'done'))

  const fetchTasks = async (filters: TaskFilters = {}) => {
    loading.value = true
    error.value = null
    try {
      const fetchedTasks = await taskService.getTasks(filters)
      tasks.value = fetchedTasks
    } catch (err) {
      error.value = err instanceof Error ? err.message : 'Failed to fetch tasks'
    } finally {
      loading.value = false
    }
  }

  const createTask = async (taskData: TaskCreate) => {
    loading.value = true
    error.value = null
    try {
      const newTask = await taskService.createTask(taskData)
      tasks.value.push(newTask)
      return newTask
    } catch (err) {
      error.value = err instanceof Error ? err.message : 'Failed to create task'
      throw err
    } finally {
      loading.value = false
    }
  }

  const updateTask = async (id: string, taskData: TaskUpdate) => {
    loading.value = true
    error.value = null
    try {
      const updatedTask = await taskService.updateTask(id, taskData)
      const index = tasks.value.findIndex(task => task.id === id)
      if (index !== -1) {
        tasks.value[index] = updatedTask
      }
      return updatedTask
    } catch (err) {
      error.value = err instanceof Error ? err.message : 'Failed to update task'
      throw err
    } finally {
      loading.value = false
    }
  }

  const toggleTaskStatus = async (id: string) => {
    const task = tasks.value.find(t => t.id === id)
    if (!task) return

    const newStatus = task.status === 'todo' ? 'done' : 'todo'
    try {
      const updatedTask = await taskService.updateTaskStatus(id, newStatus)
      const index = tasks.value.findIndex(t => t.id === id)
      if (index !== -1) {
        tasks.value[index] = updatedTask
      }
    } catch (err) {
      error.value = err instanceof Error ? err.message : 'Failed to update task status'
    }
  }

  const deleteTask = async (id: string) => {
    loading.value = true
    error.value = null
    try {
      await taskService.deleteTask(id)
      tasks.value = tasks.value.filter(task => task.id !== id)
    } catch (err) {
      error.value = err instanceof Error ? err.message : 'Failed to delete task'
      throw err
    } finally {
      loading.value = false
    }
  }

  const clearError = () => {
    error.value = null
  }

  return {
    tasks,
    loading,
    error,
    todoTasks,
    doneTasks,
    fetchTasks,
    createTask,
    updateTask,
    toggleTaskStatus,
    deleteTask,
    clearError
  }
}) 