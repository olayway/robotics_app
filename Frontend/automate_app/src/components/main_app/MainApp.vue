<template>
  <div class="main-app">
    <FilterNav
      :filters="availableFilters"
      @filter-results="updateFilters"
    ></FilterNav>
    <v-container id="filterResults">
      <v-row>
        <v-col v-for="(item, index) in useCases" :key="index" cols="12" md="6">
          <FilterCard :use-case="item"></FilterCard>
        </v-col>
      </v-row>
    </v-container>
    <PageNum :total="pagesCount" @page-change="updatePageNum"></PageNum>
  </div>
</template>

<script>
import { getUseCases } from '../../api'
import FilterNav from '../main_app/FilterNav'
import FilterCard from '../main_app/FilterCard'
import PageNum from '../base/PageNum'
export default {
  name: 'MainApp',
  components: { FilterNav, FilterCard, PageNum },
  data() {
    return {
      useCases: null,
      timeout: null,
      pagesCount: 1,
      currentPage: 1,
      appliedFilters: null,
      availableFilters: {}
    }
  },
  watch: {
    currentPage: {
      handler: 'filterResults'
    },
    appliedFilters: {
      handler: 'filterResults',
      deep: true
    }
  },
  created() {
    console.log('GET ALL')
    getUseCases()
      .then(response => {
        console.log(response.data)
        this.useCases = response.data.use_cases
        this.pagesCount = response.data.pages_count
        this.availableFilters = response.data.available_filters
      })
      .catch(error => console.log('ERROR', error))
  },
  methods: {
    updatePageNum(pageNum) {
      this.currentPage = pageNum
    },
    updateFilters(selections) {
      this.appliedFilters = selections
    },
    filterResults() {
      console.log('filtereerer', this.appliedFilters)
      clearTimeout(this.timeout)
      this.timeout = setTimeout(() => {
        getUseCases(this.appliedFilters, this.currentPage)
          .then(response => {
            console.log(response.data)
            this.useCases = response.data.use_cases
            this.pagesCount = response.data.pages_count
          })
          .catch(error => console.log(error))
      }, 1000)
    }
  }
}
</script>

<style scoped>
.main-app {
  background: linear-gradient(180deg, #464d78 0%, #0d0c1f 100%);
}
</style>
