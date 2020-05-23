<template>
  <v-container class="sign-in-up d-flex justify-end pa-0">
    <router-link to="/login">
      <a class="tile">Log In</a>
    </router-link>
    <v-btn
      depressed
      small
      color="#02B159"
      :ripple="false"
      class="tile register-button"
      @click.prevent
    >
      <router-link to="/register">
        <a href="#">Sign Up</a>
      </router-link>
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
  font-weight: 400;
  font-size: 16px;
  text-decoration: none;
}

.sign-in-up > * {
  margin: 0 0 0 20px;
}

.register-button a {
  font-size: 14px;
  color: white;
}
</style>
