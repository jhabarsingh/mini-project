<template>
    <v-card
        style="max-width:800px;margin:auto;"
    >
        <template>
            <center 
              style="padding:10px;font-size:30px;text-transform:uppercase;"
            >
              Update Container Settings
            </center>
            
            <v-divider />

            <v-form
                ref="form"
                v-model="valid"
                lazy-validation
                style="padding:30px;"
            >

                <v-text-field
                v-model="name"
                :rules="nameRules"
                label="Deployement Name"
                disabled="true"
                ></v-text-field>
                
                <v-text-field
                v-model="app"
                :rules="nameRules"
                label="Container Name"
                disabled="true"
                ></v-text-field>
                
                <v-text-field
                v-model="image"
                :rules="nameRules"
                label="Image Name"
                disabled="true"
                ></v-text-field>
                
                <v-text-field
                v-model="port"
                :rules="nameRules"
                label="Port Number"
                disabled="true"
                ></v-text-field>
                
                <v-text-field
                v-model="cpu"
                :rules="nameRules"
                label="CPU Requirement"
                ></v-text-field>
                
                <v-text-field
                v-model="memory"
                :rules="nameRules"
                label="Memory Requirement"
                ></v-text-field>

                <v-text-field
                v-model="container_lifetime"
                label="Container Max Running Time"
                ></v-text-field>

                <v-text-field
                v-model="container_maxreplica"
                label="Container Max Replicas"
                type="text"
                required
                ></v-text-field>

                <v-btn
                color="primary"
                class="mr-4"
                @click="login"
                >
                Update
                </v-btn>

            </v-form>
            </template>
    </v-card>
</template>

<script>
  export default {
    data: () => ({
      valid: true, 
      name: '',
      app : '',
      cpu : '',
      memory : '',
      image : '',
      port : '',
      container_lifetime: '',
      container_maxsize: '',
      container_maxreplica: '',
      select: null
    }),
    methods: {
      login () {
        this.$refs.form.validate()
         let a = this.$refs.form.validate()
        
        if(true) {
          this.$store.dispatch('userLogin', {
            username: this.username,
            password: this.password
          })
          .then(res => {
            this.$store.state.isLoggedin = true;
            this.$store.state.username = this.username
            localStorage.setItem("username", this.username);
            
            this.$router.push("/home");
          })
          .catch(err => {
            this.$store.commit('changeDialog', {
              'heading': 'Instructions',
              details: [
                'email and password should be valid',
              ]
            })
            this.$store.state.dialog = true;
          })
        }
      }
    },
  }
</script>