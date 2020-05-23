<template>
  <div>
    <router-link to="/" class="logo" :style="{ fontSize: fontSize }">
      <span>auto</span>mate
    </router-link>
  </div>
</template>

<script>
export default {
  name: 'AutoMateLogo',
  props: {
    fontSize: {
      type: String,
      required: true
    }
  },
  data() {
    return {}
  }
}
</script>

<style scoped>
.logo {
  color: #f1d302;
  display: inline-block;
  text-decoration: none;
}

.logo span {
  font-weight: bold;
}
</style>
