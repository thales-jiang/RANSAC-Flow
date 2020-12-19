<template>
  <div class="game">
    <div>Wumpus</div>
    <div><canvas ref="game" width="500" height="500"></canvas></div>
  </div>
</template>

<script>
import * as Wumpus from "./wumpus/main";
export default {
  name: 'Game',
  props: {
    msg: String
  },
  mounted() {
    let __wumpus = new Wumpus.main(this.$refs['game']);
    __wumpus.start();
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
