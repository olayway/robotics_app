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
      :value="BPSectionData.title"
      @input="
        setSectionDataBP({
          userInput: { title: $event },
          tabIndex: tabIndex
        })
      "
    ></v-text-field>
    <label for="section_bulletpoints">Section bullet points:</label>
    <v-text-field
      v-for="(n, i) in BPSectionData.content"
      :key="i"
      :label="(i + 1).toString()"
      color="indigo"
      hide-details
      :value="BPSectionData.content[i]"
      @input="
        setSectionDataBP({
          userInput: { content: { text: $event, pointNo: i } },
          tabIndex: tabIndex
        })
      "
    ></v-text-field>
  </v-card>
</template>

<script>
import { mapGetters } from 'vuex'
import { mapActions } from 'vuex'
export default {
  name: 'BulletPoints',
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
    ...mapGetters(['getContent']),
    BPSectionData() {
      return this.getContent.bullet_points[this.tabIndex]
    }
  },
  methods: {
    ...mapActions(['setSectionDataBP', 'addNewSectionBP'])
  }
}
</script>
