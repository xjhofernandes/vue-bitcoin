<template>
  <nav class="bg-gray-900">
    <div class="relative flex items-center justify-between h-16">
      <p class="text-white text-center text-2xl">Bitcoin Home</p> 
    </div>
  </nav>

  <!-- <img alt="Vue logo" src="./assets/logo.png"> -->
  <div class="flex justify-between px-24 pt-8">
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
#app {
  font-family: "Roboto";
  font-weight: 400;
}

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
