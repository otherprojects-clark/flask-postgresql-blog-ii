import { createRouter, createWebHashHistory } from 'vue-router'
import { createApp } from 'vue'
import App from './App.vue'

import './style.css'
import 'uikit/dist/css/uikit.min.css'
import '@fortawesome/fontawesome-free/css/all.min.css'

const routes = [
  { path: "/", component: () => import("./views/Index.vue") },
  { path: "/about", component: () => import("./views/About.vue") },
  { path: "/:pathMatch(.*)*", component: () => import("./views/404.vue") },
  { path: "/create", component: () => import("./views/crud/Create.vue") },
  { path: "/delete/:id", component: () => import("./views/crud/Delete.vue") },
  { path: "/edit/:id", component: () => import("./views/crud/Edit.vue") },
  { path: "/post/:id", component: () => import("./views/crud/Post.vue") },
  { path: "/posts", component: () => import("./views/crud/Posts.vue") }
]

const router = createRouter({
	routes,
	history: createWebHashHistory()
})

createApp(App)
  .use(router)
  .mount('#app')
