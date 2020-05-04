<template>
  <v-toolbar id="filterNav" class="flex-row" color="#515E8A">
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
        v-for="(value, key) in filters"
        :label="key | capitalize"
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
  filters: {
    capitalize: value => {
      return value.charAt(0).toUpperCase() + value.slice(1)
    }
  },
  created() {
    window.addEventListener('scroll', this.handleScroll)
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
  }
}
</script>

<style scoped></style>

// :style="fixedFilterNav ? filterNavStyle : ''"
