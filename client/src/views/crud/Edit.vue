<template>
	<div class="center">
    <div v-if="status == 404" class="container">
	    <div> Post with id {{ id }} not found </div>
    </div>
    <div v-else class="container">
      <h1>Editing "{{post.title}}" </h1>
      <form class="create-form" @submit="editPost">
        <label for="title">Title</label>
        <input name="title" type="text" class="uk-input" placeholder="Title" v-model="title">      
        <label for="content">Content</label>
        <textarea name="content" cols="30" rows="10" class="uk-textarea" placeholder="What's on your mind?" v-model="content"></textarea>
        <input type="submit" class="submit uk-button" value="edit">
      </form>
    </div>
	</div>
</template>

<script>
import axios from 'axios'
import { serverurl } from '../../data'
import { getStatus } from './getStatus'
import { getPostInfo } from './getPostInfo'

export default {
	data(){
		return {
			post: '',
			id: this.$route.params.id,
      title: '',
      content: '',
      status: ''
		}
	},
	methods: {
    async editPost(){
      await axios.post(serverurl + `edit/${this.id}`, {
        title: this.title,
        content: this.content
      })
    }
  },
  async created(){
  	this.post = await getPostInfo(this.id)
    this.status = await getStatus(this.id)
  }
}
</script>