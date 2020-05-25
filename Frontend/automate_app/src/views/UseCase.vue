<template>
  <div>
    <CaseTitleBar
      :image="caseData.main_image"
      :thumbnail="caseData.main_thumbnail"
      :provider="caseData.provider"
      :basic-info="caseData.basic_info"
    ></CaseTitleBar>
    <v-container>
      <v-row justify="space-between">
        <v-col cols="8" class="pr-6">
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
              <PhotoGallery
                :images="[caseData.main_image, ...caseData.images]"
              ></PhotoGallery>
            </v-col>
          </v-row>
        </v-col>
        <v-col cols="4" class="pt-8 pl-8">
          <v-row>
            <v-col
              v-for="(item, index) in caseData.content.bullet_points"
              :key="index"
              cols="12"
              class="tile_contain"
            >
              <v-card class="pa-5 tile" flat tile>
                <p class="title_bp">{{ item.title }}</p>
                <div
                  v-if="caseData.provider === 'Universal Robots'"
                  v-html="item.content"
                ></div>
                <ul v-else>
                  <li v-for="(point, i) of item.content" :key="i">
                    {{ point }}
                  </li>
                </ul>
              </v-card>
            </v-col>
          </v-row>
        </v-col>
      </v-row>
    </v-container>
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
  font-size: 1rem;
  color: #4a4a4a;
}

.title {
  color: #3e5292;
  font-family: Maven Pro;
  font-size: 1.5rem !important;
}

.tile_contain {
  border-left: 1px solid rgb(216, 216, 216);
}

.tile * {
  font-size: 0.8rem;
}

.title_bp {
  color: #3e5292;
  font-size: 1.2rem;
  font-weight: 500;
}
</style>
