<template>
  <div>
  </div>
</template>

<script>
// import L from 'leaflet"'
export default {
  name: 'project-item-marker',
  components: {
  },
  props: {
    project: {
      type: Object,
      required: true
    },
    myMap: null
  },
  data () {
    return {
      long: 0,
      lat: 0,
      position: 0,
      positionGeoJSON: 0
    }
  },
  computed: {
    getPostGISPOINTtoLatLong() {
      var vm = this
      var point = vm.project.geom.toString().split(';').splice(1, 1).toString().split(' ')
      console.log(point)
      vm.long = point[1].toString().slice(1, vm.lat.length)
      console.log('long:' + vm.long)
      vm.lat = point[2].toString()
      vm.lat = point[2].toString().slice(0, (vm.lat.length - 1))
      console.log('lat:' + vm.lat)
    }
  },

  methods: {
    initMarker () {
      var vm = this
      var marker = L.marker(L.latLng(vm.lat, vm.long), {
        title: 'string'
      })
        .addTo(vm.myMap)
      // var str = 'test'
      var PopupMessageHTML = '<b>' + 'Project Name: ' + vm.project.code + '-' + vm.project.name + '</b>'
      marker.bindPopup(PopupMessageHTML, { minWidth: 100 })
      // vm.position = marker.getLatLng()
      // console.log('vm.project.name:' + vm.project.name)
      // console.log('vm.position:' + vm.position)
    }
  },
  mounted () {
    var vm = this
    vm.getPostGISPOINTtoLatLong
    vm.initMarker()
  }
}
</script>
<style scoped>
</style>
