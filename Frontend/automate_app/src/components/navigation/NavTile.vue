<template>
  <v-menu offset-y>
    <template v-slot:activator="{ on }">
      <a class="tile" v-on="on">{{ title }}</a>
    </template>

    <v-list elevation="0" v-if="subtitles.length > 0">
      <v-list-item
        v-for="(item, index) in subtitles"
        :key="index"
        @click.prevent
      >
        <v-list-item-title>{{ item }}</v-list-item-title>
      </v-list-item>
    </v-list>
  </v-menu>
</template>

<script>
export default {
  name: 'NavTile',
  props: {
    title: {
      type: String,
      required: true
    },
    subtitles: {
      type: Array
    }
  },
  data() {
    return {}
  }
}
</script>

<style scoped>
.v-menu__content {
  box-shadow: none;
}

.tile {
  margin: 0 10px 0 10px;
}

.v-application a {
  color: #4a4a4a;
  text-align: center;
  font-weight: 500;
  font-size: 16px;
  /* border: 1px solid red; */
}
</style>
