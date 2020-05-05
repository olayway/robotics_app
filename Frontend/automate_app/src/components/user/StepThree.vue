<template>
  <v-card flat color="grey lighten-5">
    <v-container class="pa-4">
      <v-row>
        <v-col lg="6">
          <p class="tab-title">Upload Images</p>
          <v-divider></v-divider>
          <label for="main_photo">Main photo:</label>
          <v-file-input chips></v-file-input>
          <label for="other_photos">Other photos:</label>
          <v-file-input multiple chips></v-file-input>
          <v-btn class="save-button my-3" outlined color="green lighten-1"
            >Save</v-btn
          >
          <v-btn
            class="reset-button my-3 ml-3"
            outlined
            color="orange lighten-1"
            >Reset</v-btn
          >
        </v-col>
      </v-row>
    </v-container>
  </v-card>
</template>

<script>
export default {
  name: 'StepOne',
  data() {}
}
</script>

<style scoped>
.tab-title {
  font-size: 25px;
  color: #3e5292;
}
</style>
