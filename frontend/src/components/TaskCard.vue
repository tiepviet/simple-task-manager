<template>
  <div
    class="bg-white rounded-lg shadow-sm border border-gray-200 p-6 hover:shadow-md transition-all duration-200 animate-slide-up"
    :class="{ 'opacity-75 bg-gray-50': task.status === 'done' }"
  >
    <div class="flex items-start justify-between mb-4">
      <div class="flex items-center space-x-3 flex-1">
        <input
          type="checkbox"
          :checked="task.status === 'done'"
          @change="$emit('toggle-status', task.id)"
          class="h-4 w-4 text-primary-600 focus:ring-primary-500 border-gray-300 rounded cursor-pointer"
        />
        <h3
          class="text-lg font-medium text-gray-900 flex-1"
          :class="{ 'line-through text-gray-500': task.status === 'done' }"
        >
          {{ task.title }}
        </h3>
      </div>

      <div class="flex items-center space-x-2">
        <button
          @click="$emit('edit', task)"
          class="inline-flex items-center px-2.5 py-1.5 border border-gray-300 shadow-sm text-xs font-medium rounded text-gray-700 bg-white hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-primary-500 transition-colors duration-200"
        >
          <svg
            class="w-3 h-3 mr-1"
            fill="none"
            stroke="currentColor"
            viewBox="0 0 24 24"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z"
            ></path>
          </svg>
          Edit
        </button>
        <button
          @click="$emit('delete', task.id)"
          class="inline-flex items-center px-2.5 py-1.5 border border-transparent text-xs font-medium rounded text-white bg-red-600 hover:bg-red-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-red-500 transition-colors duration-200"
        >
          <svg
            class="w-3 h-3 mr-1"
            fill="none"
            stroke="currentColor"
            viewBox="0 0 24 24"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"
            ></path>
          </svg>
          Delete
        </button>
      </div>
    </div>

    <div v-if="task.detail" class="mb-4 text-sm text-gray-600 leading-relaxed">
      {{ task.detail }}
    </div>

    <div class="flex items-center justify-between">
      <div class="flex items-center space-x-3">
        <span class="badge" :class="priorityBadgeClass">
          {{ priorityText }}
        </span>

        <div v-if="task.due_date" class="flex items-center text-sm">
          <svg
            class="w-4 h-4 text-gray-400 mr-1"
            fill="none"
            stroke="currentColor"
            viewBox="0 0 24 24"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"
            ></path>
          </svg>
          <span class="font-medium" :class="{ 'text-red-600': isOverdue }">
            {{ formatDate(task.due_date) }}
          </span>
        </div>
      </div>

      <div class="flex items-center">
        <span
          class="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium"
          :class="statusBadgeClass"
        >
          <div
            class="w-2 h-2 rounded-full mr-1.5"
            :class="statusDotClass"
          ></div>
          {{ task.status === "done" ? "Completed" : "Pending" }}
        </span>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import type { Task } from "@/services/tasks";
import { computed } from "vue";

interface Props {
  task: Task;
}

const props = defineProps<Props>();

defineEmits<{
  "toggle-status": [taskId: string];
  edit: [task: Task];
  delete: [taskId: string];
}>();

const priorityText = computed(() => {
  const priorities = ["Low", "Medium", "High", "Urgent"];
  return priorities[props.task.priority] || "Low";
});

const priorityBadgeClass = computed(() => {
  const classes = [
    "bg-green-100 text-green-800",
    "bg-yellow-100 text-yellow-800",
    "bg-orange-100 text-orange-800",
    "bg-red-100 text-red-800",
  ];
  return classes[props.task.priority] || classes[0];
});

const statusBadgeClass = computed(() => {
  return props.task.status === "done"
    ? "bg-green-100 text-green-800"
    : "bg-blue-100 text-blue-800";
});

const statusDotClass = computed(() => {
  return props.task.status === "done" ? "bg-green-400" : "bg-blue-400";
});

const isOverdue = computed(() => {
  if (!props.task.due_date || props.task.status === "done") return false;
  const dueDate = new Date(props.task.due_date);
  const today = new Date();
  today.setHours(0, 0, 0, 0);
  return dueDate < today;
});

const formatDate = (dateString: string) => {
  return new Date(dateString).toLocaleDateString();
};
</script>
