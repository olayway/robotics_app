<template>
  <div>
    <v-container>
      <v-row justify="center">
        <div class="main-icon-title">
          <img src="@/assets/images/main_icon.svg" alt="automate-icon" />
          <p class="main-title">Find your Auto-Mate!</p>
        </div>
      </v-row>
      <v-row justify="center">
        <v-col md="8">
          <h1>Adapt a proven solution to your business</h1>
        </v-col>
      </v-row>
      <v-row justify="center">
        <v-col md="8">
          <p class="main-text top">
            Vitae eget placerat lorem aliquam consectetur ut enim cursus. Turpis
            tortor et, vel nisi faucibus nibh sollicitudin suspendisse. Aliquam
            sapien vel nisi faucibus nibh sollicitu dinaugue ipsum non.
          </p>
          <p class="main-text">
            Sit accumsan iaculis commodo dignissim scelerisque purus vitae cras
            vitae cras ac. Odio integer blandit at turpis ac sem pellentesque
            habitasse adipiscing. Vitae, varius vestibulum viverra tellus
            aliquam vestibulum ultrices hendrerit. Suspendisse vitae pulvinar
            pharetra, eleifend.
          </p>
        </v-col>
      </v-row>
      <v-row justify="center">
        <v-col sm="8" md="4">
          <SearchField></SearchField>
        </v-col>
      </v-row>
    </v-container>
    <MainApp></MainApp>
  </div>
</template>

<script>
import SearchField from '@/components/main_app/SearchField.vue'
import MainApp from '@/components/main_app/MainApp.vue'
export default {
  name: 'Home',
  components: { SearchField, MainApp }
}
</script>

<style scoped>
div * {
  border: 1px solid blue;
  font-family: Maven Pro;
  font-style: normal;
  font-weight: normal;
  font-size: 24px;
  color: #4a4a4a;
}

h1 {
  border: 1px solid red;
  font-size: 40px;
  color: #3e5292;
  text-align: center;
}

img {
  width: 81px;
}

.main-title {
  margin: 0 0 0 0;
}

.main-icon-title {
  display: flex;
  align-items: center;
}

.main-text {
  text-align: center;
  font-size: 16px;
  line-height: 23px;
  margin: 0 0 0 0;
}

.main-text.top {
  margin-bottom: 10px;
}
</style>
