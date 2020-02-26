<template>
  <v-container style="border: 1px solid green" class="d-flex justify-end pa-0">
    <v-btn @click="$emit('toggle-drawer')" class="mx-2" fab dark small color="teal">
      <v-icon dark>mdi-format-list-bulleted-square</v-icon>
    </v-btn>
  </v-container>
</template>

<script>
export default {
  name: 'DrawerButton',
  data() {
    return {}
  }
}
</script>