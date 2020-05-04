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
      <router-view></router-view>
    </v-content>
    <SubsCard
      v-if="[...userViews, ...loginViews].indexOf($route.name) == -1"
    ></SubsCard>
    <PageFooter></PageFooter>
  </v-app>
</template>

<script>
import NavBar from '@/components/navigation/NavBar.vue'
import UserNavBar from '@/components/user/UserNavBar.vue'
import NavDrawer from '@/components/navigation/NavDrawer.vue'
import UserDrawer from '@/components/user/UserDrawer.vue'
import SubsCard from '@/components/base/SubsCard.vue'
import PageFooter from '@/components/base/PageFooter.vue'

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
      loginViews: ['Login', 'Register']
    }
  },
  methods: {}
}
</script>
