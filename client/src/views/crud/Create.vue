<template>
	<div class="container">
	  <h1>Create Post</h1>
	  <form action="" class="create-form" @submit="createPost">
	    <label for="title">Title</label>
	    <input type="text" class="uk-input" placeholder="Title" name="title" v-model="title" required>

	    <label for="content">Content</label>
	    <textarea name="content" cols="30" rows="10" class="uk-textarea" placeholder="What's on your mind?" v-model="content"></textarea>
	    <input type="submit" class="submit uk-button" value="create">
	    
	    <div id="test"></div>
	  </form>
    <button class="submit uk-button" @click="this.$router.push('/')">Back</button>
	</div>
</template>

<script>
import { serverurl as server } from '../../data'
import axios from 'axios'

export default {
	data(){
		return {
			title: '',
			content: ''
		}
	},
	methods: {
		async createPost(){
			axios.post(server + 'create', {
				title: this.title,
				content: this.content
			}).then(res => { console.log(res) })
		}
	}
}
</script>