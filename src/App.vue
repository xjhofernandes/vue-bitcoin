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

    <div class="column is-two-fifths">
      <p class="is-primary">
        <img class="" id="svg" alt="Vue" src="./assets/Investing.svg">
      </p>
    </div>
    
    <div class="column">
      <HelloWorld />
    </div>
  </div>

<footer class="footer has-background-dark">
  <div class="content has-text-centered">
    <p class="has-text-white">
      <strong class="has-text-white">Site</strong> by <a href="https://jhofernandes.dev">Jonathan Fernandes</a>. The source code is licensed
      <a href="http://opensource.org/licenses/mit-license.php">MIT</a>. The website content
      is licensed <a href="http://creativecommons.org/licenses/by-nc-sa/4.0/">CC BY NC SA 4.0</a>.
    </p>
  </div>
</footer>
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
