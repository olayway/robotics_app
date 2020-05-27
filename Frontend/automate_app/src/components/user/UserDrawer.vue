<template>
  <div>
    <v-navigation-drawer
      absolute
      style="margin-top: 55px"
      mini-variant
      permanent
    >
      <v-list dense>
        <v-list-item>
          <v-icon
            class="router-icon"
            color="grey lighten-1"
            @click="$router.push('/user-panel').catch(err => {})"
            >{{ 'mdi-view-dashboard' }}</v-icon
          >
        </v-list-item>
        <v-list-item>
          <v-icon
            class="router-icon"
            color="grey lighten-1"
            @click="
              $store.commit('resetUseCase')
              $router.push('/new-case').catch(err => {})
            "
            >{{ 'mdi-note-plus' }}</v-icon
          >
        </v-list-item>
        <v-list-item>
          <v-icon
            class="router-icon"
            color="grey lighten-1"
            @click="$router.push('/settings').catch(err => {})"
            >{{ 'mdi-settings' }}</v-icon
          >
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
    return {}
  }
}
</script>

<style scoped>
.router-icon {
  text-decoration: None;
}
</style>
