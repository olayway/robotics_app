<template>
  <v-text-field
    hide-details
    rounded
    class="search-field"
    :placeholder="placeholder"
    append-icon="mdi-magnify"
    clear-icon="mdi-close-circle"
    clearable
    outlined
    dense
    type="text"
    color="yellow"
    single-line
  ></v-text-field>
</template>

<script>
export default {
  name: 'SearchFiled',
  data() {
    return {
      placeholder: 'Search for industries, processes, companies...'
    }
  }
}
</script>

<style scoped>
.search-field {
  font-size: 14px;
}
</style>
