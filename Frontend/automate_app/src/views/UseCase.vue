<template>
  <div>
    <CaseTitleBar
      :image="caseData.images[0]"
      :thumbnail="caseData.thumbnail"
      :provider="caseData.provider"
      :basic-info="caseData.basic_info"
    ></CaseTitleBar>
    <div class="py-12">
      <ArticleSection
        v-for="(article, index) of caseData.content.article_sections"
        :key="index"
      >
        <template v-slot:header>
          <p class="title mt-6">
            {{ article.title.toLowerCase() | capitalize }}
          </p>
        </template>
        <template v-slot:content>
          <div
            v-if="caseData.provider === 'Universal Robots'"
            class="content"
            v-html="article.content"
          ></div>
          <p v-else class="content">{{ article.content }}</p>
        </template>
      </ArticleSection>
      <v-row justify="center">
        <v-col cols="8" class="pa-0">
          <PhotoGallery :images="caseData.images"></PhotoGallery>
        </v-col>
      </v-row>
    </div>
  </div>
</template>

<script>
import { fetchUseCase } from '../api'
import CaseTitleBar from '@/components/applications/CaseTitleBar'
import ArticleSection from '@/components/applications/ArticleSection'
import PhotoGallery from '@/components/applications/PhotoGallery'

export default {
  name: 'UseCase',
  filters: {
    capitalize: value => {
      return value.charAt(0).toUpperCase() + value.slice(1)
    }
  },
  components: { CaseTitleBar, ArticleSection, PhotoGallery },
  data() {
    return {
      caseData: null
    }
  },
  watch: {
    $route: 'getUseCaseData'
  },
  created() {
    this.getCaseData()
  },
  methods: {
    getCaseData() {
      fetchUseCase(this.$route.params.id)
        .then(response => {
          this.caseData = response.data
        })
        .catch(error => console.log('Error fetching use-case data', error))
    }
  }
}
</script>

<style scoped>
* {
  font-family: Maven Pro;
  font-size: 16px;
  color: #4a4a4a;
}

.title {
  color: #3e5292;
  font-family: Maven Pro;
  font-size: 30px !important;
}
</style>
