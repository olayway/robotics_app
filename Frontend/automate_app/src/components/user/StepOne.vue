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
          <v-form ref="form" class="step1-form">
            <label for="company_name">Company name</label>
            <v-text-field
              id="company"
              color="indigo"
              background-color="white"
              outlined
              dense
              counter="15"
              :rules="[rules.counter, rules.required]"
              :value="getBasicInfo.customer"
              @input="setBasicInfo({ customer: $event })"
            ></v-text-field>
            <label for="company_size">Company size</label>
            <v-select
              id="company_size"
              color="indigo"
              background-color="white"
              outlined
              dense
              :items="inputOptions.company_size"
              :rules="[rules.required]"
              :value="getBasicInfo.company_size"
              @input="setBasicInfo({ company_size: $event })"
            ></v-select>
            <label for="country">Country</label>
            <v-select
              id="country"
              color="indigo"
              background-color="white"
              outlined
              dense
              :items="inputOptions.country"
              :rules="[rules.required]"
              :value="getBasicInfo.country"
              @input="setBasicInfo({ country: $event })"
            ></v-select>
            <label for="industry">Industry</label>
            <v-select
              id="industry"
              color="indigo"
              background-color="white"
              outlined
              dense
              :items="inputOptions.industry"
              :rules="[rules.required]"
              :value="getBasicInfo.industry"
              @input="setBasicInfo({ industry: $event })"
            ></v-select>
            <label for="applications">Applications</label>
            <v-select
              id="applications"
              color="indigo"
              background-color="white"
              outlined
              clearable
              multiple
              dense
              persistent-hint
              :items="inputOptions.applications"
              :rules="[rules.required]"
              :value="getBasicInfo.applications"
              @input="setBasicInfo({ applications: $event })"
            ></v-select>
          </v-form>
        </v-col>
      </v-row>
    </v-container>
  </v-card>
</template>

<script>
import { mapActions } from 'vuex'
import { mapGetters } from 'vuex'
export default {
  name: 'StepOne',
  data() {
    return {
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
  computed: {
    ...mapGetters(['getBasicInfo'])
  },
  methods: {
    ...mapActions(['setBasicInfo'])
  }
}
</script>

<style scoped>
.tab-title {
  font-size: 25px;
  color: #3e5292;
}
</style>
