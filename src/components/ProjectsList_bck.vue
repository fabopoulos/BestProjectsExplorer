<template>
<v-card>
    <v-card-title>
      Projects
         <v-btn>
        <v-icon>note_add</v-icon>
          Add
      </v-btn>
      <v-spacer></v-spacer>
      <v-text-field
        append-icon="search"
        label="Search"
        single-line
        hide-details
        v-model="search"
      ></v-text-field>

    </v-card-title>
  <v-data-table
      v-bind:headers="headers"
      :items="projects"
      :search="search"
      class="elevation-1"
    >
    <template slot="items" slot-scope="props">
      <!--<v-layout >
       <v-flex >
       -->
      <!--<td >{{props.item.code}}<td/>-->
      <!--<td class="text-xs-left">{{props.item.name}}</td>-->
      <td class="text-xs-center">{{props.item.best_code}}</td>
      <td class="text-xs-left">{{props.item.territory}}</td>
      <!--<td class="text-xs-left">{{props.item.start_date}}</td>
      <td class="text-xs-left">{{props.item.end_date}}</td>
      <td class="text-xs-right">{{props.item.total_budget}}</td>-->
        <!--
        </v-flex>
        <v-flex >
        -->
      <td >
        <v-card>
          <v-card-title  >
            <div>
              <h3 class="headline mb-0">{{props.item.name}}</h3>
            </div>
          </v-card-title>
              <v-container fill-height fluid>
                <v-tabs fluid icons centered >
                  <v-tabs-bar dark color="cyan">
                    <v-tabs-slider color="yellow"></v-tabs-slider>
                    <v-tabs-item href="#tab-1">
                      <v-icon>details</v-icon>
                      Details
                    </v-tabs-item>
                    <v-tabs-item href="#tab-2">
                      <v-icon>dashboard</v-icon>
                      Dashbord

                    </v-tabs-item>
                    <v-tabs-item href="#tab-3">
                      <v-icon>history</v-icon>
                      Historic
                    </v-tabs-item>
                  </v-tabs-bar>
                  <v-tabs-items>
                    <v-tabs-content :id="'tab-1'">
                      <v-card>
                        <v-card-text>
                          <table class="project-details">
                          <tr  style="height: 10px">
                            <td class="project-details">Start Date:</td>
                            <td>{{ props.item.start_date }}</td>
                          </tr>
                          <tr>
                            <td class="project-details">End Date:</td>
                            <td>{{ props.item.end_date }}</td>
                          </tr>
                          <tr>
                            <td class="project-details">Total Budget:</td>
                            <td>{{ props.item.total_budget }}</td>
                          </tr>
                          </table>
                          <textarea name="textarea" rows="10" cols="80%" disabled>
                            {{ props.item.description }}
                          </textarea>
                        </v-card-text>
                      </v-card>
                    </v-tabs-content>
                    <v-tabs-content :id="'tab-2'">
                      <v-card flat>
                        <v-card-text>

                          <v-data-table
                          v-bind:headers="headersOuputs"
                          :items="props.item.outputs"
                          hide-actions
                          hide-headers
                          class="ation-1"
                        >
                        <template slot="items" slot-scope="output">
                          <td>
                          <h3>{{ output.item.name }}</h3>
                            <v-data-table
                            v-bind:headers="headersActivities"
                            :items="output.item.activities"
                            hide-actions
                            class="elevation-1"
                             >
                            <template slot="items" slot-scope="activity">
                              <td>
                                {{ activity.item.name }}
                              </td>
                              <td>
                                {{ activity.item.target }}
                              </td>
                              <td>
                                {{ activity.item.unit }}
                              </td>
                              <td v-for="i,index in report" :key="index">
                                M{{index+1}}:{{i}}
                              </td>
                            </template>
                            </v-data-table>
                          </td>
                        </template>
                      </v-data-table>
                        </v-card-text>
                      </v-card>
                    </v-tabs-content>
                    <v-tabs-content :id="'tab-3'">
                      <v-card flat>
                        <v-card-text>
                          Historic
                        </v-card-text>
                      </v-card>
                    </v-tabs-content>
                  </v-tabs-items>
                </v-tabs>
              </v-container>
          <v-card-actions>
            <v-btn flat color="orange">Edit</v-btn>
            <v-btn flat color="orange">Delete</v-btn>
          </v-card-actions>
        </v-card>
      </td>
     <!--
     </v-flex>
    </v-layout>
    -->
    </template>
    <template slot="no-data">
      <v-alert :value="true" color="error" icon="warning">
        Sorry, nothing to display here :(
      </v-alert>
    </template>
  </v-data-table>
  </v-card>
</template>

<script>
/* eslint-disable no-multiple-empty-lines,key-spacing */

import ProjectItem from './ProjectItem'

export default {
  name: 'projects-list',
  props: {
    projects: {
      type: Array,
      required: true
    }
  },
  components:{
    ProjectItem
  },
  methods: {
    convertStringtoArray (strReport) {
      console.log('strReport' + strReport)
      var vm = this
      var str = strReport
      vm.report = str.split(',')
      console.log(vm.report)
    }
  },
  data () {
    return {
      search: '',
      report:[1,1,0,0,0,1,1,1,0,0,0,1],
      headers:[
        {
          text: 'Project Code',
          align: 'left',
          value: 'best_code',
          width: '3%'
        },
        {
          text: 'Location',
          align: 'left',
          value: 'location',
          width: '7%'
        },
        {
          text: 'Project Name',
          align: 'left',
          value: 'name',
          width: '90%'
        }
      ],
      headersOuputs:[
        {
          text: 'Output Name',
          align: 'left',
          value: 'outputs',
        }
      ],
      headersActivities:[
        {
          text: 'Activity Name',
          align: 'left',
          value: 'activities',
        },
        {
          text: 'Target',
          align: 'left',
          value: 'target',
        },
        {
          text: 'Unit',
          align: 'left',
          value: 'unit',
        },
      ]
    }
  }
}

</script>
<style scoped>
  td.project-details{
    height: 4px;
    font-weight: bold;
  }
</style>
