<template>
  <Drawer
  >
    <template
      v-slot:main
    >
       <Admin />
    </template>
  </Drawer>
</template>

<script>
  import Admin from '../components/user/Admin.vue'
  import Drawer from '../components/Drawer.vue'

  export default {

    components: {
      Admin,
      Drawer
    },
  }
</script>
