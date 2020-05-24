<template>
  <v-card flat tile>
    <v-dialog v-model="dialog" width="80%">
      <v-img
        :src="'data:image/jpg;base64,' + selectedImage"
        @click.stop="dialog = false"
      ></v-img>
    </v-dialog>
    <v-container fluid>
      <v-row>
        <v-col
          v-for="(image, index) of images"
          :key="index"
          class="d-flex child-flex"
          cols="12"
          sm="6"
          lg="4"
        >
          <v-card flat tile class="d-flex">
            <v-img
              :src="'data:image/jpg;base64,' + image"
              class="grey lighten-2 image"
              @click.stop="zoomImage($event, image)"
            >
              <template v-slot:placeholder>
                <v-row class="fill-height ma-0" align="center" justify="center">
                  <v-progress-circular
                    indeterminate
                    color="grey lighten-5"
                  ></v-progress-circular>
                </v-row>
              </template>
            </v-img>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
  </v-card>
</template>

<script>
export default {
  name: 'PhotoGallery',
  props: {
    images: {
      type: Array,
      required: true
    }
  },
  data() {
    return {
      selectedImage: null,
      dialog: false
    }
  },
  methods: {
    zoomImage(_, image) {
      this.selectedImage = image
      this.dialog = true
    }
  }
}
</script>

<style scoped>
.image {
  cursor: pointer;
}
</style>
