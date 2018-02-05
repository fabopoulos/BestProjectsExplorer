<template>
  <div class="activities">
  <v-card onload="addMonthReportHeader(duration)">
    <v-progress-linear value="10" height="20" color="red"></v-progress-linear>
    <v-data-table
      :headers="headersActivities"
      :items="activities"
      hide-actions
    >
      <template slot="items" slot-scope="props">
          <td class="text-xs-center">
          <v-progress-circular
                  v-bind:size="40"
                  v-bind:width="6"
                  v-bind:rotate="360"
                  v-bind:value=calculate(props.item.monthly_report,props.item.target)
                  color="teal"
                >
                  {{percentage}}%
                </v-progress-circular>
          </td>
          <td>
            <input
                name="activity-name"
                v-model="props.item.name"
              />
          </td>
          <td>
            <input
                name="activity-target"
                v-model="props.item.target"
                class="field"
              />
          </td>
          <td >
            <input
                name="activity-unit"
                v-model="props.item.unit"
                class="field"
              />
          </td>
          <td  v-if="report" v-for="m, index in report"  v-bind:key="index">
            <input v-model=report[index] class="month"/>
          </td>
        <!-- <ActivityReport :monthly_report="props.item.monthly_report"></ActivityReport>-->
      </template>
    </v-data-table>
    </v-card>
    </div>
</template>

<script>

export default {
  name: 'activities',
  components: {
    // ActivityReport
  },
  props: {
    activities: {
      type: Array,
      required: true
    },
    // monthly_report: [],
    duration: 0
  },
  methods: {
    calculate (str, target) {
      let vm = this
      let myTarget = Number(target)
      vm.realised = 0
      vm.percentage = 0
      vm.report = str.split(',')
      let nbMonth = vm.report.length
      for (let i = 0; i !== nbMonth; i++) {
        // alert(Number(vm.monthly_report[i]))
        // alert(Number(vm.report[i]))
        vm.realised = vm.realised + Number(vm.report[i])
        // alert(vm.realised)
      }
      // alert(vm.realised)
      vm.percentage = ((vm.realised * 100) / myTarget)
      return (vm.percentage)
    },
    splitMonthlyReport (str) {
      let vm = this
      vm.monthly_report = str.split(',')
      return vm.monthly_report
    },
    addMonthReportHeader (index) {
      let vm = this
      let i = 0
      // alert('addMonthReportHeader index:' + index)
      for (i = 1; i !== (index + 1); i++) {
        var myObj = {
          text: 'M' + (i),
          align: 'left',
          value: 'M' + (i)
        }
        vm.headersActivities.push(myObj)
      }
    }
  },
  data () {
    return {
      realised: 0,
      percentage: 0,
      report: [],
      headersActivities: [
        {
          text: 'Progress',
          align: 'center',
          value: 'progress'
        },
        {
          text: 'Activity Name',
          align: 'left',
          value: 'name'
        },
        {
          text: 'Target',
          align: 'left',
          value: 'target',
          sortable: 'false'
        },
        {
          text: 'Unit',
          align: 'left',
          value: 'unit',
          sortable: 'false'
        }
      ]
    }
  },
  computed () {

  },
  mounted () {
    var vm = this
    // alert('mounted')
    vm.addMonthReportHeader(vm.duration)
  }
}
</script>
<style scoped>
  .field {
    width: 30px;
    text-align: center;
  }
  .month{
    width: 20px;
    text-align: center;
  }
  div.activities{
    overflow: auto;
  }
</style>
