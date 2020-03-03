<template>
  <v-container @click.stop="toggleDrawer" class="d-flex justify-end pa-0">
    <v-app-bar-nav-icon class="mx-2" fab dark small color="yellow"></v-app-bar-nav-icon>
  </v-container>
</template>

<script>
import { mapActions } from 'vuex'
export default {
  name: 'DrawerButton',
  data() {
    return {}
  },
  methods: {
    ...mapActions(['toggleDrawer'])
  }
}
</script>