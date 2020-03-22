<template>
  <v-btn class="btn" color="white" rounded outlined>
    <slot>Let's Go!</slot>
  </v-btn>
</template>

<script>
export default {
  name: 'OutlinedButton',
  data() {
    return {}
  }
}
</script>

<style scoped>
.btn {
  font-family: Maven Pro;
  font-style: normal;
  font-weight: normal;
  text-transform: initial;
  font-size: 16px;
  letter-spacing: 0;
  margin: 10px 0;
}
</style>
