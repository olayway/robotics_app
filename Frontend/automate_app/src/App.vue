<template>
  <v-app>
    <NavBar></NavBar>
    <NavDrawer></NavDrawer>
    <v-content>
      <router-view></router-view>
    </v-content>
  </v-app>
</template>

<script>
import NavBar from '@/components/navigation/NavBar.vue'
import NavDrawer from '@/components/navigation/NavDrawer.vue'

export default {
  name: 'App',

  components: { NavBar, NavDrawer },

  data() {
    return
  },
  methods: {}
}
</script>


