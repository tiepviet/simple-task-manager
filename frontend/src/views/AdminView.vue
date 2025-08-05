<template>
  <div class="space-y-6">
    <!-- Header -->
    <div>
      <h1 class="text-2xl font-bold text-gray-900">Admin Dashboard</h1>
      <p class="mt-1 text-sm text-gray-500">
        Monitor users, tasks, and overall system performance
      </p>
    </div>

    <!-- Statistics -->
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
      <div class="card">
        <div class="flex items-center">
          <div class="flex-shrink-0">
            <div
              class="h-8 w-8 rounded-full bg-blue-100 flex items-center justify-center"
            >
              <svg
                class="h-5 w-5 text-blue-600"
                fill="none"
                stroke="currentColor"
                viewBox="0 0 24 24"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197m13.5-9a2.5 2.5 0 11-5 0 2.5 2.5 0 015 0z"
                ></path>
              </svg>
            </div>
          </div>
          <div class="ml-4">
            <p class="text-sm font-medium text-gray-500">Total Users</p>
            <p class="text-2xl font-semibold text-gray-900">
              {{ users.length }}
            </p>
          </div>
        </div>
      </div>

      <div class="card">
        <div class="flex items-center">
          <div class="flex-shrink-0">
            <div
              class="h-8 w-8 rounded-full bg-green-100 flex items-center justify-center"
            >
              <svg
                class="h-5 w-5 text-green-600"
                fill="none"
                stroke="currentColor"
                viewBox="0 0 24 24"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M9 5H7a2 2 0 00-2 2v10a2 2 0 002 2h8a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-3 7h3m-3 4h3m-6-4h.01M9 16h.01"
                ></path>
              </svg>
            </div>
          </div>
          <div class="ml-4">
            <p class="text-sm font-medium text-gray-500">Total Tasks</p>
            <p class="text-2xl font-semibold text-gray-900">
              {{ allTasks.length }}
            </p>
          </div>
        </div>
      </div>

      <div class="card">
        <div class="flex items-center">
          <div class="flex-shrink-0">
            <div
              class="h-8 w-8 rounded-full bg-purple-100 flex items-center justify-center"
            >
              <svg
                class="h-5 w-5 text-purple-600"
                fill="none"
                stroke="currentColor"
                viewBox="0 0 24 24"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"
                ></path>
              </svg>
            </div>
          </div>
          <div class="ml-4">
            <p class="text-sm font-medium text-gray-500">Completed Tasks</p>
            <p class="text-2xl font-semibold text-gray-900">
              {{ completedTasks.length }}
            </p>
          </div>
        </div>
      </div>

      <div class="card">
        <div class="flex items-center">
          <div class="flex-shrink-0">
            <div
              class="h-8 w-8 rounded-full bg-yellow-100 flex items-center justify-center"
            >
              <svg
                class="h-5 w-5 text-yellow-600"
                fill="none"
                stroke="currentColor"
                viewBox="0 0 24 24"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z"
                ></path>
              </svg>
            </div>
          </div>
          <div class="ml-4">
            <p class="text-sm font-medium text-gray-500">Completion Rate</p>
            <p class="text-2xl font-semibold text-gray-900">
              {{ completionRate }}%
            </p>
          </div>
        </div>
      </div>
    </div>

    <!-- Filters -->
    <div class="card">
      <div class="flex items-center justify-between mb-4">
        <h3 class="text-lg font-medium text-gray-900 flex items-center">
          <svg
            class="w-5 h-5 text-gray-400 mr-2"
            fill="none"
            stroke="currentColor"
            viewBox="0 0 24 24"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              d="M3 4a1 1 0 011-1h16a1 1 0 011 1v2.586a1 1 0 01-.293.707l-6.414 6.414a1 1 0 00-.293.707V17l-4 4v-6.586a1 1 0 00-.293-.707L3.293 7.293A1 1 0 013 6.586V4z"
            ></path>
          </svg>
          Filters
        </h3>
        <button
          @click="clearFilters"
          class="text-sm text-gray-500 hover:text-gray-700"
        >
          Clear all
        </button>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
        <div>
          <label for="user-filter" class="form-label">User</label>
          <select id="user-filter" v-model="filters.user_id" class="form-input">
            <option value="">All Users</option>
            <option v-for="user in users" :key="user.id" :value="user.id">
              {{ user.username }}
            </option>
          </select>
        </div>

        <div>
          <label for="status-filter" class="form-label">Status</label>
          <select
            id="status-filter"
            v-model="filters.status"
            class="form-input"
          >
            <option value="">All Status</option>
            <option value="todo">Todo</option>
            <option value="done">Done</option>
          </select>
        </div>

        <div class="flex items-end">
          <button
            @click="applyFilters"
            class="w-full inline-flex justify-center items-center px-4 py-2 border border-transparent text-sm font-medium rounded-md text-white bg-primary-600 hover:bg-primary-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-primary-500 transition-colors duration-200"
          >
            <svg
              class="w-4 h-4 mr-2"
              fill="none"
              stroke="currentColor"
              viewBox="0 0 24 24"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"
              ></path>
            </svg>
            Apply Filters
          </button>
        </div>
      </div>
    </div>

    <!-- Users Section -->
    <div>
      <h2 class="text-xl font-semibold text-gray-900 mb-4 flex items-center">
        <svg
          class="w-5 h-5 text-gray-400 mr-2"
          fill="none"
          stroke="currentColor"
          viewBox="0 0 24 24"
        >
          <path
            stroke-linecap="round"
            stroke-linejoin="round"
            stroke-width="2"
            d="M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197m13.5-9a2.5 2.5 0 11-5 0 2.5 2.5 0 015 0z"
          ></path>
        </svg>
        Users ({{ users.length }})
      </h2>
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        <div v-for="user in users" :key="user.id" class="card">
          <div class="flex items-center justify-between mb-4">
            <div class="flex items-center">
              <div
                class="h-10 w-10 rounded-full bg-gray-300 flex items-center justify-center"
              >
                <span class="text-sm font-medium text-gray-700">
                  {{ user.username.charAt(0).toUpperCase() }}
                </span>
              </div>
              <div class="ml-3">
                <p class="text-sm font-medium text-gray-900">
                  {{ user.username }}
                </p>
                <p class="text-sm text-gray-500">{{ user.email }}</p>
              </div>
            </div>
            <div v-if="user.is_admin" class="badge badge-danger">Admin</div>
          </div>

          <div class="grid grid-cols-2 gap-4">
            <div class="text-center p-3 bg-gray-50 rounded-lg">
              <p class="text-2xl font-bold text-gray-900">
                {{ getUserTaskCount(user.id) }}
              </p>
              <p class="text-xs text-gray-500">Total Tasks</p>
            </div>
            <div class="text-center p-3 bg-gray-50 rounded-lg">
              <p class="text-2xl font-bold text-green-600">
                {{ getUserCompletedCount(user.id) }}
              </p>
              <p class="text-xs text-gray-500">Completed</p>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- All Tasks Section -->
    <div>
      <h2 class="text-xl font-semibold text-gray-900 mb-4 flex items-center">
        <svg
          class="w-5 h-5 text-gray-400 mr-2"
          fill="none"
          stroke="currentColor"
          viewBox="0 0 24 24"
        >
          <path
            stroke-linecap="round"
            stroke-linejoin="round"
            stroke-width="2"
            d="M9 5H7a2 2 0 00-2 2v10a2 2 0 002 2h8a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-3 7h3m-3 4h3m-6-4h.01M9 16h.01"
          ></path>
        </svg>
        All Tasks ({{ filteredTasks.length }})
      </h2>

      <div v-if="loading" class="loading">
        <svg
          class="animate-spin h-8 w-8 text-primary-600"
          xmlns="http://www.w3.org/2000/svg"
          fill="none"
          viewBox="0 0 24 24"
        >
          <circle
            class="opacity-25"
            cx="12"
            cy="12"
            r="10"
            stroke="currentColor"
            stroke-width="4"
          ></circle>
          <path
            class="opacity-75"
            fill="currentColor"
            d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"
          ></path>
        </svg>
        <p class="mt-2 text-gray-500">Loading tasks...</p>
      </div>

      <div v-else-if="filteredTasks.length === 0" class="text-center py-12">
        <svg
          class="mx-auto h-12 w-12 text-gray-400"
          fill="none"
          stroke="currentColor"
          viewBox="0 0 24 24"
        >
          <path
            stroke-linecap="round"
            stroke-linejoin="round"
            stroke-width="2"
            d="M9 5H7a2 2 0 00-2 2v10a2 2 0 002 2h8a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-3 7h3m-3 4h3m-6-4h.01M9 16h.01"
          ></path>
        </svg>
        <h3 class="mt-2 text-sm font-medium text-gray-900">No tasks found</h3>
        <p class="mt-1 text-sm text-gray-500">Try adjusting your filters.</p>
      </div>

      <div v-else class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        <div v-for="task in filteredTasks" :key="task.id" class="card">
          <div class="flex items-start justify-between mb-3">
            <h4 class="text-sm font-medium text-gray-900 line-clamp-2">
              {{ task.title }}
            </h4>
            <span
              class="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-gray-100 text-gray-800 ml-2"
            >
              {{ getUserName(task.owner_id) }}
            </span>
          </div>

          <div
            v-if="task.detail"
            class="text-sm text-gray-600 mb-3 line-clamp-2"
          >
            {{ task.detail }}
          </div>

          <div class="flex items-center justify-between">
            <div class="flex items-center space-x-2">
              <span
                class="badge"
                :class="task.status === 'done' ? 'badge-success' : 'badge-info'"
              >
                {{ task.status === "done" ? "Completed" : "Pending" }}
              </span>
              <span class="badge" :class="getPriorityBadgeClass(task.priority)">
                {{ getPriorityText(task.priority) }}
              </span>
            </div>

            <div v-if="task.due_date" class="text-xs text-gray-500">
              {{ formatDate(task.due_date) }}
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import type { User } from "@/services/auth";
import { authService } from "@/services/auth";
import type { Task } from "@/services/tasks";
import { taskService } from "@/services/tasks";
import { computed, onMounted, reactive, ref } from "vue";

