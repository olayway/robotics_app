<template>
  <v-container class="user-panel" fluid style="padding-left: 70px">
    <v-row no-gutters>
      <v-col class="pa-3 pa-md-6">
        <p class="panel-title">Your use-cases</p>
        <v-card flat>
          <v-toolbar dark height="auto" dense flat class="panel-toolbar">
            <v-container pa-2 ma-0>
              <v-row no-gutters>
                <v-col>
                  <v-row no-gutters>
                    <v-checkbox hide-details dense></v-checkbox>
                    <span>Id</span>
                  </v-row>
                </v-col>
                <v-divider vertical class="mx-2"></v-divider>
                <v-col>
                  <span>Country</span>
                </v-col>
                <v-divider vertical class="mx-2"></v-divider>
                <v-col>
                  <span>Industry</span>
                </v-col>
                <v-divider vertical class="mx-2"></v-divider>
                <v-col>
                  <span>Company</span>
                </v-col>
                <v-divider vertical class="mx-2"></v-divider>
                <v-col>
                  <span>Applications</span>
                </v-col>
                <v-divider vertical class="mx-2"></v-divider>
                <v-col>
                  <span>Status</span>
                </v-col>
                <v-divider vertical class="mx-2"></v-divider>
                <v-col>
                  <span>Options</span>
                </v-col>
              </v-row>
            </v-container>
          </v-toolbar>
          <v-card flat tile>
            <PanelUseCase
              v-for="(item, index) in useCases"
              :key="index"
              :use-case="item"
              :index="index + 1 + (currentPage - 1) * viewCases"
            ></PanelUseCase>
          </v-card>
        </v-card>
      </v-col>
    </v-row>
    <v-row class="px-3 px-md-6" no-gutters>
      <v-col align="start">
        <v-pagination
          v-model="currentPage"
          class="page-num"
          :length="pages"
          color="indigo darken-4"
          circle
        ></v-pagination>
      </v-col>
      <v-col align="end">
        <v-btn
          class="delete-button elevation-2"
          rounded
          color="red lighten-1 white--text"
          :disabled="bulk"
          >Delete</v-btn
        >
      </v-col>
    </v-row>
    <v-fade-transition>
      <v-overlay v-if="overlay" absolute color="#575c63">
        <v-progress-circular indeterminate size="40"></v-progress-circular>
      </v-overlay>
    </v-fade-transition>
  </v-container>
</template>

<script>
// import Bus from '../utils'
import PanelUseCase from '../components/user/PanelUseCase.vue'
import { mapGetters } from 'vuex'

export default {
  name: 'UserPanel',
  components: { PanelUseCase },
  data() {
    return {
      selected: [],
      currentPage: 1,
      viewCases: 5,
      overlay: false,
      bulk: false
    }
  },
  computed: {
    ...mapGetters(['getUserUseCases']),
    casesCount() {
      return this.getUserUseCases().length
    },
    pages() {
      return Math.ceil(this.casesCount / this.viewCases)
    },
    useCases() {
      const max_index = this.currentPage * this.viewCases
      const min_index = max_index - this.viewCases
      if (max_index < this.casesCount) {
        return this.getUserUseCases(min_index, max_index)
      } else {
        return this.getUserUseCases(min_index)
      }
    }
  },
  // created() {
  //   Bus.$on('overlay-on', function() {
  //     this.overlay = true
  //   })
  //   Bus.$on('overlay-off', function() {
  //     this.overlay = false
  //   })
  // },
  methods: {}
}
</script>

<style scoped>
.user-panel {
  font-family: Maven Pro;
  font-size: 14px;
}

.panel-title {
  color: #3e5292;
  font-size: 18px;
  font-weight: bold;
}

.panel-toolbar {
  background: linear-gradient(
    90deg,
    #122353 -0.2%,
    #122b6f -0.19%,
    #1a49cd 100%
  );
  border-radius: 4px;
}

.panel-toolbar >>> div {
  padding: 0;
}

.delete-button {
  text-transform: initial;
}

ul.page-num {
  justify-content: start;
}
</style>
