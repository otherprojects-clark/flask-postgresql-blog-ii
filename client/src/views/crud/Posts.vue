<template>
	<div class="container">
	  <div style="text-align: center;">
	  	<div v-for="x in posts">
	      <div><router-link	:to="'/post/' + x.id">{{x.title}}</router-link	></div>  
	      <div>Created At: {{x.createdat}}</div>
	      <br> 
	  	</div>
	  </div>
	</div>
</template>

<script>
import axios from 'axios'
import { serverurl as server } from '../../data'

export default {
	data(){
		return {
			posts: ''
		}
	},
	methods: {
		async getPosts(){
			try {
				let posts = await axios.get(server + 'posts')
				console.log(posts.data.data[0])
				this.posts = posts.data.data
			} catch(err) {
				throw err
			}
		}
	},
	mounted(){this.getPosts()}
}
</script>