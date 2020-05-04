<template>
  <div>
    <v-navigation-drawer
      absolute
      style="margin-top: 55px"
      mini-variant
      permanent
    >
      <v-list dense>
        <v-list-item v-for="(nav, index) in navs" :key="index" link>
          <router-link :to="nav.link" class="router-icon">
            <v-icon color="grey lighten-1">{{ nav.icon }}</v-icon>
          </router-link>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>
  </div>
</template>

<script>
export default {
  name: 'UserDrawer',
  components: {},
  data() {
    return {
      navs: [
        {
          title: 'All use-cases',
          icon: 'mdi-view-dashboard',
          link: '/user-panel'
        },
        { title: 'New use-case', icon: 'mdi-note-plus', link: '/new-case' },
        { title: 'Settings', icon: 'mdi-settings', link: '/settings' }
      ]
    }
  }
}
</script>

<style scoped>
.router-icon {
  text-decoration: None;
}
</style>
