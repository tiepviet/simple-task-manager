import { useAuthStore } from "@/stores/auth";
import { createRouter, createWebHistory } from "vue-router";

const routes = [
  {
    path: "/",
    name: "Home",
    component: () => import("@/views/HomeView.vue"),
    meta: { requiresAuth: true },
  },
  {
    path: "/login",
    name: "Login",
    component: () => import("@/views/LoginView.vue"),
    meta: { requiresAuth: false },
  },
  {
    path: "/register",
    name: "Register",
    component: () => import("@/views/RegisterView.vue"),
    meta: { requiresAuth: false },
  },
  {
    path: "/admin",
    name: "Admin",
    component: () => import("@/views/AdminView.vue"),
    meta: { requiresAuth: true, requiresAdmin: true },
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

// Navigation guard
router.beforeEach(async (to, _from, next) => {
  const authStore = useAuthStore();

  // Initialize auth if not already done
  if (!authStore.user && authStore.token) {
    await authStore.initializeAuth();
  }

  if (to.meta.requiresAuth && !authStore.isAuthenticated) {
    next("/login");
  } else if (to.meta.requiresAdmin && !authStore.isAdmin) {
    next("/");
  } else if (to.path === "/login" && authStore.isAuthenticated) {
    next("/");
  } else {
    next();
  }
});

export default router;
