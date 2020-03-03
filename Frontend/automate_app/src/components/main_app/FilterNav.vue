<template>
  <v-toolbar class="filter-nav flex-row" color="#515E8A">
    <!-- cache-items? -->
    <v-container class="d-flex flex-row">
      <v-select
        class="ma-2"
        hide-details
        solo
        dense
        clearable
        flat
        item-color="#515E8A"
        multiple
        dark
        background-color="#6976A4"
        :label="key | capitalize"
        v-for="(value, key) in filters"
        :key="key"
        :items="value"
      ></v-select>
    </v-container>
  </v-toolbar>
</template>

<script>
export default {
  name: 'FilterNav',
  data() {
    return {
      filters: {
        company: ['Milka', 'Wedel', 'Terravita'],
        industry: ['Food & Beverages', 'Automotive', 'Electronics'],
        country: ['Poland', 'USA', 'Germany'],
        application: ['welding', 'packaging', 'painting', 'cutting', 'assembly']
      }
    }
  },
  filters: {
    capitalize: value => {
      return value.charAt(0).toUpperCase() + value.slice(1)
    }
  }
}
</script>

<style scoped>
</style>