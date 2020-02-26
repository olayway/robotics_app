<template>
  <v-app-bar absolute elevate-on-scroll>
    <v-container id="nav-bar" class="pa-0" style="border: 1px solid black">
      <v-row no-gutters class="align-center">
        <!-- Logo -->
        <v-col md="3">
          <v-container style="border: 1px solid red" class="pa-0">
            <div id="logo" class="tile" style="border: 1px solid green">
              <span>auto</span>mate
            </div>
          </v-container>
        </v-col>

        <!-- Main Navigation Buttons -->
        <v-col class="d-none d-lg-block" md="6">
          <v-container style="border: 1px solid green" class="d-flex justify-center pa-0">
            <NavTile
              v-for="(item, index) in navTiles"
              :key="index"
              :title="item.title"
              :subtitles="item.subtitles"
            ></NavTile>
          </v-container>
        </v-col>

        <!-- Sign in and register buttons -->
        <v-col id="sign-in-up" style="border: 1px solid blue">
          <component @toggle-drawer="drawer = !drawer" :is="navigation"></component>
        </v-col>
      </v-row>
    </v-container>
  </v-app-bar>
</template>

<script>
import NavTile from './NavTile.vue'
import SignInUp from './SignInUp.vue'
import DrawerButton from './DrawerButton.vue'

export default {
  name: 'NavBar',
  components: { NavTile, SignInUp, DrawerButton },
  data() {
    return {
      navTiles: [
        { title: 'Home', subtitles: [] },
        { title: 'About', subtitles: [] },
        { title: 'Learn', subtitles: ['Tutorials', 'Articles', 'Courses'] },
        { title: 'Subscribe', subtitles: [] },
        { title: 'Contact', subtitles: [] }
      ],
      drawer: false
    }
  },
  computed: {
    navigation() {
      if (['xs', 'sm', 'md'].includes(this.$vuetify.breakpoint.name)) {
        return DrawerButton
      } else {
        return SignInUp
      }
    }
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
  border: 1px solid red;
}

#logo {
  font-size: 30px;
  color: #f1d302;
}

#logo span {
  font-weight: bold;
}

.register-button a {
  color: white;
  text-decoration: none;
  text-transform: initial;
}

.tile {
  margin: 0 10px 0 10px;
}
</style>
