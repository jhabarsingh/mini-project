<template>
  <Drawer
  >
    <template
      v-slot:main
    >
      <KubeRequirements />
    </template>
  </Drawer>
</template>

<script>
  import KubeRequirements from '../components/KubeRequirements.vue'
  import Drawer from '../components/Drawer.vue'
  export default {

    components: {
      KubeRequirements,
      Drawer
    },
  }
</script>
