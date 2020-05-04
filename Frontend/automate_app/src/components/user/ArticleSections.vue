<template>
  <div>
    <label for="article_sections">Article sections</label>
    <v-tabs
      v-model="current_tab"
      height="30px"
      hide-slider
      style="border-radius: 5px"
      show-arrows
      background-color="#3E5292"
      dark
      class="my-2"
    >
      <v-tab v-for="(n, index) in tabs" :key="n">Section {{ index + 1 }}</v-tab>
    </v-tabs>

    <v-tabs-items ref="tabs" v-model="current_tab">
      <v-tab-item v-for="n in tabs" :key="n">
        <MainSection></MainSection>
      </v-tab-item>
    </v-tabs-items>

    <v-card-text>
      <v-btn outlined small color="green" @click="addTab">Add section</v-btn>
      <v-divider vertical class="mx-2"></v-divider>
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
      tabs: [1],
      current_tab: null
    }
  },
  methods: {
    addTab() {
      this.tabs.push(this.tabs.length + 1)
    },
    deleteTab() {
      this.tabs.splice(this.current_tab, 1)
    }
  }
}
</script>
