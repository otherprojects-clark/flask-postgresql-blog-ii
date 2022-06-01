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
import { serverurl } from '../../data'

export default {
  data(){
    return {
      post: '',
      id: this.$route.params.id,
      status: ''
    }
  },
  methods: {
    async getPost(id = this.id){
      try {
        let post = await axios.get(serverurl + `post/${id}`)
        this.post = post.data
      } catch(err) {
        console.error(err)
        return err.response.status
      }
    },
    async getStatus(){
      try {
        let code = await axios.get(serverurl + `post/${this.id}`)
        return code.status
      } catch (err) {
        return err.response.status
      }
    }
  },
  async created() {
    this.status = await this.getStatus()
    this.post = this.getPost()
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