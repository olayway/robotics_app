<template>
  <v-pagination
    v-model="currentPage"
    :length="total"
    circle
    color="#F1D302"
    :total-visible="5"
    class="my-3"
  ></v-pagination>
</template>

<script>
export default {
  name: 'PageNav',
  props: {
    total: {
      type: Number,
      required: true
    }
  },
  data() {
    return {
      currentPage: 1
    }
  },
  watch: {
    currentPage: function(newValue) {
      this.$emit('page-change', newValue)
    }
  }
}
</script>

<style scoped></style>
