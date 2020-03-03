<template>
  <v-navigation-drawer
    class="pa-2"
    temporary
    floating
    right
    stateless
    v-model="drawerState"
    absolute
    v-click-outside="toggleDrawer"
  >
    <v-list dense nav class="py-0">
      <v-container v-for="(item, index) in navTiles" :key="index">
        <v-list-item v-if="!item.subtitles.length" link>
          <v-list-item-content>
            <v-list-item-title>{{ item.title }}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>

        <v-list-group v-model="listOpen" v-else no-action>
          <template v-slot:activator>
            <v-list-item-content>
              <v-list-item-title v-text="item.title"></v-list-item-title>
            </v-list-item-content>
          </template>
          <v-list-item v-for="(s, i) in item.subtitles" :key="i" @click.prevent>
            <v-list-item-title v-text="s"></v-list-item-title>
          </v-list-item>
        </v-list-group>
      </v-container>
    </v-list>
  </v-navigation-drawer>
</template>

<script>
import { mapGetters } from 'vuex'
import { mapActions } from 'vuex'

export default {
  name: 'NavDrawer',
  data() {
    return {
      listOpen: false
    }
  },
  computed: {
    ...mapGetters(['navTiles', 'drawerState'])
  },
  methods: {
    ...mapActions(['toggleDrawer'])
  },
  collapseList() {
    this.listOpen = false
  }
}
</script>
