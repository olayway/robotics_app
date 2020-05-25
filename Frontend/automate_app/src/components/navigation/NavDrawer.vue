<template>
  <v-navigation-drawer
    v-model="drawer"
    class="pa-6"
    width="auto"
    right
    floating
    temporary
    fixed
  >
    <v-list dense nav class="py-0">
      <v-list-item link>
        <v-list-item-content>
          <v-list-item-title
            ><router-link class="drawer-link" to="/"
              >Home</router-link
            ></v-list-item-title
          >
        </v-list-item-content>
      </v-list-item>
      <v-list-item link>
        <v-list-item-content>
          <v-list-item-title
            ><router-link class="drawer-link" to="/login"
              >Login</router-link
            ></v-list-item-title
          >
        </v-list-item-content>
      </v-list-item>
      <v-list-item link>
        <v-list-item-content>
          <v-list-item-title
            ><router-link class="drawer-link" to="/register"
              >Register</router-link
            ></v-list-item-title
          >
        </v-list-item-content>
      </v-list-item>

      <!-- <v-list-group v-else v-model="listOpen" no-action>
          <template v-slot:activator>
            <v-list-item-content>
              <v-list-item-title v-text="item.title"></v-list-item-title>
            </v-list-item-content>
          </template>
          <v-list-item v-for="(s, i) in item.subtitles" :key="i" @click.prevent>
            <v-list-item-title v-text="s"></v-list-item-title>
          </v-list-item>
        </v-list-group> -->
    </v-list>
  </v-navigation-drawer>
</template>

<script>
import { EventBus } from '../../utils/index'
// import { mapGetters } from 'vuex'

export default {
  name: 'NavDrawer',
  data() {
    return {
      listOpen: false,
      drawer: false
    }
  },
  computed: {
    // ...mapGetters(['getNavTiles'])
  },
  mounted() {
    const that = this
    EventBus.$on('open-drawer', () => (that.drawer = true))
  },
  methods: {
    collapseList() {
      this.listOpen = false
    }
  }
}
</script>

<style scoped>
a.drawer-link {
  font-family: Maven Pro;
  font-size: 1rem;
  font-weight: 300;
  color: #4a4a4a;
  text-decoration: none;
}
</style>
