<template>
  <v-card :class="[index % 2 !== 0 ? 'grey lighten-4' : '']" flat tile>
    <v-container pa-2 ma-0>
      <v-row no-gutters>
        <v-col align-self="start">
          <v-row align="center" no-gutters>
            <v-checkbox
              v-model="selected"
              color="indigo darken-4"
              :ripple="false"
              class="ma-0"
              hide-details
              dense
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
            <li v-for="(item, i) in useCase.applications" :key="i">
              {{ item }}
            </li>
          </ul>
        </v-col>
        <v-divider vertical class="mx-2"></v-divider>
        <v-col>{{ useCase.status }}</v-col>
        <v-divider vertical class="mx-2"></v-divider>
        <v-col>
          <v-btn fab x-small icon color="red lighten-3" @click="remove">
            <v-icon>mdi-file-remove</v-icon>
          </v-btn>

          <v-btn fab x-small icon color="grey" depressed dark>
            <v-icon>mdi-file-cancel</v-icon>
          </v-btn>
          <v-btn fab x-small icon color="green lighten-2" depressed dark>
            <v-icon>mdi-file-check</v-icon>
          </v-btn>
          <v-btn fab x-small icon color="indigo accent-1" depressed dark>
            <v-icon>mdi-file-edit</v-icon>
          </v-btn>
        </v-col>
      </v-row>
    </v-container>
  </v-card>
</template>

<script>
// import ConfirmDialog from './ConfirmDialog.vue'
import { deleteUseCase } from '../../api'
export default {
  name: 'PanelUseCase',
  // components: { ConfirmDialog },
  props: {
    useCase: {
      type: Object,
      required: true
    },
    index: {
      type: Number,
      required: true
    }
  },
  data() {
    return {
      selected: false
    }
  },
  methods: {
    remove() {
      console.log('deleetiiiiing')
      const csrfAccess = window.$cookies.get('csrf_access_token')
      deleteUseCase(this.useCase.id, csrfAccess)
        .then(response => console.log(response.data))
        .catch(error => console.log('Error deleting use case', error))
    }
  }
}
</script>

<style scoped>
.content {
  text-align: center;
}
</style>
