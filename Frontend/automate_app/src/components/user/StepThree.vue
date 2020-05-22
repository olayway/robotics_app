<template>
  <v-card flat color="grey lighten-5">
    <v-container class="pa-4">
      <v-row>
        <v-col lg="6">
          <p class="tab-title">Upload Images</p>
          <v-divider></v-divider>
          <label for="main_photo">Main photo:</label>
          <v-file-input
            accept="image/*"
            show-size
            counter
            chips
            clearable
            @change="uploadMainImage"
          ></v-file-input>
          <label for="other_photos">Other photos:</label>
          <v-file-input
            accept="image/*"
            multiple
            show-size
            counter
            chips
            clearable
            @change="uploadImage"
          ></v-file-input>
          <v-btn
            class="save-button my-3"
            outlined
            color="green lighten-1"
            @click="save"
            >Save</v-btn
          >
          <v-btn
            class="reset-button my-3 ml-3"
            outlined
            color="orange lighten-1"
            >Discard</v-btn
          >
        </v-col>
      </v-row>
    </v-container>
  </v-card>
</template>

<script>
import { saveUseCase } from '../../api'
import { mapActions } from 'vuex'
export default {
  name: 'StepThree',
  data() {
    return {}
  },
  methods: {
    ...mapActions(['uploadMainImage', 'uploadImage']),
    save() {
      const useCaseData = this.$store.state.useCaseData
      const companyName = this.$store.state.userData.companyName
      const csrfAccess = window.$cookies.get('csrf_access_token')
      saveUseCase({ ...useCaseData, provider: companyName }, csrfAccess).then(
        response => {
          console.log(response)
          this.$router.push('/user-panel')
        }
      )
    }
  }
}
</script>

<style scoped>
.tab-title {
  font-size: 25px;
  color: #3e5292;
}
</style>
