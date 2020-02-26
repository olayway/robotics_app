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
        <v-col class="d-none d-md-block" md="6">
          <v-container
            style="border: 1px solid green"
            class="d-flex justify-center pa-0"
          >
            <v-menu
              v-for="(item, index) in navTiles"
              v-bind:key="index"
              offset-y
            >
              <template v-slot:activator="{ on }">
                <a class="tile" v-on="on">{{ item.title }}</a>
              </template>

              <v-list elevation="0" v-if="item.subtitles.length > 0">
                <v-list-item
                  v-for="(item, index) in item.subtitles"
                  :key="index"
                  @click.prevent
                >
                  <v-list-item-title>{{ item }}</v-list-item-title>
                </v-list-item>
              </v-list>
            </v-menu>
          </v-container>
        </v-col>

        <!-- Sign in and register buttons -->
        <v-col id="sign-in-up" md="3">
          <v-container
            style="border: 1px solid green"
            class="d-flex justify-end pa-0"
          >
            <a class="tile">Log In</a>
            <v-btn
              @click.prevent
              depressed
              small
              color="success"
              :ripple="false"
              class="tile register-button"
            >
              <a href="">Sign Up</a>
            </v-btn>
          </v-container>
        </v-col>
      </v-row>
    </v-container>
  </v-app-bar>
</template>

<script>
export default {
  name: 'NavBar',
  data() {
    return {
      navTiles: [
        { title: 'Home', subtitles: [] },
        { title: 'About', subtitles: [] },
        { title: 'Learn', subtitles: ['Tutorials', 'Articles', 'Courses'] },
        { title: 'Subscribe', subtitles: [] },
        { title: 'Contact', subtitles: [] }
      ]
    }
  },
  props: ['item']
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

.v-menu__content {
  box-shadow: none;
  border: 1px solid blue;
}

.tile {
  margin: 0 10px 0 10px;
}
</style>
