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
        <v-col>{{ useCase.basic_info.country }}</v-col>
        <v-divider vertical class="mx-2"></v-divider>
        <v-col>{{ useCase.basic_info.industry }}</v-col>
        <v-divider vertical class="mx-2"></v-divider>
        <v-col>{{ useCase.basic_info.customer }}</v-col>
        <v-divider vertical class="mx-2"></v-divider>
        <v-col>
          <ul>
            <li v-for="(item, i) in useCase.basic_info.applications" :key="i">
              {{ item }}
            </li>
          </ul>
        </v-col>
        <v-divider vertical class="mx-2"></v-divider>
        <v-col>{{ useCase.status }}</v-col>
        <v-divider vertical class="mx-2"></v-divider>
        <v-col>
          <v-btn
            :ripple="false"
            fab
            x-small
            icon
            color="red lighten-3"
            @click="remove"
          >
            <v-icon>mdi-file-remove</v-icon>
          </v-btn>

          <v-btn
            :ripple="false"
            fab
            x-small
            icon
            color="grey lighten-1"
            depressed
            dark
            @click="changeStatus($event, 'inactive')"
          >
            <v-icon>mdi-file-cancel</v-icon>
          </v-btn>
          <v-btn
            :ripple="false"
            fab
            x-small
            icon
            color="green lighten-2"
            depressed
            dark
            @click="changeStatus($event, 'active')"
          >
            <v-icon>mdi-file-check</v-icon>
          </v-btn>
          <v-btn
            :ripple="false"
            fab
            x-small
            icon
            color="indigo accent-1"
            depressed
            dark
            @click="edit"
          >
            <v-icon>mdi-file-edit</v-icon>
          </v-btn>
          <v-btn
            :ripple="false"
            fab
            x-small
            icon
            color="orange lighten-3"
            depressed
            dark
            @click="
              $router.push({ name: 'UseCase', params: { id: useCase.id } })
            "
          >
            <v-icon>mdi-file-eye</v-icon>
          </v-btn>
        </v-col>
      </v-row>
    </v-container>
  </v-card>
</template>

<script>
// import ConfirmDialog from './ConfirmDialog.vue'
import { deleteUseCase, changeCaseStatus } from '../../api'
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
      const that = this
      const csrfAccess = window.$cookies.get('csrf_access_token')
      deleteUseCase(this.useCase.id, csrfAccess)
        .then(response => console.log(response.data))
        .then(() => that.$store.dispatch('setUserUseCases'))
        .catch(error => console.log('Error deleting use case', error))
    },
    changeStatus(e, status) {
      console.log('changing status to:', status)
      const caseId = this.useCase.id
      const that = this
      const csrfAccess = window.$cookies.get('csrf_access_token')
      changeCaseStatus(caseId, status, csrfAccess)
        .then(response => console.log(response))
        .then(() => that.$store.dispatch('setUserUseCases'))
        .catch(error => console.log('Error changing status', error))
    },
    edit() {
      const caseId = this.useCase.id
      this.$store.dispatch('fetchForUpdate', caseId)
    }
  }
}
</script>

<style scoped>
.content {
  text-align: center;
}
</style>
