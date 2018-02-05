<template>
  <v-card id="create">
    <v-speed-dial
      v-model="fab"
        :top="top"
        :bottom="bottom"
        :right="right"
        :left="left"
        :direction="direction"
        :hover="hover"
        :transition="transition"
    >
      <v-btn
        slot="activator"
        color="blue darken-2"
        dark
        fab
        hover
        v-model="fab"
      >
        <v-icon>account_circle</v-icon>
        <v-icon>close</v-icon>
      </v-btn>
      <v-btn
        fab
        dark
        small
        color="green"
      >
        <v-icon>edit</v-icon>
      </v-btn>
      <v-btn
        fab
        dark
        small
        color="indigo"
      >
        <v-icon>add</v-icon>
      </v-btn>
      <v-btn
        fab
        dark
        small
        color="red"
      >
        <v-icon>delete</v-icon>
      </v-btn>
    </v-speed-dial>
  </v-card>
</template>

<script>
export default {
  name: 'project-speed-dial',
  props: {
    project: null
  },
  data: () => ({
    direction: "bottom",
    fab: false,
    fling: false,
    hover: false,
    tabs: null,
    top: true,
    right: true,
    bottom: false,
    left: true,
    transition: 'slide-y-reverse-transition'
  }),

  watch: {
    top(val) {
      this.bottom = !val
    },
    right(val) {
      this.left = !val
    },
    bottom(val) {
      this.top = !val
    },
    left(val) {
      this.right = !val
    }
  },

  computed: {
    activeFab() {
      switch (this.tabs) {
        case 'one':
          return {'class': 'purple', icon: 'account_circle'}
        case 'two':
          return {'class': 'red', icon: 'edit'}
        case 'three':
          return {'class': 'green', icon: 'keyboard_arrow_up'}
        default:
          return {}
      }
    }
  }
}
</script>

<style scoped>

</style>
