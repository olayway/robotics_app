<template>
  <v-app-bar app height="55px" class="nav-bar" tile flat>
    <v-app-bar-nav-icon>
      <v-img height="40px" width="40px" src="@/assets/images/main_icon.svg"></v-img>
    </v-app-bar-nav-icon>
    <!-- <v-divider class="divider" dark vertical></v-divider> -->
    <div>
      <v-text-field
        filled
        dark
        dense
        class="search-field ml-4"
        hide-details
        rounded
        placeholder="Lookup use-case"
        append-icon="mdi-magnify"
        type="text"
        single-line
      ></v-text-field>
    </div>
    <OutlinedButton class="ml-4">Advanced Search</OutlinedButton>
    <v-spacer></v-spacer>
    <!-- <v-divider class="divider" dark vertical></v-divider> -->
    <v-btn
      class="logout"
      height="35px"
      width="35px"
      dark
      fab
      depressed
      color="rgba(213, 213, 213, 0.26)"
      @click="logout"
    >
      <v-icon>mdi-power</v-icon>
    </v-btn>
  </v-app-bar>
</template>

<script>
import OutlinedButton from '@/components/base/OutlinedButton.vue'
export default {
  name: 'UserNavBar',
  components: { OutlinedButton },
  data() {
    return {}
  },
  methods: {
    logout() {
      this.$store.dispatch('logout').then(() => this.$router.push('/login'))
    }
  }
}
</script>

<style scoped>
.nav-bar {
  background: linear-gradient(
    90deg,
    #122353 -0.2%,
    #122b6f -0.18%,
    #1a49cd 122.44%
  );
}
.search-field {
  font-family: Maven Pro;
  font-size: 16px;
  margin: 0 10px;
}

.search-field >>> .v-input__slot {
  box-shadow: inset 4px 4px 6px rgba(0, 0, 0, 0.15);
  /* min-height: 0 !important; */
}

/* .search-field >>> .v-input__control .v-input__append-inner {
  margin: auto !important;
} */

.divider {
  height: 10px;
  margin: 10px;
}

#user-panel-container {
  padding: 0;
}
</style>