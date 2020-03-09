<template>
  <div>
    <CaseMain></CaseMain>
    <div>{{ case_data.data }}</div>
  </div>
</template>

<script>
import CaseMain from '@/components/applications/CaseMain'
export default {
  name: 'UseCase',
  components: { CaseMain },
  data() {
    return {
      case_data: null
    }
  },
  methods: {
    getCase() {
      const path = 'http://localhost:5000/test'
      this.axios
        .get(path)
        .then(res => {
          this.case_data = res
          console.log(res)
        })
        .catch(error => console.error(error))
    }
  },
  created() {
    this.getCase()
  }
}
</script>
