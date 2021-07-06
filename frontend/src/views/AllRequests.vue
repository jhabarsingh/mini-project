<template>
  <Drawer
  >
    <template
      v-slot:main
    >
      <AllRequests />
    </template>
  </Drawer>
</template>

<script>
  import AllRequests from '../components/AllRequests'
  import Drawer from '../components/Drawer.vue'
  export default {

    components: {
      AllRequests,
      Drawer
    },
  }
</script>
