<template>
  <v-hover>
    <template v-slot:default="{ hover }">
      <v-card
        class="filter-card pa-5 d-flex"
        dark
        color="#293453"
        @click="$router.push({ name: 'UseCase', params: { id: useCase.id } })"
      >
        <v-container pa-0>
          <v-row no-gutters>
            <v-col cols="12" md="6" class="d-flex flex-column">
              <v-img
                :src="'data:image/jpg;base64,' + useCase.main_image"
                :lazy="'data:image/jpg;base64,' + useCase.main_thumbnail"
                ><template v-slot:placeholder>
                  <v-row
                    class="fill-height ma-0"
                    align="center"
                    justify="center"
                  >
                    <v-progress-circular
                      indeterminate
                      color="grey lighten-5"
                    ></v-progress-circular>
                  </v-row>
                </template>
              </v-img>
            </v-col>
            <v-col cols="12" md="6" class="mt-2 mt-md-0 d-flex flex-column">
              <div>
                <p style="text-align: bottom" class="provider mb-0 ml-md-4">
                  {{ useCase.provider.toUpperCase() }}
                </p>
                <v-divider class="my-2 ml-md-4"></v-divider>
                <p class="customer mb-0 ml-md-4">
                  Customer: {{ useCase.basic_info.customer | capitalize }}
                </p>
                <p class="industry mb-2 ml-md-4">
                  Industry: {{ useCase.basic_info.industry | capitalize }}
                </p>
              </div>
              <div>
                <p class="applications mb-0 ml-md-4">
                  {{ useCase.basic_info.applications.join(' | ') | capitalize }}
                </p>
              </div>
            </v-col>
          </v-row>
        </v-container>
        <v-fade-transition>
          <v-overlay
            v-if="hover"
            opacity="0.65"
            class="card-overlay"
            absolute
            z-index="1"
            color="#8294bf"
          >
            <v-btn color="#1d263d" dark>See more info</v-btn>
          </v-overlay>
        </v-fade-transition>
      </v-card>
    </template>
  </v-hover>
</template>

<script>
export default {
  name: 'FilterCard',
  filters: {
    capitalize: value => {
      const array = value.split(' ')
      const arrayUpper = array.map(
        item => item.charAt(0).toUpperCase() + item.slice(1)
      )
      return arrayUpper.join(' ')
    }
  },
  props: {
    useCase: {
      type: Object,
      required: true
    }
  },
  data() {
    return {}
  },
  computed: {}
}
</script>

<style scoped>
/* img {
  width: 100%;
  height: auto;
} */

.filter-card * {
  /* border: 1px solid white; */
  font-family: Maven Pro;
  font-style: normal;
  font-weight: normal;
}

.provider {
  font-size: 1.5rem;
}

.customer {
  font-size: 0.9rem;
}

.industry {
  font-size: 0.9rem;
  color: #f1d302;
}

.applications {
  font-size: 0.7rem;
}
</style>
