<template>
  <v-btn class="btn" depressed color="rgba(20, 18, 40, 0.98)" dark rounded>
    <slot>Let's Go!</slot>
  </v-btn>
</template>

<script>
export default {
  name: 'FilledButton',
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
