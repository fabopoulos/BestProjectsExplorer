<template>
  <div id="app">
      <v-app>
        <v-navigation-drawer fixed temporary v-model="drawer" :stateless="left" app>
            <v-list dense>
              <v-list-tile @click.stop="left = !left">
                <v-list-tile-action>
                  <v-icon>exit_to_app</v-icon>
                </v-list-tile-action>
                <v-list-tile-content>
                  <v-list-tile-title>Open Temporary Drawer</v-list-tile-title>
                </v-list-tile-content>
              </v-list-tile>
            </v-list>
           </v-navigation-drawer>
          <v-toolbar dark class="blue">
            <v-toolbar-side-icon @click.stop="drawer = !drawer"></v-toolbar-side-icon>
            <v-toolbar-title>
              <router-link to="/" tag="span" style="cursor: pointer" >BEST Projects Explorer</router-link>
            </v-toolbar-title>
            <v-spacer></v-spacer>
            <v-toolbar-items>
              <!--
              <v-btn flat v-for="item in menuItems" :key="item.title" router :to="item.link">
                <v-icon left>{{ item.icon }}</v-icon>
                  {{ item.title }}
              </v-btn>
              -->
              <v-btn flat >
                <v-icon left>settings_applications</v-icon>
                Admin
              </v-btn>
            </v-toolbar-items>
          </v-toolbar>
          <main>
              <router-view></router-view>
          </main>
        <v-footer color="blue-grey" class="white--text" app>
          <span>interact relief</span>
           <v-spacer></v-spacer>
          <span>&copy; 2017</span>
        </v-footer>
    </v-app>
  </div>
</template>

<script>
import ProjectExplorer from './components/ProjectsExplorer.vue'
export default {
  data () {
    return {
      drawer: false,
      left: false,
      menuItems: [
        {icon: 'settings_applications', title: 'Admin', link: 'http://127.0.0.1/admin/'}
      ]
    }
  },
  components: {
    ProjectExplorer
  }
}
</script>

<style>
#app {
  /*
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
  */
}
</style>
