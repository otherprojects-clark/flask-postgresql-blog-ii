<template>
	<div class="container">
	  <div style="text-align: center;">
	    <!-- <div v-if="">You currently don't have any posts. </div> -->
	  	<div v-for="x in posts">
	  		<!-- if you have posts -->
	    <!-- {% for x in posts %}  /post/{{x[id]}} -->
	      <div><router-link	:to="'/post/' + x.id">{{x.title}}</router-link	></div>  
	      <div>Created At: {{x.createdat}}</div>
	      <br> 
	    <!-- {% endfor %} -->
	  <!-- {% endif %} -->
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