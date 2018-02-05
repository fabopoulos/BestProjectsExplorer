<template>
    <v-tabs  icons centered >
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
        <v-tabs-item href="#tab-3">
          <v-badge left>
            <span slot="badge">{{nbUpdates}}</span>
            <span>Updates</span>
          </v-badge>
        </v-tabs-item>
      </v-tabs-bar>
      <v-tabs-items>
        <v-tabs-content :id="'tab-1'">
          <v-card>
            <v-card-text>
              <table class="project-details">
                <tr  style="height: 10px">
                  <td class="project-details">Start Date:</td>
                  <td><input v-model="project.start_date" readonly="true"  v-on:dblclick="this.readonly = false " v-on:keypress="nbUpdates += 1" /></td>
                </tr>
                <tr>
                  <td class="project-details">End Date:</td>
                  <td><input v-model="project.end_date"/></td>
                </tr>
                <tr>
                  <td class="project-details">Duration:</td>
                  <td><input v-model="project.duration"/></td>
                </tr>
                <tr>
                  <td class="project-details">Total Budget:</td>
                  <td><input v-model="project.total_budget"/></td>
                </tr>
              </table>
              <textarea name="textarea" rows="10" cols="80%" v-model="project.description">
              </textarea>
            </v-card-text>
          </v-card>
        </v-tabs-content>
        <v-tabs-content :id="'tab-2'">
          <v-card flat>
            <outputs :outputs="project.outputs" :duration="project.duration"></outputs>
          </v-card>
        </v-tabs-content>
        <v-tabs-content :id="'tab-3'">
          <v-card flat>
            <v-card-text>
              {{ getProjectJSON() }}
            </v-card-text>
          </v-card>
        </v-tabs-content>
      </v-tabs-items>
    </v-tabs>
</template>

<script>
import Outputs from './outputs/Outputs'


export default {
  name: 'project-details',
  props: {
    project: {
      type: Array,
      required: true
    }
  },
  components: {
    Outputs,

  },
  data () {
    return {
      nbUpdates: 0
    }
  },
  methods: {
    addUpdate () {
      let vm = this
      vm.nbUpdates = vm.nbUpdates + 1
      alert('nbUpdates:' + vm.nbUpdates)
    },
    getProjectJSON () {
      let vm = this
      return JSON.stringify(vm.project)
    }
  },
  mounted: {

  }
}
</script>

<style scoped>
  td.project-details{
    height: 4px;
    font-weight: bold;
  }
</style>
