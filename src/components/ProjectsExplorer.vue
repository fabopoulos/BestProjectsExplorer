<template>
  <v-container grid-list-md text-xs-center>
    <v-layout row wrap>
      <v-flex xs12>
        <ProjectsList v-bind:projects="projects"></ProjectsList>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import ProjectsList from './ProjectsList'
import ProjectDetails from './ProjectDetails'
import Map from './Map'

export default {
  name: 'projects-explorer',
  components: {
    ProjectsList,
    ProjectDetails,
    Map
  },
  data () {
    return {
      projects: {
        type: Object,
        required: true
      }
    }
  },
  methods: {
    getProjectsJSON () {
      var vm = this
      console.log('getProjectsJSON')
      $.getJSON('http://127.0.0.1:8000/BestProjectExplorerApp/projects', function (data) {
        vm.projects = data
      })
    },
    initExplorer () {
      var vm = this
      // console.log('initExplorer')
      vm.getProjectsJSON()
    }
  },
  mounted () {
    /* var self = this
    // get json projects response from backend api
    $.getJSON('http://127.0.0.1:8000/BestProjectExplorerApp/projects', function (data) {
      self.projects = data
    })
    */
    var vm = this
    vm.initExplorer()
    // console.log('mounted')
  }
}
</script>
<style scoped>
</style>
