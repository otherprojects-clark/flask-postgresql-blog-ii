<template>
	<div class="container">
		<div v-if="status == 404">
			post not found
		</div>
	  <div v-else>
	  	Are you sure you want to delete "{{post.title}}"?
		  <div>
		    <form @submit="deletePost">
		      <div class="uk-flex uk-flex-column">
		        <div>
		          <input type="radio" name="delete" value="false" checked v-model="delete">
		          Nope, I'll keep it
		        </div>
		        <div>
		          <input type="radio" name="delete" value="true" v-model="delete">
		          Yes, I do
		        </div>
		      </div>
		      <br>
		      <input type="submit" value="ok" class="uk-margin-small-top uk-button uk-button-danger" >
		    </form>
		    <button @click="this.$router.push('/')" class="uk-button-primary uk-button"> Cancel </button>
		  </div>  
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
			delete: 'false',
			status: ''
		}
	},
	methods: {
    async deletePost(){
    	if (this.delete == 'false'){
    		this.$router.push('/')
    	} else {
	    	try {
	    		await axios.post(serverurl + `delete/${this.id}`, {
	    			delete: this.delete
	    		})
	    	} catch(err) {
	    		throw err
	    	}
    	}
    }
  },
  async mounted(){
  	this.post = await getPostInfo(this.id)
  	this.status = await getStatus(this.id)
  }
}
</script>