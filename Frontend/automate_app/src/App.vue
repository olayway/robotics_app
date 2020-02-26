<template>
  <v-app>
    <NavBar></NavBar>
    <NavDrawer></NavDrawer>
  </v-app>
</template>

<script>
import NavBar from '@/components/NavBar.vue'
import NavDrawer from '@/components/NavDrawer.vue'

export default {
  name: 'App',

  components: { NavBar, NavDrawer },

  data() {
    return
  },
  methods: {}
}
</script>


