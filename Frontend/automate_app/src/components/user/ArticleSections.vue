<template>
  <div>
    <label for="article_sections">Article sections</label>
    <v-tabs
      v-model="currentTab"
      height="30px"
      hide-slider
      style="border-radius: 5px"
      show-arrows
      background-color="#3E5292"
      dark
      class="my-2"
    >
      <v-tab v-for="(section, index) in articleSections" :key="index"
        >Section {{ index + 1 }}</v-tab
      >
    </v-tabs>

    <v-tabs-items ref="tabs" v-model="currentTab">
      <v-tab-item v-for="(section, i) in articleSections" :key="i">
        <MainSection :tab-index="i.toString()"></MainSection>
      </v-tab-item>
    </v-tabs-items>

    <v-card-text>
      <v-btn outlined small color="green" @click="addNewSection"
        >Add section</v-btn
      >
      <v-divider vertical class="mx-2"></v-divider>
      <!-- TODO disable possibility to remove the only exisiting section -->
      <v-btn
        outlined
        small
        color="red"
        @click="deleteSection({ mouse: $event, tabIndex: currentTab })"
        >Remove section</v-btn
      >
      <v-divider vertical class="mx-2"></v-divider>
      <!-- TODO add reset functionality -->
      <v-btn
        outlined
        small
        color="grey"
        @click="deleteSection({ mouse: $event, tabIndex: currentTab })"
        >Reset</v-btn
      >
    </v-card-text>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
import { mapActions } from 'vuex'
import MainSection from '../user/MainSection.vue'
export default {
  name: 'ArticleSections',
  components: { MainSection },
  data() {
    return {
      currentTab: 0
    }
  },
  computed: {
    ...mapGetters(['getContent']),
    articleSections() {
      return this.getContent['article_sections']
    }
  },
  methods: {
    ...mapActions(['addNewSection', 'deleteSection'])
  }
}
</script>
