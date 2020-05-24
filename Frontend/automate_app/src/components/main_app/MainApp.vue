<template>
  <div>
    <FilterNav
      :filters="availableFilters"
      @filter-results="updateFilters"
    ></FilterNav>
    <v-card tile flat class="main-app" min-height="15rem">
      <v-container>
        <v-row justify="start">
          <v-col
            v-for="(item, index) in useCases"
            :key="index"
            class="d-flex"
            cols="12"
            sm="6"
            height="100px"
          >
            <FilterCard :use-case="item"></FilterCard>
          </v-col>
        </v-row>
        <v-row>
          <PageNum
            v-if="pagesCount"
            :total="pagesCount"
            @page-change="updatePageNum"
          ></PageNum>
        </v-row>
      </v-container>

      <v-fade-transition>
        <v-overlay v-if="overlay" absolute color="#1d263d">
          <v-progress-circular indeterminate size="64"></v-progress-circular>
        </v-overlay>
      </v-fade-transition>
    </v-card>
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
      overlay: true,
      timeout: null,
      pagesCount: null,
      currentPage: 1,
      appliedFilters: null,
      availableFilters: {
        application: [],
        country: [],
        customer: [],
        industry: [],
        provider: []
      }
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
    getUseCases()
      .then(response => {
        this.useCases = response.data.use_cases
        this.pagesCount = response.data.pages_count
        this.availableFilters = response.data.available_filters
        this.overlay = false
      })
      .catch(error => console.log('ERROR', error))
  },
  methods: {
    updatePageNum(pageNum) {
      this.currentPage = pageNum
    },
    updateFilters(selections) {
      console.log('updateFilters')
      this.currentPage = 1
      this.appliedFilters = selections
    },
    filterResults() {
      this.overlay = true
      clearTimeout(this.timeout)
      this.timeout = setTimeout(() => {
        getUseCases(this.appliedFilters, this.currentPage)
          .then(response => {
            this.useCases = response.data.use_cases
            this.pagesCount = response.data.pages_count
            this.availableFilters = response.data.available_filters
            this.overlay = false
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
