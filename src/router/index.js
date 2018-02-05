import Vue from 'vue'
import Router from 'vue-router'

import ProjectsExplorer from '../components/ProjectsExplorer'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'ProjectsExplorer',
      component: ProjectsExplorer
    },
    {
      path: '/admin/',
      name: 'Admin'
    }
  ],
  mode: 'history'
})
