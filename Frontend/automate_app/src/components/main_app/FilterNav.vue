<template>
  <v-toolbar id="filterNav" height="auto" color="#515E8A">
    <!-- cache-items? -->
    <v-container pa-0>
      <v-row align="stretch" justify="center">
        <v-col
          v-for="(value, key) in filters"
          :key="key"
          class="pa-0"
          cols="4"
          lg="2"
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
            :label="key | capitalize"
            :items="value"
            background-color="#6976A4"
            @blur="$emit('filter-results', selections)"
          >
            <template v-slot:selection="{ item, index }">
              <span v-if="index === 0" class="select mr-7 mb-0">{{
                item | truncate(strLength)
              }}</span>
              <span v-if="index === 1" class="select-count grey--text"
                >(+{{ selections[key].length - 1 }} others)</span
              >
            </template>
          </v-select>
        </v-col>
      </v-row>
    </v-container>
  </v-toolbar>
</template>

<script>
export default {
  name: 'FilterNav',
  filters: {
    capitalize: value => {
      return value.charAt(0).toUpperCase() + value.slice(1)
    },
    truncate: (str, len) => {
      return str.length > len ? str.slice(0, len) + '...' : str
    }
  },
  props: {
    filters: {
      type: Object,
      required: true
    }
  },
  data() {
    return {
      selections: {}
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
  computed: {
    strLength() {
      let len
      switch (this.$vuetify.breakpoint.name) {
        case 'xs':
          len = 5
          break
        case 'sm':
          len = 10
          break
        case 'md':
          len = 15
          break
        case 'lg':
          len = 10
          break
        case 'xl':
          len = 15
          break
      }
      return len
    }
  },
  methods: {}
  // watch: {
  //   filterResultsPosition: function(value) {
  //     let navHeight = document
  //       .querySelector('#filterNav')
  //       .getBoundingClientRect().height
  //     if (value < navHeight) {
  //       this.fixedFilterNav = true
  //     } else {
  //       this.fixedFilterNav = false
  //     }
  //   }
  // },
  // created() {
  //   window.addEventListener('scroll', this.handleScroll)
  // },
  // destroyed() {
  //   window.removeEventListener('scroll', this.handleScroll)
  // },
  // methods: {
  // handleScroll() {
  //   this.filterNavPosition = document
  //     .querySelector('#filterNav')
  //     .getBoundingClientRect().top
  //   this.filterResultsPosition = document
  //     .querySelector('#filterResults')
  //     .getBoundingClientRect().top
  //   console.log('FILTER', this.filterNavPosition)
  //   console.log('RESULTS', this.filterResultsPosition)
  //   console.log(
  //     'FILTERHEIGHT',
  //     document.querySelector('#filterNav').getBoundingClientRect().height
  //   )
  // }
  // }
}
</script>

<style scoped>
.disabled {
  pointer-events: none;
  color: #bfcbd9;
  cursor: not-allowed;
  background-image: none;
  background-color: #eef1f6;
  border-color: #d1dbe5;
}
.select {
  font-size: 12px;
}

.select-count {
  font-size: 11px;
}
</style>
