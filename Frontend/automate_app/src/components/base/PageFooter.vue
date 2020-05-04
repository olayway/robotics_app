<template>
  <v-footer light padless>
    <v-card flat tile width="100%" class="text-center py-1">
      <v-card-text class="py-2">
        <v-btn v-for="icon in icons" :key="icon" class="mx-4 grey--text" icon>
          <v-icon size="22px">{{ icon }}</v-icon>
        </v-btn>
      </v-card-text>

      <v-divider></v-divider>

      <v-card-text class="grey--text">
        Copyright © {{ new Date().getFullYear() }}
        <strong>Yaskawa Polska Sp. z o.o.</strong>
      </v-card-text>
    </v-card>
  </v-footer>
</template>

<script>
export default {
  name: 'PageFooter',
  data() {
    return {
      icons: ['mdi-facebook', 'mdi-twitter', 'mdi-linkedin']
    }
  }
}
</script>
