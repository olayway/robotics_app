<template>
  <v-card flat color="grey lighten-5">
    <v-container class="pa-4">
      <v-row>
        <v-col lg="8">
          <p class="tab-title">Basic Information</p>
          <v-divider></v-divider>
        </v-col>
      </v-row>
      <v-row>
        <v-col lg="8">
          <v-form class="step1-form" ref="form">
            <label for="company_name">Company name</label>
            <v-text-field
              id="company_name"
              color="indigo"
              background-color="white"
              outlined
              dense
              counter="15"
              v-model="userInput.company"
              :rules="[rules.counter, rules.required]"
            ></v-text-field>
            <label for="company_size">Company size</label>
            <v-select
              id="company_size"
              color="indigo"
              background-color="white"
              outlined
              dense
              v-model="userInput.company_size"
              :items="inputOptions.company_size"
              :rules="[rules.required]"
            ></v-select>
            <label for="country">Country</label>
            <v-select
              id="country"
              color="indigo"
              background-color="white"
              outlined
              dense
              v-model="userInput.country"
              :items="inputOptions.country"
              :rules="[rules.required]"
            ></v-select>
            <label for="industry">Industry</label>
            <v-select
              id="industry"
              color="indigo"
              background-color="white"
              outlined
              dense
              v-model="userInput.industry"
              :items="inputOptions.industry"
              :rules="[rules.required]"
            ></v-select>
            <label for="applications">Applications</label>
            <v-select
              id="applications"
              color="indigo"
              background-color="white"
              outlined
              clearable
              v-model="userInput.applications"
              :items="inputOptions.applications"
              :rules="[rules.required]"
              multiple
              dense
              persistent-hint
            ></v-select>
            <v-btn class="save-button my-3" outlined color="green lighten-1"
              >Save</v-btn
            >
            <v-btn
              class="reset-button my-3 ml-3"
              outlined
              color="orange lighten-1"
              >Reset</v-btn
            >
          </v-form>
        </v-col>
      </v-row>
    </v-container>
  </v-card>
</template>

<script>
export default {
  name: 'StepOne',
  data() {
    return {
      userInput: {
        company: '',
        company_size: '',
        country: '',
        industry: '',
        applications: []
      },
      inputOptions: {
        company_size: ['< 1k', '1-5k', '5-20k', '20-50k', '50-100k', '> 100k'],
        country: ['Poland', 'Germany', 'Sweden', 'USA'],
        industry: [
          'Automotive',
          'Food & Beverages',
          'Agriculture',
          'Manufacturing'
        ],
        applications: [
          'Welding',
          'Packaging',
          'Machine Tending',
          'Pick & Place'
        ]
      },
      rules: {
        counter: value => value.length <= 15 || 'Max 15 characters',
        required: value => !!value || 'This field is required'
      }
    }
  },
  methods: {
    saveUserInput() {
      const { userInput } = this
      console.log(userInput)
      this.$store.dispatch('saveUserInput', userInput)
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
