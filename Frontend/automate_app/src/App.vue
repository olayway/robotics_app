<template>
  <v-app>
    <NavBar v-if="['Login', 'Register', 'UserPanel'].indexOf($route.name)==-1"></NavBar>
    <NavDrawer></NavDrawer>
    <v-content>
      <router-view></router-view>
    </v-content>
    <SubsCard v-if="['Login', 'Register', 'UserPanel'].indexOf($route.name)==-1"></SubsCard>
    <PageFooter></PageFooter>
  </v-app>
</template>

<script>
import NavBar from '@/components/navigation/NavBar.vue'
import NavDrawer from '@/components/navigation/NavDrawer.vue'
import SubsCard from '@/components/base/SubsCard.vue'
import PageFooter from '@/components/base/PageFooter.vue'

export default {
  name: 'App',

  components: { NavBar, NavDrawer, SubsCard, PageFooter },

  data() {
    return
  },
  methods: {}
}
</script>


