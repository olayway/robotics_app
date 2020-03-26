<template>
  <div>
    <v-navigation-drawer absolute style="margin-top: 55px" mini-variant permanent>
      <v-list dense>
        <v-list-item v-for="(nav, index) in navs" :key="index" link>
          <v-icon color="grey lighten-1">{{ nav.icon }}</v-icon>
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
        { title: 'All use-cases', icon: 'mdi-view-dashboard' },
        { title: 'New use-case', icon: 'mdi-note-plus' },
        { title: 'Settings', icon: 'mdi-settings' }
      ]
    }
  }
}
</script>

<style scoped>
</style>