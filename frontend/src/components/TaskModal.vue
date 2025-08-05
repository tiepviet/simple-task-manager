<template>
  <div
    class="fixed inset-0 bg-gray-600 bg-opacity-50 overflow-y-auto h-full w-full z-50 flex items-center justify-center p-4"
    @click="$emit('close')"
  >
    <div
      class="relative bg-white rounded-lg shadow-xl w-full max-w-md mx-auto"
      @click.stop
    >
      <!-- Header -->
      <div
        class="flex items-center justify-between p-6 border-b border-gray-200"
      >
        <div class="flex items-center">
          <div class="flex-shrink-0">
            <div
              class="h-8 w-8 rounded-full bg-primary-100 flex items-center justify-center"
            >
              <svg
                class="h-5 w-5 text-primary-600"
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
          <div class="ml-3">
            <h3 class="text-lg font-medium text-gray-900">
              {{ isEditing ? "Edit Task" : "Create New Task" }}
            </h3>
            <p class="text-sm text-gray-500">
              {{
                isEditing
                  ? "Update task details"
                  : "Add a new task to your list"
              }}
            </p>
          </div>
        </div>
        <button
          @click="$emit('close')"
          class="text-gray-400 hover:text-gray-600 transition-colors duration-200"
        >
          <svg
            class="w-6 h-6"
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

      <!-- Form -->
      <form @submit.prevent="handleSubmit" class="p-6 space-y-4">
        <div>
          <label for="title" class="form-label"
            >Title <span class="text-red-500">*</span></label
          >
          <input
            id="title"
            v-model="form.title"
            type="text"
            class="form-input"
            required
            placeholder="Enter task title"
          />
        </div>

        <div>
          <label for="detail" class="form-label">Description</label>
          <textarea
            id="detail"
            v-model="form.detail"
            class="form-input resize-none"
            rows="3"
            placeholder="Enter task details (optional)"
          ></textarea>
        </div>

        <div class="grid grid-cols-2 gap-4">
          <div>
            <label for="priority" class="form-label">Priority</label>
            <select id="priority" v-model="form.priority" class="form-input">
              <option value="0">Low</option>
              <option value="1">Medium</option>
              <option value="2">High</option>
              <option value="3">Urgent</option>
            </select>
          </div>

          <div>
            <label for="due-date" class="form-label">Due Date</label>
            <input
              id="due-date"
              v-model="form.due_date"
              type="date"
              class="form-input"
            />
          </div>
        </div>

        <div v-if="isEditing">
          <label for="status" class="form-label">Status</label>
          <select id="status" v-model="form.status" class="form-input">
            <option value="todo">Todo</option>
            <option value="done">Done</option>
          </select>
        </div>

        <!-- Actions -->
        <div
          class="flex items-center justify-end space-x-3 pt-4 border-t border-gray-200"
        >
          <button type="button" @click="$emit('close')" class="btn btn-outline">
            Cancel
          </button>
          <button type="submit" class="btn btn-primary" :disabled="loading">
            <svg
              v-if="!isEditing"
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
            <svg
              v-else
              class="w-4 h-4 mr-2"
              fill="none"
              stroke="currentColor"
              viewBox="0 0 24 24"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-8l-4-4m0 0L8 8m4-4v12"
              ></path>
            </svg>
            {{
              loading ? "Saving..." : isEditing ? "Update Task" : "Create Task"
            }}
          </button>
        </div>
      </form>
    </div>
  </div>
</template>

<script setup lang="ts">
import type { Task, TaskCreate, TaskUpdate } from "@/services/tasks";
import { computed, onMounted, reactive, ref } from "vue";

interface Props {
  task: Task | null;
}

const props = defineProps<Props>();

const emit = defineEmits<{
  close: [];
  save: [data: TaskCreate | TaskUpdate];
}>();

const loading = ref(false);

const isEditing = computed(() => !!props.task);

const form = reactive({
  title: "",
  detail: "",
  priority: 0,
  due_date: "",
  status: "todo",
});

onMounted(() => {
  if (props.task) {
    form.title = props.task.title;
    form.detail = props.task.detail || "";
    form.priority = props.task.priority;
    form.due_date = props.task.due_date || "";
    form.status = props.task.status;
  }
});

const handleSubmit = () => {
  const formData = {
    title: form.title,
    detail: form.detail || undefined,
    priority: form.priority,
    due_date: form.due_date || undefined,
  };

  if (isEditing.value) {
    (formData as TaskUpdate).status = form.status;
  }

  emit("save", formData);
};
</script>
