<template>
  <div>
    <CaseTitleBar
      :image="caseData.images[0]"
      :thumbnail="caseData.thumbnail"
      :provider="caseData.provider"
      :basic-info="caseData.basic_info"
    ></CaseTitleBar>
    <ArticleSection
      v-for="(article, index) of caseData.content.article_sections"
      :key="index"
      :title="article.title"
      >{{ article.content.join() }}</ArticleSection
    >
  </div>
</template>

<script>
import { fetchUseCase } from '../api'
import CaseTitleBar from '@/components/applications/CaseTitleBar'
import ArticleSection from '@/components/applications/ArticleSection'

export default {
  name: 'UseCase',
  components: { CaseTitleBar, ArticleSection },
  data() {
    return {
      caseData: null
    }
  },
  watch: {
    $route() {
      this.getCaseData()
    }
  },
  created() {
    this.getCaseData()
  },
  methods: {
    getCaseData() {
      fetchUseCase(this.$route.params.id)
        .then(response => (this.caseData = response.data))
        .catch(error => console.log('Error fetching use-case data', error))
    }
  }
}
</script>
