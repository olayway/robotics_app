<template>
  <v-app-bar id="appBar" color="white" app elevate-on-scroll>
    <v-container id="nav-bar" class="pa-0">
      <v-row no-gutters class="align-center">
        <!-- Logo -->
        <v-col md="3">
          <router-link to="/">
            <AutoMateLogo font-size="25px"></AutoMateLogo>
          </router-link>
        </v-col>

        <!-- Main Navigation Buttons -->
        <v-col class="d-none d-lg-block" md="6">
          <v-container class="d-flex justify-center pa-0">
            <NavTile
              v-for="(item, index) in getNavTiles"
              :key="index"
              :title="item.title"
              :subtitles="item.subtitles"
            ></NavTile>
          </v-container>
        </v-col>

        <!-- Sign in/up buttons OR Drawer toggle button -->
        <v-col id="sign-in-up">
          <component :is="navigation"></component>
        </v-col>
      </v-row>
    </v-container>
  </v-app-bar>
</template>

<script>
import { mapGetters } from 'vuex'
import NavTile from './NavTile.vue'
import SignInUp from './SignInUp.vue'
import DrawerButton from './DrawerButton.vue'
import AutoMateLogo from '../base/AutoMateLogo.vue'

export default {
  name: 'NavBar',
  components: { NavTile, SignInUp, DrawerButton, AutoMateLogo },
  data() {
    return {
      // navBarStyle: {
      //   position: 'absolute'
      // }
    }
  },
  computed: {
    navigation() {
      if (['xs', 'sm', 'md'].includes(this.$vuetify.breakpoint.name)) {
        return DrawerButton
      } else {
        return SignInUp
      }
    },
    ...mapGetters(['getNavTiles'])
  }
}
</script>

<style scoped>
* {
  font-family: 'Maven Pro';
}

.tile {
  margin: 0 10px 0 10px;
}
</style>
