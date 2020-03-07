<template>
  <div>
    <p></p>
  </div>
</template>

<script>
export default {
  name: 'About',
  data() {
    return {
      cases: []
    }
  },
  methods: {
    getCases() {
      const path = 'http://localhost:5000/denmark'
      this.axios
        .get(path)
        .then(res => {
          this.cases = res
          // console.log(res)
        })
        .catch(error => {
          console.error(error)
        })
    }
  },
  created() {
    this.getCases()
  }
}
</script>
