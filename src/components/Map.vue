<template>
  <div>
    <div id="myMap"></div>
    <ProjectItemMarker v-for="project in projects"  :project="project" :my-map="myMap" v-bind:key="project.id"  ></ProjectItemMarker>

      <!--
      <gmap-map
        :center="center"
        :zoom="7"
        style="width: 500px; height: 300px"
      >
        <gmap-marker
          :key="index"
          v-for="(m, index) in markers"
          :position="m.position"
          :clickable="true"
          :draggable="false"
          @click="center=m.position"
        ></gmap-marker>
      </gmap-map>-->
  </div>
</template>

<script>
// import VueLeaflet from 'vueleaflet'
// import * as VueGoogleMaps from 'vue2-google-maps'

import ProjectItemMarker from './ProjectItemMarker'
import L from 'leaflet'

export default {
  name: 'my-map',
  components: {
    ProjectItemMarker
    // VueLeaflet
  },
  props: {
    projects: {
      type: Array,
      required: true
    }
  },
  data () {
    return {
      myMap: null,
      myLayer: null
    }
  },
  methods: {
    initMap () {
      var vm = this
      vm.myMap = L.map('myMap').setView([16.0782, -61.6808], 4)
      vm.initLayers()
    },
    initLayers () {
      var vm = this
      vm.Layer = L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}', {
        attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="http://mapbox.com">Mapbox</a>',
        maxZoom: 18,
        id: 'mapbox.streets',
        accessToken: 'pk.eyJ1IjoiZmFib3BvdWxvcyIsImEiOiJjamN4dTIxeHM0OGFqMzNwZ2Y4YmRkanhnIn0.OohI-PR5Rkjs5kSo5kVHZw'
      }).addTo(vm.myMap)
      // vm.layer.redraw()
      // vm.myMap.fitBounds(layer.getBounds)
    }
  },
  mounted () {
    var vm = this
    vm.initMap()

    vm.$forceUpdate()

  }
}
</script>

<style scoped>

  #myMap{
    height: 400px;
  }
</style>
