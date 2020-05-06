<template>
  <v-card flat tile color="grey lighten-5" class="my-3">
    <label for="section_title">Section title:</label>
    <v-text-field
      color="indigo"
      background-color="white"
      outlined
      dense
      hide-details
      class="mb-2"
      :value="getUseCaseData.content.article_sections[tabId].title"
      @input="
        setSectionData({
          userInput: { title: $event },
          sectionId: tabId
        })
      "
    ></v-text-field>
    <label for="section_content">Section content:</label>
    <v-textarea
      background-color="white"
      color="indigo"
      hide-details
      outlined
      :value="getUseCaseData.content.article_sections[tabId].content"
      @input="
        setSectionData({
          userInput: { title: $event },
          sectionId: tabId
        })
      "
    ></v-textarea>
  </v-card>
</template>

<script>
import { mapGetters } from 'vuex'
import { mapActions } from 'vuex'
export default {
  name: 'MainSection',
  props: {
    tabId: {
      type: String,
      required: true
    }
  },
  data() {
    return {
      tabData: {
        tabId: this.tabId,
        title: '',
        content: ''
      }
    }
  },
  computed: {
    ...mapGetters(['getUseCaseData'])
  },
  created() {
    this.setBasicInfo()
  },
  methods: {
    ...mapActions(['setSectionData'])
  }
}
</script>
