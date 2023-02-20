import { createApp } from 'vue'
import './style.css'
import App from './App.vue'
import router from '@/plugins/router'
import apolloProvider from '@/plugins/apollo'

const app = createApp(App)
app.use(router)
app.use(apolloProvider)

app.mount('#app')