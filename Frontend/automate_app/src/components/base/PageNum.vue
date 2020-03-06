<template>
  <v-pagination v-model="page" :length="15" color="#F1D302" :total-visible="7" class="mb-6"></v-pagination>
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