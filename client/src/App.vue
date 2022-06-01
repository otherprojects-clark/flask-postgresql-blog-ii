<template>
  <nav class="navbar">
    <router-link to="/" class="brand"> {{title}} </router-link>
    <div>
      <router-link to="/about">About</router-link>
    </div>
  </nav>
  <div>
    <router-view />
  </div>
</template>
<script>
import { title } from './data'

export default {
  data(){
    return {
      title
    }
  }
}
</script>