<template>
	<div class="container">
	  <h1>Welcome to <span style="font-weight: bold"> {{title}} </span>! </h1>
	  <div>Create your first post now:
	    <button class="create-post button" 
	    @click="this.$router.push('/create')">
	    	Create Post 
	  	</button>
	  </div>
	  <div>
	    Take a look at this list of your posts: 
	    <button class="button" @click="this.$router.push('/posts')">Posts</button>
	  </div>
	  <div class="uk-margin-medium-top">
	    <strong>Note:</strong> Still maintaining the client-side
	  </div>
	</div>
</template>

<script>
import axios from 'axios'
import { title, serverurl as server } from '../data'

export default {
	data(){
		return {
			title
		}
	},
	beforeMount(){
		window.history.pushState({}, "Hide", "http://127.0.0.1:3000/#/")
	}
}

</script>