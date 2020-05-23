<template>
  <v-container class="d-flex justify-end pa-0" @click.stop="openDrawer">
    <v-app-bar-nav-icon
      class="mx-2"
      fab
      dark
      small
      color="yellow"
    ></v-app-bar-nav-icon>
  </v-container>
</template>

<script>
import Bus from '../../utils/index'
export default {
  name: 'DrawerButton',
  data() {
    return {}
  },
  methods: {
    openDrawer() {
      Bus.$emit('open-drawer')
    }
  }
}
</script>
