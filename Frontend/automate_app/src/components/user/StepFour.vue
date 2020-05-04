<template>
  <v-card flat color="grey lighten-5">
    <v-container class="pa-4">
      <v-row>
        <v-col lg="6">
          <p class="tab-title">Preview & Save</p>
          <v-divider></v-divider>
          <v-btn color="green" rounded class="white--text my-4">Save</v-btn>
          <v-btn color="red" rounded class="white--text my-4 ml-2"
            >Discard</v-btn
          >
        </v-col>
      </v-row>
      <v-row>
        <v-col cols="12" lg="8"></v-col>
      </v-row>
    </v-container>
  </v-card>
</template>

<script>
export default {
  name: 'StepOne',
  data() {
    return {
      tags: {
        company_name: null,
        company_size: null,
        country: null,
        industry: null,
        applications: []
      }
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
