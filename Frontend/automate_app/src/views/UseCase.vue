<template>
  <div>
    <CaseTitleBar
      :image="caseData.main_image"
      :thumbnail="caseData.main_thumbnail"
      :provider="caseData.provider"
      :basic-info="caseData.basic_info"
    ></CaseTitleBar>
    <v-container pa-10>
      <v-row justify="space-between">
        <v-col cols="8" class="pr-6">
          <h1 v-if="caseData.content.article_title" class="article_title mb-2">
            {{ caseData.content.article_title }}
          </h1>
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
          <PhotoGallery
            :images="[caseData.main_image, ...caseData.images]"
          ></PhotoGallery>
        </v-col>
        <v-col cols="4" class="pl-8">
          <v-row>
            <v-col
              v-for="(item, index) in caseData.content.bullet_points"
              :key="index"
              cols="12"
              class="tile_contain pl-4"
            >
              <v-card class="pb-5 pl-5 tile" flat tile>
                <p class="title_bp">
                  {{ item.title.toLowerCase() | capitalize }}
                </p>
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
import { EventBus } from '@/utils'
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
  // watch: {
  //   $route: 'getUseCaseData'
  // },
  created() {
    EventBus.$emit('toggle-overlay', true)
    this.getCaseData()
  },
  methods: {
    getCaseData() {
      fetchUseCase(this.$route.params.id)
        .then(response => {
          this.caseData = response.data
          this.$nextTick(() => EventBus.$emit('toggle-overlay', false))
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
  text-align: justify;
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
  text-align: initial;
}

.title_bp {
  color: #3e5292;
  font-size: 1.2rem;
  font-weight: 500;
}

.article_title {
  text-align: initial;
  font-size: 2rem;
  font-weight: 500;
  color: #3e5292;
}
</style>
