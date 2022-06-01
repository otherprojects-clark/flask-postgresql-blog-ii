<template>
	<div class="container">
	  <h1 class="">About <span class="uk-text-bold">{{title}}</span> </h1>
	  <div class="uk-h2 uk-margin-remove-top"> 
	    A simple project made by <a href="https://github.com/clark-john" class="uk-text-primary uk-text-bold" target="_blank">Clark</a>
	  </div>
	  <div class="">
	    Tech Stack: 
	    <ul>
	      <li>Vue</li>
	      <li>Flask</li>
	      <li>PostgreSQL</li>
	    </ul>
	    Styling Tools:
	    <ul class="uk-margin-remove-top">
	      <li>PostCSS</li>
	    </ul>
	  </div>
	  <div>This project is used for practicing purposes.</div>
	</div>
</template>
<script>
import { title } from '../data'

export default {
	data(){
		return {
			title
		}
	}
}
</script>