<template>
  <div class="h-16 bg-gray-900 mb-8">
    <!-- <img class="as" alt="Vue" src="./assets/bitcoin.svg"> -->
    <p>Bitcoin Home</p> 
  </div>

  <!-- <img alt="Vue logo" src="./assets/logo.png"> -->
  <div class="flex justify-between px-24">
    <div class="">
      <img class="h-96" alt="Vue" src="./assets/Investing.svg">
    </div>
    <div class="">
      <HelloWorld />
    </div>
  </div>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue'

export default {
  name: 'App',
  components: {
    HelloWorld
  }
}
</script>

<style>
/* #app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
  margin-top: 0px;
} */

/* .head{
  display: flex;
  align-items: center;
  justify-content: center;
  height: 85px;
  margin-bottom: 60px;
  color: white;
  background: #50514F;
}

.head p{
  font-size: 2em;
  color: white;
}

.container{
  padding-left: 15%;
  padding-right: 15%;
}

.bitcoin{
  height: 24em;
  color: #2e86c1;
} */
</style>
