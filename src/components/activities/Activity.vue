<template slot="items" slot-scope="activity">
  <div>
    <td>
      {{ activity.item.name }}
    </td>
    <td>
      {{ activity.item.target }}
    </td>
    <td>
      {{ activity.item.unit }}
    </td>
    <td>
      {{ activity.item.monthly_report }}
    </td>
  </div>
</template>
<script>
export default {
  name: 'activity',
  props: {
    activity: {
      type: Object,
      required: true
    }
  }
}
</script>

<style scoped>

</style>
