<template>
  <v-container class="user-panel" fluid style="padding-left: 70px">
    <v-row no-gutters>
      <v-col class="pa-3 pa-md-6">
        <v-card tile class="elevation-3">
          <v-toolbar dark dense tile class="new-toolbar"
            >New use-case</v-toolbar
          >
          <v-tabs color="indigo darken-3" vertical>
            <v-tab> <v-icon left>mdi-home</v-icon>Step 1 </v-tab>
            <v-tab> <v-icon left>mdi-text</v-icon>Step 2 </v-tab>
            <v-tab> <v-icon left>mdi-image-plus</v-icon>Step 3 </v-tab>
            <!-- STEP 1 -->
            <v-tab-item>
              <StepOne></StepOne>
            </v-tab-item>
            <!-- STEP 2 -->
            <v-tab-item>
              <StepTwo></StepTwo>
            </v-tab-item>
            <!-- STEP 3 -->
            <v-tab-item>
              <StepThree></StepThree>
            </v-tab-item>
          </v-tabs>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import StepOne from '../components/user/StepOne.vue'
import StepTwo from '../components/user/StepTwo.vue'
import StepThree from '../components/user/StepThree.vue'
export default {
  name: 'UserPanel',
  components: { StepOne, StepTwo, StepThree },
  data() {
    return {}
  }
}
</script>

<style scoped>
.user-panel {
  font-family: Maven Pro;
}

.new-toolbar {
  background: linear-gradient(
    90deg,
    #122353 -0.2%,
    #122b6f -0.19%,
    #1a49cd 100%
  );
}

/* .step1-form >>> .v-input__slot {
  min-height: auto;
}

.step1-form >>> .v-input__append-inner {
  margin: auto;
}

.step1-form >>> input {
  padding: 0;
} */
</style>
