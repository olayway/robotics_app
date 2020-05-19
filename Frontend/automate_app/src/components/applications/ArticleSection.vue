<template>
  <v-container fill-height fluid>
    <v-row align="center" justify="center">
      <v-col cols="10">
        <h2>{{ title | capitalize }}</h2>
        <slot></slot>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  name: 'CaseContent',
  filters: {
    capitalize: value => {
      return value.toUpperCase()
    }
  },
  components: {},
  props: {
    title: {
      type: String,
      required: true
    }
  },
  data() {
    return {}
  }
}
</script>

<style scoped>
.title-bar * {
  /* border: 1px solid white; */
  color: white;
  font-family: Maven Pro;
}
</style>
