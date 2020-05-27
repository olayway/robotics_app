<template>
  <v-app>
    <NavBar
      v-if="[...userViews, ...loginViews].indexOf($route.name) == -1"
    ></NavBar>
    <UserNavBar v-else-if="userViews.indexOf($route.name) !== -1"></UserNavBar>
    <NavDrawer
      v-if="[...userViews, ...loginViews].indexOf($route.name) == -1"
    ></NavDrawer>
    <UserDrawer v-else-if="userViews.indexOf($route.name) !== -1"></UserDrawer>
    <v-content>
      <v-card class="content" min-height="500px" flat tile>
        <keep-alive :exclude="['NewUseCase', 'Register', 'Login']">
          <router-view :key="$route.fullPath"></router-view>
        </keep-alive>
      </v-card>
    </v-content>
    <SubsCard
      v-if="
        [...userViews, ...loginViews, 'NotFound'].indexOf($route.name) == -1
      "
    ></SubsCard>
    <PageFooter></PageFooter>
    <v-fade-transition>
      <v-overlay v-if="overlay" absolute color="#c4c4c4">
        <v-progress-circular indeterminate size="64"></v-progress-circular>
      </v-overlay>
    </v-fade-transition>
  </v-app>
</template>

<script>
import NavBar from '@/components/navigation/NavBar.vue'
import UserNavBar from '@/components/user/UserNavBar.vue'
import NavDrawer from '@/components/navigation/NavDrawer.vue'
import UserDrawer from '@/components/user/UserDrawer.vue'
import SubsCard from '@/components/base/SubsCard.vue'
import PageFooter from '@/components/base/PageFooter.vue'
import { EventBus } from '@/utils'

export default {
  name: 'App',

  components: {
    NavBar,
    UserNavBar,
    NavDrawer,
    UserDrawer,
    SubsCard,
    PageFooter
  },

  data() {
    return {
      userViews: ['UserPanel', 'NewUseCase', 'Settings'],
      loginViews: ['Login', 'Register'],
      overlay: false
    }
  },
  created() {
    const that = this
    EventBus.$on('toggle-overlay', value => (that.overlay = value))
    this.$store.dispatch('retrieveInterval')
  },
  methods: {}
}
</script>
