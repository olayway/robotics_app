<template>
  <v-row align="center" justify="center">
    <v-col class="py-0">
      <slot name="header"></slot>
      <slot name="content"></slot>
    </v-col>
  </v-row>
</template>

<script>
export default {
  name: 'CaseContent',
  data() {
    return {}
  }
}
</script>

<style scoped></style>
