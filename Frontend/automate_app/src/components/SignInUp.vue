<template>
  <v-container style="border: 1px solid green" class="d-flex justify-end pa-0">
    <a class="tile">Log In</a>
    <v-btn
      @click.prevent
      depressed
      small
      color="success"
      :ripple="false"
      class="tile register-button"
    >
      <a href>Sign Up</a>
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