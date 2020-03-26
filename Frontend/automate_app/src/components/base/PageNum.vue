<template>
  <v-pagination v-model="page" :length="5" circle color="#F1D302" :total-visible="3" class="mb-6"></v-pagination>
</template>

<script>
export default {
  name: 'PageNav',
  data() {
    return {
      page: 1
    }
  }
}
</script>

<style scoped>
</style>