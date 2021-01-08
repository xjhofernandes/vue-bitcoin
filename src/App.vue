<template>
  <section class="hero">
    <div class="hero-body">
      <div class="container">
        <h1 class="title">Bitcoin Checker</h1>
        <h2 class="subtitle">A simple site to check the bitcoin price</h2>

        <div class="columns mb-5 mt-5">
          <div class="column is-two-fifths">
            <div>
              <img class="" id="svg" alt="Vue" src="./assets/Investing.svg" />
            </div>
          </div>
          <div class="column">
            <bitcoinChart />
          </div>
        </div>
      </div>
    </div>
  </section>
  <pageFooter />
</template>

<script>
import bitcoinChart from "./components/bitcoinChart.vue";
import pageFooter from "./components/pageFooter.vue";

export default {
  name: "App",
  components: {
    bitcoinChart,
    pageFooter,
  },
};
</script>

<style lang="scss">
#app {
  font-family: "Roboto";
  font-weight: 400;
}
</style>
