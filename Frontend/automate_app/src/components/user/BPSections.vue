<template>
  <div>
    <label for="article_bullets">Article bullet-point sections</label>
    <v-tabs
      v-model="currentTab"
      height="30px"
      hide-slider
      style="border-radius: 5px"
      show-arrows
      background-color="#8C8C8C"
      dark
      class="my-2"
    >
      <v-tab v-for="(section, index) in bulletPointSections" :key="index"
        >Section {{ index + 1 }}</v-tab
      >
    </v-tabs>

    <v-tabs-items ref="tabs" v-model="currentTab">
      <v-tab-item v-for="(tab, i) in bulletPointSections" :key="i">
        <BulletPoints :tab-index="i.toString()"></BulletPoints>
      </v-tab-item>
    </v-tabs-items>

    <v-card-text>
      <v-btn outlined small color="green" @click="addNewSectionBP"
        >Add section</v-btn
      >
      <v-divider class="mx-2" vertical></v-divider>
      <v-btn
        outlined
        small
        color="red"
        @click="deleteSectionBP({ mouse: $event, tabIndex: currentTab })"
        >Remove section</v-btn
      >
      <v-divider class="mx-2" vertical></v-divider>
    </v-card-text>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
import { mapActions } from 'vuex'
import BulletPoints from './BulletPoints'
export default {
  name: 'BPSections',
  components: { BulletPoints },
  data() {
    return {
      currentTab: 0
    }
  },
  computed: {
    ...mapGetters(['getContent']),
    bulletPointSections() {
      return this.getContent['bullet_points']
    }
  },
  methods: {
    ...mapActions(['addNewSectionBP', 'deleteSectionBP'])
  }
}
</script>
