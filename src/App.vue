<template>
  <section class="hero">
    <div class="hero-body">
      <div class="container">
        <h1 class="title">
          Bitcoin Checker
        </h1>
        <h2 class="subtitle">
          Value of bitcoin
        </h2>
      </div>
    </div>
  </section>

<div class="columns p-6">

  <div class="column has-background-grey-light">
    <div class="control">
  <input class="input" type="text" placeholder="Normal input">
</div>
    <div class="columns">
      <div class="column is-one-quarter">
        <input class="input is-rounded" type="text" value="1">
      </div>
      <div class="is-one-quarter select">      
        <select>
          <option>Bitcoin</option>
          <option>Dolar</option>
        </select>
      </div>
      <div class="column is-one-quarter">      
        <input class="input is-rounded" type="text" value="32,000">
      </div>
      <div class="column is-one-quarter">      
        <input class="input is-rounded" type="text" value=" R$" disabled>
      </div>
    </div>
  </div>
  
  <div class="column">
    <HelloWorld />
  </div>
</div>

<div class="columns is-centered ">
  <div class="column is-one-third">
    <p class="is-primary">
      <img class="" id="svg" alt="Vue" src="./assets/Investing.svg">
    </p>
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

<style lang="scss">
#app {
  font-family: "Roboto";
  font-weight: 400;
}

</style>
