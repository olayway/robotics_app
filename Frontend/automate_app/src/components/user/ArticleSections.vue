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
      <v-tab v-for="(uid, index) in tabs" :key="uid"
        >Section {{ index + 1 }}</v-tab
      >
    </v-tabs>

    <v-tabs-items ref="tabs" v-model="currentTab">
      <v-tab-item v-for="uid in tabs" :key="uid">
        <MainSection :tab-id="uid"></MainSection>
      </v-tab-item>
    </v-tabs-items>

    <v-card-text>
      <v-btn outlined small color="green" @click="addTab">Add section</v-btn>
      <v-divider vertical class="mx-2"></v-divider>
      <!-- TODO disable possibility to remove the only exisiting section -->
      <v-btn outlined small color="red" @click="deleteTab"
        >Remove section</v-btn
      >
      <v-divider vertical class="mx-2"></v-divider>
      <v-btn outlined small color="grey" @click="deleteTab">Reset</v-btn>
    </v-card-text>
  </div>
</template>

<script>
import MainSection from '../user/MainSection.vue'
export default {
  name: 'ArticleSections',
  components: { MainSection },
  data() {
    return {
      tabs: [],
      currentTab: ''
    }
  },
  created() {
    const baseTabUid = this.generateUid()
    this.tabs.push(baseTabUid)
    this.currentTab = baseTabUid
  },
  methods: {}
}
</script>
