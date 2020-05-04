<template>
  <v-card :class="[index % 2 !== 0 ? 'grey lighten-4' : '']" flat tile>
    <v-container pa-2 ma-0>
      <v-row no-gutters>
        <v-col align-self="start">
          <v-row align="center" no-gutters>
            <v-checkbox
              color="indigo darken-4"
              :ripple="false"
              class="ma-0"
              hide-details
              dense
              v-model="selected"
            ></v-checkbox>
            <span class="content">{{ index }}</span>
          </v-row>
        </v-col>
        <v-divider vertical class="mx-2"></v-divider>
        <v-col>{{ useCase.title }}</v-col>
        <v-divider vertical class="mx-2"></v-divider>
        <v-col>{{ useCase.industry }}</v-col>
        <v-divider vertical class="mx-2"></v-divider>
        <v-col>{{ useCase.company }}</v-col>
        <v-divider vertical class="mx-2"></v-divider>
        <v-col>
          <ul>
            <li v-for="(item, index) in useCase.applications" :key="index">
              {{ item }}
            </li>
          </ul>
        </v-col>
        <v-divider vertical class="mx-2"></v-divider>
        <v-col>{{ useCase.status }}</v-col>
        <v-divider vertical class="mx-2"></v-divider>
        <v-col>
          <v-btn fab small icon color="red lighten-3">
            <v-icon>mdi-file-remove</v-icon>
          </v-btn>
          <v-btn fab small icon color="grey" depressed dark>
            <v-icon>mdi-file-cancel</v-icon>
          </v-btn>
          <v-btn fab small icon color="green lighten-2" depressed dark>
            <v-icon>mdi-file-check</v-icon>
          </v-btn>
          <v-btn fab small icon color="indigo accent-1" depressed dark>
            <v-icon>mdi-file-edit</v-icon>
          </v-btn>
        </v-col>
      </v-row>
    </v-container>
  </v-card>
</template>

<script>
export default {
  name: 'PanelUseCase',
  props: {
    useCase: Object,
    index: Number
  },
  data() {
    return {
      selected: false
    }
  }
}
</script>

<style scoped>
.content {
  text-align: center;
}
</style>
