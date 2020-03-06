<template>
  <v-app-bar id="appBar" color="white" app elevate-on-scroll>
    <v-container id="nav-bar" class="pa-0">
      <v-row no-gutters class="align-center">
        <!-- Logo -->
        <v-col md="3">
          <v-container class="pa-0">
            <div id="logo" class="tile">
              <span>auto</span>mate
            </div>
          </v-container>
        </v-col>

        <!-- Main Navigation Buttons -->
        <v-col class="d-none d-lg-block" md="6">
          <v-container class="d-flex justify-center pa-0">
            <NavTile
              v-for="(item, index) in navTiles"
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

export default {
  name: 'NavBar',
  components: { NavTile, SignInUp, DrawerButton },
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
    ...mapGetters(['navTiles'])
  }
}
</script>

<style scoped>
* {
  font-family: 'Maven Pro';
}

.v-application a {
  color: #4a4a4a;
  text-align: center;
  font-weight: 500;
  font-size: 16px;
  /* border: 1px solid red; */
}

#logo {
  font-size: 30px;
  color: #f1d302;
}

#logo span {
  font-weight: bold;
}

.tile {
  margin: 0 10px 0 10px;
}
</style>
