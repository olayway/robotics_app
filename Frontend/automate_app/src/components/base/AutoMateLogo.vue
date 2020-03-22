<template>
  <div id="logo" :style="{fontSize: fontSize}">
    <span>auto</span>mate
  </div>
</template>

<script>
export default {
  name: 'AutoMateLogo',
  props: ['fontSize'],
  data() {
    return {}
  }
}
</script>

<style scoped>
#logo {
  color: #f1d302;
  display: inline-block;
}

#logo span {
  font-weight: bold;
}
</style>