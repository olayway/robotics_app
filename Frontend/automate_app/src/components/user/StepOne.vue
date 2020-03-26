<template>
  <v-card flat color="grey lighten-5">
    <v-container class="pa-4">
      <v-row>
        <v-col lg="8">
          <p class="tab-title">Basic Information</p>
          <v-divider></v-divider>
          <v-form class="step1-form" ref="form">
            <label for="company_name">Company name</label>
            <v-text-field
              id="company_name"
              color="indigo"
              background-color="white"
              outlined
              dense
              hide-details
              v-model="tags.company_name"
              class="mb-2"
            ></v-text-field>
            <label for="company_size">Company size</label>
            <v-select
              id="company_size"
              color="indigo"
              background-color="white"
              outlined
              dense
              hide-details
              v-model="tags.company_size"
              class="mb-2"
            ></v-select>
            <label for="country">Country</label>
            <v-select
              id="country"
              color="indigo"
              background-color="white"
              outlined
              dense
              hide-details
              v-model="tags.country"
              class="mb-2"
            ></v-select>
            <label for="industry">Industry</label>
            <v-select
              id="industry"
              color="indigo"
              background-color="white"
              outlined
              dense
              hide-details
              v-model="tags.industry"
              class="mb-2"
            ></v-select>
            <label for="applications">Applications</label>
            <v-select
              id="applications"
              color="indigo"
              background-color="white"
              outlined
              v-model="tags.applications"
              multiple
              dense
              hint="select"
              persistent-hint
              class="mb-2"
            ></v-select>
            <v-btn class="reset-button my-3" outlined color="orange lighten-1">Reset</v-btn>
          </v-form>
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