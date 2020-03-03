<template>
  <v-container class="sign-in-up d-flex justify-end pa-0">
    <a class="tile">Log In</a>
    <v-btn
      @click.prevent
      depressed
      small
      color="#02B159"
      :ripple="false"
      class="tile register-button"
    >
      <a href="#">Sign Up</a>
    </v-btn>
  </v-container>
</template>

<script>
export default {
  name: 'SignInUp',
  data() {
    return {}
  }
}
</script>

<style scoped>
.sign-in-up * {
  color: #4a4a4a;
  font-weight: 500;
  font-size: 16px;
  text-decoration: none;
}

.sign-in-up > * {
  margin: 0 0 0 20px;
}

.register-button a {
  color: white;
}
</style>