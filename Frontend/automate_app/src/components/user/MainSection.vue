<template>
  <v-card flat tile color="grey lighten-5" class="my-3">
    <label for="section_title">Section title:</label>
    <v-text-field
      id="section_title"
      color="indigo"
      background-color="white"
      outlined
      dense
      hide-details
      class="mb-2"
      v-model="section_title"
    ></v-text-field>
    <label for="section_content">Section content:</label>
    <v-textarea
      background-color="white"
      color="indigo"
      hide-details
      outlined
      v-model="section_content"
    ></v-textarea>
  </v-card>
</template>

<script>
export default {
  name: 'MainSection',
  data() {
    return {
      section_title: '',
      section_content: ''
    }
  }
}
</script>
