<template>
  <v-card flat color="grey lighten-5">
    <v-container class="pa-4">
      <v-row>
        <v-col>
          <p class="tab-title">Article Content</p>
          <v-divider></v-divider>
        </v-col>
      </v-row>
      <v-row>
        <v-col lg="8">
          <label for="article_title">Article title</label>
          <v-text-field
            id="article_title"
            color="indigo"
            background-color="white"
            outlined
            dense
            v-model="article_title"
          ></v-text-field>
          <v-divider class="my-5"></v-divider>

          <!-- ARTICLE SECTIONS -->
          <ArticleSections></ArticleSections>
          <!-- ARTICLE BULLET POINT SECTIONS -->
          <BPSections></BPSections>
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
import ArticleSections from './ArticleSections'
import BPSections from './BPSections'
export default {
  name: 'StepTwo',
  components: { ArticleSections, BPSections },
  data() {
    return {
      article_title: ''
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
