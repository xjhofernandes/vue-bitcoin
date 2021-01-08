<template>
  <footer class="footer has-background-black">
    <div
      class="container is-flex is-justify-content-space-between is-align-items-center pt-5"
    >
      <div class="has-text-white">
        <div class="has-text-white is-bold">
          Site by
          <a href="https://jhofernandes.dev">Jhon Jons.</a>
        </div>
        <div>
          The source code is
          <a href="http://opensource.org/licenses/mit-license.php">MIT</a>
          licensed.
        </div>
      </div>
      <div>
        <img
          class="bitcoin-svg"
          id="svg"
          alt="Vue"
          src="../assets/bitcoin.svg"
        />
      </div>
      <div class="has-text-white">Made in Vue, Bulma & FastApi</div>
    </div>
  </footer>
</template>

<script>
export default {
  name: "pageFooter",
};
</script>

<style scoped>
.bitcoin-svg {
  max-width: 6em;
}
</style>