<template>
  <div class="uk-text-center container">
  <div v-if="status == 404">
    post not found
  </div>
  <div v-else>
    <div>{{ post.title }}</div>
    <div>{{ post.content }}</div>
    <div>Created At: {{ post.createdat }}</div>
    <div>Last Modified: {{ post.updatedat }}</div>

    <div class="center">
      <button @click="this.$router.push('/edit/' + id)">
        <i class="fas fa-pencil edit"></i>
      </button>
      <button @click="this.$router.push('/delete/' + id)"> 
        <i class="fas fa-trash delete"></i>
      </button>
    </div>
  </div>
</div>
</template>

<script>
import axios from 'axios'
import { getPostInfo } from './getPostInfo'
import { getStatus } from './getStatus'
import { serverurl } from '../../data'

export default {
  data(){
    return {
      post: '',
      id: this.$route.params.id,
      status: ''
    }
  },
  async created() {
    this.status = await getStatus(this.id)
    this.post = await getPostInfo(this.id)
    this.$watch(
      () => this.$route.params,
      async (toParams, previousParams) => {
        console.log(toParams.id)
        this.post = this.getPost(toParams.id)
      }
    )
  }
}
</script>