const users = ref<User[]>([]);
const allTasks = ref<Task[]>([]);
const loading = ref(false);

const filters = reactive({
  user_id: "",
  status: "",
});

onMounted(async () => {
  await Promise.all([loadUsers(), loadAllTasks()]);
});

const loadUsers = async () => {
  try {
    users.value = await authService.getUsers();
  } catch (error) {
    console.error("Failed to load users:", error);
  }
};

const loadAllTasks = async () => {
  loading.value = true;
  try {
    allTasks.value = await taskService.getAllTasks();
  } catch (error) {
    console.error("Failed to load tasks:", error);
  } finally {
    loading.value = false;
  }
};

const applyFilters = async () => {
  loading.value = true;
  try {
    const filterParams: any = {};
    if (filters.user_id) filterParams.user_id = filters.user_id;
    if (filters.status) filterParams.status = filters.status;

    allTasks.value = await taskService.getAllTasks(filterParams);
  } catch (error) {
    console.error("Failed to apply filters:", error);
  } finally {
    loading.value = false;
  }
};

const clearFilters = () => {
  filters.user_id = "";
  filters.status = "";
  loadAllTasks();
};

const completedTasks = computed(() =>
  allTasks.value.filter((task) => task.status === "done")
);

const completionRate = computed(() => {
  if (allTasks.value.length === 0) return 0;
  return Math.round(
    (completedTasks.value.length / allTasks.value.length) * 100
  );
});

const filteredTasks = computed(() => allTasks.value);

const getUserTaskCount = (userId: string) => {
  return allTasks.value.filter((task) => task.owner_id === userId).length;
};

const getUserCompletedCount = (userId: string) => {
  return allTasks.value.filter(
    (task) => task.owner_id === userId && task.status === "done"
  ).length;
};

const getUserName = (userId: string) => {
  const user = users.value.find((u) => u.id === userId);
  return user ? user.username : "Unknown";
};

const getPriorityText = (priority: number) => {
  const priorities = ["Low", "Medium", "High", "Urgent"];
  return priorities[priority] || "Low";
};

const getPriorityBadgeClass = (priority: number) => {
  const classes = [
    "bg-green-100 text-green-800",
    "bg-yellow-100 text-yellow-800",
    "bg-orange-100 text-orange-800",
    "bg-red-100 text-red-800",
  ];
  return classes[priority] || classes[0];
};

const formatDate = (dateString: string) => {
  return new Date(dateString).toLocaleDateString();
};
</script>
