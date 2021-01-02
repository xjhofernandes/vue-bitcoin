<template>
<div class="head">
  <!-- <img class="as" alt="Vue" src="./assets/bitcoin.svg"> -->
  <p>Bitcoin Home</p> 
</div>
  <!-- <img alt="Vue logo" src="./assets/logo.png"> -->
  <div class="container">
    <img class="bitcoin" alt="Vue" src="./assets/Investing.svg">
    <HelloWorld />
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

.head{
  display: flex;
  align-items: center;
  justify-content: center;
  height: 85px;
  margin-bottom: 60px;
  color: white;
  background: black;
}

.head p{
  font-size: 2em;
  color: white;
}

.container{
  /* background: red; */
  padding-left: 15%;
  padding-right: 15%;
}

.bitcoin{
  height: 24em;
  color: #2e86c1;
}
</style>
