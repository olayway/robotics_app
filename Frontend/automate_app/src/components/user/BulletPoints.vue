<template>
  <v-card flat tile color="grey lighten-5" class="my-3">
    <label for="section_title">Section title:</label>
    <v-text-field
      v-model="section_title"
      color="indigo"
      background-color="white"
      outlined
      dense
      hide-details
      class="mb-2"
    ></v-text-field>
    <label for="section_bulletpoints">Section bullet points:</label>
    <v-text-field
      v-for="n in 3"
      :key="n"
      v-model="section_bulletpoints"
      :label="n.toString()"
      color="indigo"
      hide-details
    ></v-text-field>
  </v-card>
</template>

<script>
export default {
  name: 'BulletPoints',
  data() {
    return {
      section_title: null,
      section_bulletpoints: null
    }
  }
}
</script>
