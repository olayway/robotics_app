<template>
  <v-card flat tile color="grey lighten-5">
    <v-container class="pa-4">
      <v-row>
        <v-col lg="8">
          <p class="tab-title">Article Content</p>
          <v-divider class="my-5"></v-divider>
          <label for="article_title">Article title</label>
          <v-text-field
            id="article_title"
            color="indigo"
            background-color="white"
            outlined
            dense
            :value="getContent.article_title"
            @input="setArticleTitle"
          ></v-text-field>
          <v-divider class="mt-2 mb-6"></v-divider>
          <!-- ARTICLE SECTIONS -->
          <ArticleSections></ArticleSections>
          <!-- ARTICLE BULLET POINT SECTIONS -->
          <BPSections></BPSections>
        </v-col>
      </v-row>
    </v-container>
  </v-card>
</template>

<script>
import { mapGetters } from 'vuex'
import { mapActions } from 'vuex'
import ArticleSections from './ArticleSections'
import BPSections from './BPSections'
export default {
  name: 'StepTwo',
  components: { ArticleSections, BPSections },
  data() {
    return {}
  },
  computed: {
    ...mapGetters(['getContent'])
  },
  methods: {
    ...mapActions(['setArticleTitle', 'addNewSection'])
  }
}
</script>

<style scoped>
.tab-title {
  font-size: 25px;
  color: #3e5292;
}
</style>
