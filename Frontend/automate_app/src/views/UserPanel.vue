<template>
  <div>
    <nav class="nav-bar">
      <div class="logo"></div>
    </nav>
  </div>
</template>

<script>
// import AutoMateLogo from '@/components/base/AutoMateLogo.vue'
export default {
  name: 'UserPanel',
  // components: { AutoMateLogo },
  data() {
    return {
      cases: []
    }
  }
}
</script>

<style scoped>
.logo {
  border: 1px solid rgb(139, 139, 139);
  width: 33px;
  height: 33px;
  border-radius: 50%;
  background-image: url('../assets/images/main_icon.svg');
  background-size: cover;
  background-position: center;
}

.nav-bar {
  background: linear-gradient(
    90deg,
    #122353 -0.2%,
    #122b6f -0.19%,
    #1a49cd 100%
  );
}
</style>>
  
