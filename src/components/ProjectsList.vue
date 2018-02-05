<template>
  <v-flex xs12>
  <v-card>
    <v-card-title>
      Projects
      <v-btn>
        <v-icon>note_add</v-icon>
        Add
      </v-btn>
      <v-text-field
        append-icon="search"
        label="Search"
        single-line
        hide-details
        v-model="search"
      >
      </v-text-field>
    </v-card-title>
    <v-data-table
      v-bind:headers="headers"
      :items="projects"
      :search="search"
      hide-headers
    >
      <template slot="headers" slot-scope="props">
        <tr>
          <th class="columns">Code</th>
          <th class="columns">Territory</th>
          <th >Project</th>
        </tr>
      </template>
      <template slot="items" slot-scope="project">
        <td class="columns">{{project.item.best_code}}</td>
        <td class="columns">{{project.item.territory}}</td>
        <td>
          <v-card>
            <v-container>
              <h2>{{project.item.best_code}}-{{project.item.name}}: [ {{ project.item.start_date }}->{{ project.item.end_date }} - {{ project.item.duration }} month(s) ]</h2>
              <project-detail :project="project.item"></project-detail>
            </v-container>
          </v-card>
        </td>
      </template>
      <template slot="no-data">
        <v-alert :value="true" color="error" icon="warning">
          Sorry, nothing to display here :(
         </v-alert>
      </template>
    </v-data-table>
  </v-card>
  </v-flex>
</template>

<script>
/* eslint-disable no-multiple-empty-lines,key-spacing */

import ProjectDetail from './ProjectDetails'
import ProjectSpeedDial from './Project/ProjectSpeedDial'
export default {
  name: 'projects-list',
  props: {
    projects: {
      type: Object,
      required: true
    }
  },
  components:{
    ProjectDetail,
    ProjectSpeedDial
  },
  data () {
    return {
      search: '',
      headers:[
        {
          text: 'Project Code',
          align: 'left',
          value: 'best_code',

        },
        {
          text: 'Location',
          align: 'left',
          value: 'location',

        },
        {
          text: 'Project Name',
          align: 'left',
          value: 'name',

        }
      ]
    }
  }
}

</script>
<style scoped>
  .columns{
    width: 30px;
  }

</style>
