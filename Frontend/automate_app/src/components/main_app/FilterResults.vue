<template>
  <v-container id="filterResults">
    <v-row>
      <v-col cols="12" md="6" v-for="n in 9" :key="n">
        <FilterCard></FilterCard>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import FilterCard from '../main_app/FilterCard'
export default {
  name: 'FilterResults',
  components: { FilterCard },
  data() {
    return {}
  }
}
</script>
