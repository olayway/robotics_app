<template>
  <v-card flat tile>
    <v-container px-12>
      <v-row>
        <v-col>
          <h2 class="not-found">Oooops! Page not found...</h2>
        </v-col>
      </v-row>
    </v-container>
  </v-card>
</template>

<script>
export default {
  name: 'NotFound',
  data() {
    return {}
  }
}
</script>

<style scoped>
.not-found {
  font-family: Source Sans Pro;
  color: #4a4a4a;
}
</style>
