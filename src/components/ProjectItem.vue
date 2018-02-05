<template>
    <tr>
      <td>{{project.code}}<td/>
    </tr>
</template>

<script>
import ProjectDetail from './ProjectItem'
export default {
  name: 'project-item',
  props: {
    project: {
      type: Array,
      required: true
    }
  },
  component: {
    ProjectDetail
  },
  data () {
    return {
      long: 0,
      lat: 0
    }
  },
  mounted () {
    var tmp = this
    var point = tmp.project.geom.toString().split(';').splice(1, 1).toString().split(' ')
    console.log(point)
    tmp.long = point[1].toString().slice(1, tmp.lat.length)
    console.log('x:' + tmp.long)
    tmp.lat = point[2].toString()
    tmp.lat = point[2].toString().slice(0, (tmp.lat.length - 1))
    console.log('y:' + tmp.lat)
  }
}
</script>
<style scoped>
</style>
