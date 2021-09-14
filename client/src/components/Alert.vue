<template>
  <div>
    <v-alert
      v-model="alert"
      dismissible
      color="warning"
      border="left"
      elevation="4"
      colored-border
      icon="mdi-message"
    >
      {{message}}
    </v-alert>

  </div>
</template>

<script>
  export default {
    props: [
        'message',
        'alert'
    ],
    data () {
      return {
      }
    },
  }
</script>