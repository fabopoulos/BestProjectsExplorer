<template>
<v-data-table
  v-bind:headers="headersOuputs"
  :items="outputs"
  hide-actions
  hide-headers
>
  <template slot="items" slot-scope="output">
    <td>
      <h3><input v-model="output.item.name"/></h3>
      <Activities :activities="output.item.activities" :duration="duration"></Activities>
    </td>
  </template>
</v-data-table>
</template>

<script>
import Activities from '../activities/Activities'
export default {
  name: 'outputs',
  components: {
    Activities
  },
  props: {
    outputs: {
      type: Array,
      required: true
    },
    duration: 0
  },
  data () {
    return {
      headersOuputs: [
        {
          text: 'Output Name',
          align: 'left',
          value: 'outputs'
        }
      ]
    }
  }
}
</script>
<style scoped>
</style>
