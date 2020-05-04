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
                  <span>Title</span>
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
          <PanelUseCase
            v-for="(item, index) in useCases"
            :key="index"
            :useCase="item"
            :index="index"
          ></PanelUseCase>
        </v-card>
      </v-col>
    </v-row>
    <v-row class="px-3 px-md-6" no-gutters>
      <v-col align="start">
        <v-pagination
          class="page-num"
          v-model="page"
          :length="3"
          color="indigo darken-4"
          circle
        ></v-pagination>
      </v-col>
      <v-col align="end">
        <v-btn
          class="delete-button elevation-2"
          rounded
          color="red lighten-1"
          dark
          >Delete</v-btn
        >
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import PanelUseCase from '../components/user/PanelUseCase.vue'
import { getUserUseCases } from '../api'

export default {
  name: 'UserPanel',
  components: { PanelUseCase },
  data() {
    return {
      useCases: [],
      selected: [],
      page: 1
    }
  },
  mounted() {
    getUserUseCases()
      .then(response => {
        this.useCases = response.data.your_use_cases
      })
      .catch(error => console.log("Error fetching user's use cases:", error))
  }
}
</script>

<style scoped>
.user-panel {
  font-family: Maven Pro;
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
