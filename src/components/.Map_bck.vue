<template>
<div id="my-map">
  <v-map :zoom=13 :center="[16.0782,-61.6808]">
    <v-tilelayer url="http://{s}.tile.osm.org/{z}/{x}/{y}.png"></v-tilelayer>
    <ProjectItemMarker  v-for="project in projects" v-bind:project="project" v-bind:key="project.id" >
      <v-marker  :lat-lng="[16.0782,-61.6808]" ></v-marker>
    </ProjectItemMarker>
  </v-map>
  <div ></div>
</div>
</template>

<script>
import Vue2Leaflet from 'vue2-leaflet'
import ProjectItemMarker from './ProjectItemMarker'
export default {
  name: 'my-map',
  components: {
    'v-map': Vue2Leaflet.Map,
    'v-tilelayer': Vue2Leaflet.TileLayer,
    'v-marker': Vue2Leaflet.Marker,
    ProjectItemMarker
    // 'v-marker': Vue2Leaflet.Marker
  },
  props: {
    projects: {
      type: Array,
      required: true
    }
  },

  mounted () {

  }
}
</script>

<style scoped>

  #my-map{
    height: 600px;
    width: 900px;
    background-color: #00bfa5;
  }
</style>
