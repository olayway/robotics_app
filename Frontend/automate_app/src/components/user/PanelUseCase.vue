<template>
  <v-card :class="[index % 2 !== 0 ? 'grey lighten-4' : '']" flat tile>
    <v-container pa-2 ma-0 fluid>
      <v-row no-gutters>
        <v-col align-self="start" cols="1">
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
        <v-col cols="3" class="column">{{
          useCase.content.article_title
        }}</v-col>
        <v-col cols="2" class="column">{{ useCase.basic_info.industry }}</v-col>
        <v-col cols="2" class="column">{{ useCase.basic_info.customer }}</v-col>
        <v-col cols="2" class="column">
          <ul>
            <li v-for="(item, i) in useCase.basic_info.applications" :key="i">
              {{ item }}
            </li>
          </ul>
        </v-col>
        <v-col cols="1" class="column">{{ useCase.status }}</v-col>
        <v-col cols="1" class="column">
          <v-row>
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
          </v-row>
        </v-col>
      </v-row>
    </v-container>
  </v-card>
</template>

<script>
// import ConfirmDialog from './ConfirmDialog.vue'
import { deleteUseCase, changeCaseStatus } from '@/api'
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
      const that = this
      const csrfAccess = window.$cookies.get('csrf_access_token')
      deleteUseCase(this.useCase.id, csrfAccess)
        .then(() => that.$store.dispatch('setUserUseCases'))
        .catch(error => console.log('Error deleting use case', error))
    },
    changeStatus(e, status) {
      const caseId = this.useCase.id
      const that = this
      const csrfAccess = window.$cookies.get('csrf_access_token')
      changeCaseStatus(caseId, status, csrfAccess)
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

.column {
  border-left: 1px solid rgb(211, 211, 211);
  padding: 0 14px;
}
</style>
