<template>
  <span>
    <td v-for="m, index in report" v-bind:key="index">
      {{ m }}
    </td>
  </span>
</template>

<script>
export default {
  name: 'activity-report',
  props: {
    monthly_report: {
      type: String,
      required: true
    }
  },
  data () {
    return {
      report: []
    }
  },
  mounted () {
    var vm = this
    // alert('vm.monthly_report:' + vm.monthly_report)
    if (vm.monthly_report !== null) {
      // alert('vm.monthly_report not null')
      vm.report = vm.monthly_report.split(',')
      // alert('vm.report:' + vm.report)
      // console.log('vm.report:' + vm.report)
      // alert('vm.monthly_report.length:' + vm.monthly_report.length)
      // vm.addMonthReportHeader(vm.monthly_report.length)
    }
  }
}
</script>
<style scoped>
</style>
