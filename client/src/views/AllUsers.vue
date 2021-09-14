<template>
  <Drawer
  >
    <template
      v-slot:main
    >
      <AllUsers />
    </template>
  </Drawer>
</template>

<script>
  import AllUsers from '../components/AllUsers.vue'
  import Drawer from '../components/Drawer.vue'
  export default {

    components: {
      AllUsers,
      Drawer
    },
  }
</script>
