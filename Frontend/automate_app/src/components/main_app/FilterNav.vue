<template>
  <v-toolbar id="filterNav" height="auto" color="#515E8A">
    <!-- cache-items? -->
    <v-container pa-0>
      <v-row align="center">
        <v-col
          v-for="(value, key) in filters"
          :key="key"
          class="pa-0"
          cols="6"
          sm="3"
        >
          <v-select
            v-model="selections[key]"
            class="ma-2"
            hide-details
            solo
            clearable
            flat
            item-color="#515E8A"
            multiple
            dark
            background-color="#6976A4"
            :label="key | capitalize"
            :items="value.map(item => item.toUpperCase())"
            @change="$emit('filter-results', selections)"
          >
            <template v-slot:selection="{ item, index }">
              <span v-if="index === 0" class="select">{{
                item | truncate
              }}</span>
              <span v-if="index === 1" class="select-count grey--text">
                (+{{ selections[key].length - 1 }} others)</span
              >
            </template>
          </v-select></v-col
        >
      </v-row>
    </v-container>
  </v-toolbar>
</template>

<script>
import { getFilters } from '../../api'
export default {
  name: 'FilterNav',
  filters: {
    capitalize: value => {
      return value.charAt(0).toUpperCase() + value.slice(1)
    },
    truncate: str => {
      console.log(this.axios)
      let len
      switch (this.$vuetify.breakpoint.name) {
        case 'xs':
        case 'sm':
          len = 6
          break
        case 'md':
        case 'lg':
        case 'xl':
          len = 12
          break
      }
      return str.length > len ? str.slice(0, len) + '...' : str
    }
  },
  data() {
    return {
      filters: null,
      selections: {
        country: null,
        industry: null,
        application: null,
        company: null
      }
      // filterNavStyle: {
      //   position: 'fixed',
      //   top: '0',
      //   left: '0',
      //   width: '100%',
      //   'z-index': '1'
      // },
      // fixedFilterNav: false,
      // filterNavPosition: null,
      // filterResultsPosition: null
    }
  },
  watch: {
    filterResultsPosition: function(value) {
      let navHeight = document
        .querySelector('#filterNav')
        .getBoundingClientRect().height
      if (value < navHeight) {
        this.fixedFilterNav = true
      } else {
        this.fixedFilterNav = false
      }
    }
  },
  created() {
    window.addEventListener('scroll', this.handleScroll)
    getFilters(this.selections)
      .then(response => {
        this.filters = response.data
      })
      .catch(error => console.log(error))
  },
  destroyed() {
    window.removeEventListener('scroll', this.handleScroll)
  },
  methods: {
    handleScroll() {
      this.filterNavPosition = document
        .querySelector('#filterNav')
        .getBoundingClientRect().top
      this.filterResultsPosition = document
        .querySelector('#filterResults')
        .getBoundingClientRect().top
      // console.log('FILTER', this.filterNavPosition)
      // console.log('RESULTS', this.filterResultsPosition)
      // console.log(
      //   'FILTERHEIGHT',
      //   document.querySelector('#filterNav').getBoundingClientRect().height
      // )
    }
  }
}
</script>

<style scoped>
.select {
  margin-right: 7px;
}

.select-count {
  font-size: 11px;
}
</style>
