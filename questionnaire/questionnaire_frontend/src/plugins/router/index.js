import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import LoginView from '@/views/LoginView.vue'
import RegistrationView from '@/views/RegistrationView.vue'
import TestView from '@/views/TestView.vue'

const routes = [
    {
      path: '/',
      name: 'main',
      component: HomeView,
    },
    {
      path: '/login',
      name: 'login',
      component: LoginView,
    },
    {
      path: '/registration',
      name: 'registration',
      component: RegistrationView,
    },

    {
      path: '/test/:id',
      name: 'test',
      component: TestView,
    },
]

  const router = createRouter({
    routes,
    history: createWebHistory(),

  })


  export default router;