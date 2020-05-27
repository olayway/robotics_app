<template>
  <v-container class="user-panel" fluid style="padding-left: 70px">
    <v-row no-gutters>
      <v-col class="pa-3 pa-md-6">
        <p class="panel-title">Your use-cases</p>
        <v-card flat>
          <v-toolbar dark height="auto" dense flat class="panel-toolbar">
            <v-container pa-2 ma-0 fluid>
              <v-row no-gutters>
                <v-col cols="1">
                  <v-row no-gutters>
                    <v-checkbox hide-details dense></v-checkbox>
                    <span>Id</span>
                  </v-row>
                </v-col>
                <v-col cols="3">
                  <span class="column">Title</span>
                </v-col>
                <v-col>
                  <span class="column" cols="2">Industry</span>
                </v-col>
                <v-col cols="2">
                  <span class="column">Company</span>
                </v-col>
                <v-col cols="2">
                  <span class="column">Applications</span>
                </v-col>
                <v-col cols="1">
                  <span class="column">Status</span>
                </v-col>
                <v-col cols="1">
                  <span class="column">Options</span>
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
      viewCases: 10,
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
  }
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

.column {
  border-left: 1px solid rgb(114, 114, 114);
  padding: 0 14px;
}
</style>
