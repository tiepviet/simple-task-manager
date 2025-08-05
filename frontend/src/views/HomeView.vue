<template>
  <div class="space-y-6">
    <!-- Header -->
    <div class="flex flex-col sm:flex-row sm:items-center sm:justify-between">
      <div>
        <h1 class="text-2xl font-bold text-gray-900">My Tasks</h1>
        <p class="mt-1 text-sm text-gray-500">
          Manage and organize your tasks efficiently
        </p>
      </div>
      <div class="mt-4 sm:mt-0">
        <button
          @click="showCreateForm = true"
          class="inline-flex items-center px-4 py-2 border border-transparent text-sm font-medium rounded-md shadow-sm text-white bg-primary-600 hover:bg-primary-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-primary-500 transition-colors duration-200"
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
              d="M12 6v6m0 0v6m0-6h6m-6 0H6"
            ></path>
          </svg>
          Add New Task
        </button>
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

      <div class="grid grid-cols-1 md:grid-cols-4 gap-4">
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

        <div>
          <label for="priority-filter" class="form-label">Priority</label>
          <select
            id="priority-filter"
            v-model="filters.priority"
            class="form-input"
          >
            <option value="">All Priorities</option>
            <option value="0">Low</option>
            <option value="1">Medium</option>
            <option value="2">High</option>
            <option value="3">Urgent</option>
          </select>
        </div>

        <div>
          <label for="due-date-filter" class="form-label">Due Before</label>
          <input
            id="due-date-filter"
            v-model="filters.due_before"
            type="date"
            class="form-input"
          />
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
            Apply
          </button>
        </div>
      </div>
    </div>

    <!-- Error Message -->
    <div v-if="taskStore.error" class="alert alert-error">
      <div class="flex">
        <svg
          class="w-5 h-5 text-red-400 mr-2"
          fill="none"
          stroke="currentColor"
          viewBox="0 0 24 24"
        >
          <path
            stroke-linecap="round"
            stroke-linejoin="round"
            stroke-width="2"
            d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"
          ></path>
        </svg>
        {{ taskStore.error }}
      </div>
      <button
        @click="taskStore.clearError()"
        class="ml-auto text-red-400 hover:text-red-600"
      >
        <svg
          class="w-4 h-4"
          fill="none"
          stroke="currentColor"
          viewBox="0 0 24 24"
        >
          <path
            stroke-linecap="round"
            stroke-linejoin="round"
            stroke-width="2"
            d="M6 18L18 6M6 6l12 12"
          ></path>
        </svg>
      </button>
    </div>

    <!-- Loading State -->
    <div v-if="taskStore.loading" class="loading">
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

    <!-- Task Lists -->
    <div v-else class="space-y-8">
      <!-- Todo Tasks -->
      <div>
        <div class="flex items-center justify-between mb-4">
          <h2 class="text-xl font-semibold text-gray-900 flex items-center">
            <div class="w-3 h-3 bg-blue-500 rounded-full mr-3"></div>
            Todo Tasks
            <span
              class="ml-2 inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-blue-100 text-blue-800"
            >
              {{ taskStore.todoTasks.length }}
            </span>
          </h2>
        </div>

        <div v-if="taskStore.todoTasks.length === 0" class="text-center py-12">
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
          <h3 class="mt-2 text-sm font-medium text-gray-900">No todo tasks</h3>
          <p class="mt-1 text-sm text-gray-500">
            Get started by creating a new task.
          </p>
          <div class="mt-6">
            <button
              @click="showCreateForm = true"
              class="inline-flex items-center px-4 py-2 border border-transparent shadow-sm text-sm font-medium rounded-md text-white bg-primary-600 hover:bg-primary-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-primary-500"
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
                  d="M12 6v6m0 0v6m0-6h6m-6 0H6"
                ></path>
              </svg>
              Add Task
            </button>
          </div>
        </div>

        <div
          v-else
          class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6"
        >
          <TaskCard
            v-for="task in taskStore.todoTasks"
            :key="task.id"
            :task="task"
            @toggle-status="taskStore.toggleTaskStatus"
            @edit="editTask"
            @delete="deleteTask"
          />
        </div>
      </div>

      <!-- Done Tasks -->
      <div>
        <div class="flex items-center justify-between mb-4">
          <h2 class="text-xl font-semibold text-gray-900 flex items-center">
            <div class="w-3 h-3 bg-green-500 rounded-full mr-3"></div>
            Completed Tasks
            <span
              class="ml-2 inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-green-100 text-green-800"
            >
              {{ taskStore.doneTasks.length }}
            </span>
          </h2>
        </div>

        <div v-if="taskStore.doneTasks.length === 0" class="text-center py-12">
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
              d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"
            ></path>
          </svg>
          <h3 class="mt-2 text-sm font-medium text-gray-900">
            No completed tasks
          </h3>
          <p class="mt-1 text-sm text-gray-500">
            Complete some tasks to see them here.
          </p>
        </div>

        <div
          v-else
          class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6"
        >
          <TaskCard
            v-for="task in taskStore.doneTasks"
            :key="task.id"
            :task="task"
            @toggle-status="taskStore.toggleTaskStatus"
            @edit="editTask"
            @delete="deleteTask"
          />
        </div>
      </div>
    </div>

    <!-- Create Task Modal -->
    <TaskModal
      v-if="showCreateForm"
      :task="null"
      @close="showCreateForm = false"
      @save="createTask"
    />

    <!-- Edit Task Modal -->
    <TaskModal
      v-if="showEditForm"
      :task="editingTask"
      @close="showEditForm = false"
      @save="updateTask"
    />
  </div>
</template>

<script setup lang="ts">
import TaskCard from "@/components/TaskCard.vue";
import TaskModal from "@/components/TaskModal.vue";
import type { Task, TaskCreate, TaskUpdate } from "@/services/tasks";
import { useTaskStore } from "@/stores/tasks";
import { onMounted, reactive, ref } from "vue";

const taskStore = useTaskStore();

const showCreateForm = ref(false);
const showEditForm = ref(false);
const editingTask = ref<Task | null>(null);

const filters = reactive({
  status: "",
  priority: "",
  due_before: "",
});

onMounted(() => {
  taskStore.fetchTasks();
});

const applyFilters = () => {
  const filterParams: any = {};
  if (filters.status) filterParams.status = filters.status;
  if (filters.priority) filterParams.priority = parseInt(filters.priority);
  if (filters.due_before) filterParams.due_before = filters.due_before;

  taskStore.fetchTasks(filterParams);
};

const clearFilters = () => {
  filters.status = "";
  filters.priority = "";
  filters.due_before = "";
  taskStore.fetchTasks();
};

const createTask = async (taskData: TaskCreate | TaskUpdate) => {
  try {
    await taskStore.createTask(taskData as TaskCreate);
    showCreateForm.value = false;
  } catch (error) {
    // Error is handled by the store
  }
};

const editTask = (task: Task) => {
  editingTask.value = task;
  showEditForm.value = true;
};

const updateTask = async (taskData: TaskUpdate) => {
  if (!editingTask.value) return;

  try {
    await taskStore.updateTask(editingTask.value.id, taskData);
    showEditForm.value = false;
    editingTask.value = null;
  } catch (error) {
    // Error is handled by the store
  }
};

const deleteTask = async (taskId: string) => {
  if (confirm("Are you sure you want to delete this task?")) {
    try {
      await taskStore.deleteTask(taskId);
    } catch (error) {
      // Error is handled by the store
    }
  }
};
</script>
