<template>
  <div class="main-app">
    <FilterNav></FilterNav>
    <FilterResults></FilterResults>
    <PageNum></PageNum>
  </div>
</template>

<script>
import FilterNav from '../main_app/FilterNav'
import FilterResults from '../main_app/FilterResults'
import PageNum from '../base/PageNum'
export default {
  name: 'MainApp',
  components: { FilterNav, FilterResults, PageNum },
  data() {
    return {}
  }
}
</script>

<style scoped>
.main-app {
  background: linear-gradient(180deg, #464d78 0%, #0d0c1f 100%);
}
</style>
