<template>
  <v-img
    :src="imgSrc"
    :lazy-src="lazySrc"
    height="450"
    gradient="90deg, #141B30 0%, rgba(41, 52, 83, 0.85) 100%"
  >
    <v-container class="title-bar pa-0" fill-height fluid>
      <v-row align="center" justify="center">
        <v-col cols="8">
          <h1 class="title-title">{{ provider | capitalize }}</h1>
          <p class="title-text">Customer: {{ basicInfo.customer }}</p>
          <p class="title-text">Country: {{ basicInfo.country }}</p>
          <p class="title-text">Industry: {{ basicInfo.industry }}</p>
          <p class="title-text">Company size: {{ basicInfo.company_size }}</p>
          <p class="title-text">
            Applications: {{ basicInfo.applications.join(' | ') }}
          </p>
        </v-col>
      </v-row>
    </v-container>
  </v-img>
</template>

<script>
export default {
  name: 'CaseTitleBar',
  filters: {
    capitalize: value => {
      return value.toUpperCase()
    }
  },
  components: {},
  props: {
    image: {
      type: String,
      required: true
    },
    thumbnail: {
      type: String,
      required: true
    },
    provider: {
      type: String,
      required: true
    },
    basicInfo: {
      type: Object,
      required: true
    }
  },
  data() {
    return {
      imgSrc: 'data:image/jpg;base64,' + this.image,
      lazySrc: 'data:image/jpg;base64,' + this.thumbnail
    }
  }
}
</script>

<style scoped>
.title-bar * {
  /* border: 1px solid white; */
  color: white;
  font-family: Maven Pro;
}

.title-title {
  font-weight: bold;
  font-size: 40px;
  margin-bottom: 30px;
}

.title-text {
  font-size: 16px;
  line-height: 20px;
}
</style>
