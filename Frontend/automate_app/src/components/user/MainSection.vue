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
      :value="getContent.article_sections[tabIndex].title"
      @input="
        setSectionData({
          userInput: { title: $event },
          tabIndex: tabIndex
        })
      "
    ></v-text-field>
    <label for="section_content">Section content:</label>
    <v-textarea
      background-color="white"
      color="indigo"
      hide-details
      outlined
      :value="getContent.article_sections[tabIndex].content"
      @input="
        setSectionData({
          userInput: { content: $event },
          tabIndex: tabIndex
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
    tabIndex: {
      type: String,
      required: true
    }
  },
  data() {
    return {}
  },
  computed: {
    ...mapGetters(['getContent'])
  },
  methods: {
    ...mapActions(['setSectionData', 'addNewSection'])
  }
}
</script>
