<template>
  <v-card flat tile color="grey lighten-5">
    <v-container class="pa-4">
      <v-row>
        <v-col lg="8">
          <p class="tab-title">Upload Images</p>
          <v-divider class="my-5"></v-divider>
          <v-form v-model="valid">
            <p>Main image:</p>
            <v-file-input
              ref="mainImage"
              :rules="[rules.size]"
              accept="image/*"
              show-size
              counter
              chips
              clearable
              :value="getMainImage"
              @change="uploadMainImage"
            ></v-file-input>
            <v-card class="my-4" min-height="10rem">
              <v-container>
                <v-row>
                  <v-col cols="3">
                    <v-img
                      v-if="mainPreview"
                      contain
                      height="8rem"
                      :src="mainPreview"
                    ></v-img>
                  </v-col>
                </v-row>
              </v-container>
            </v-card>
            <p for="other_photos">Other images:</p>
            <v-file-input
              ref="images"
              :value="getImages"
              :rules="[rules.arraySize, rules.arrayLimit]"
              accept="image/*"
              multiple
              show-size
              counter
              chips
              clearable
              @change="uploadImage"
            ></v-file-input>
            <v-card class="my-4" min-height="10rem">
              <v-container>
                <v-row>
                  <v-col
                    v-for="(url, index) of otherPreview"
                    :key="index"
                    cols="3"
                  >
                    <v-img contain :src="url" height="8rem"></v-img>
                  </v-col>
                </v-row>
              </v-container>
            </v-card>
          </v-form>
          <p v-if="warn" class="red--text">
            Not all required fields are correctly filled in.
          </p>
          <v-btn
            class="save-button my-3"
            outlined
            color="green lighten-1"
            @click="
              validateSteps()
              save()
            "
            >Save</v-btn
          >
          <v-btn
            class="reset-button my-3 ml-3"
            outlined
            color="orange lighten-1"
            @click="discard"
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
import { mapGetters } from 'vuex'
import { EventBus } from '@/utils'
export default {
  name: 'StepThree',
  components: {},
  data() {
    return {
      warn: false,
      allValid: false,
      valid: false,
      mainUrl: null,
      otherUrls: null,
      rules: {
        size: value =>
          !value ||
          value.size < 150000 ||
          'Image size should be less than 150 kB!',
        arraySize: array =>
          array.every(value => value.size < 150000) ||
          'Image size should be less than 150 kB!',
        arrayLimit: array => array.length <= 5 || 'Max 5 images'
      }
    }
  },
  computed: {
    ...mapGetters(['getMainImage', 'getImages']),
    mainPreview() {
      return this.getMainImage ? URL.createObjectURL(this.getMainImage) : null
    },
    otherPreview() {
      const images = this.getImages
      return images ? images.map(file => URL.createObjectURL(file)) : []
    }
  },
  created() {
    const that = this
    EventBus.$on('valid-check', value => {
      that.allValid = value
      that.warn = !value
    })
  },
  methods: {
    ...mapActions(['uploadMainImage', 'uploadImage']),
    validateSteps() {
      EventBus.$emit('validate')
    },
    save() {
      console.log('asdfasdfdf')
      if (this.allValid) {
        EventBus.$emit('toggle-overlay', true)
        const useCaseData = this.$store.state.case.useCaseData
        const companyName = this.$store.state.user.userData.companyName
        const useCaseId = this.$store.state.case.useCaseId
        const csrfAccess = window.$cookies.get('csrf_access_token')
        saveUseCase(
          { ...useCaseData, provider: companyName },
          useCaseId,
          csrfAccess
        )
          .then(response => {
            console.log(response)
            EventBus.$emit('toggle-overlay', false)
            this.$store.commit('resetUseCase')
            this.$store.dispatch('setUserUseCases')
            this.$router.push('/user-panel')
          })
          .catch(error => console.log(error))
      } else {
        console.log('invalid')
      }
    },
    discard() {
      this.$store.commit('resetUseCase')
      this.$router.push('/user-panel')
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
