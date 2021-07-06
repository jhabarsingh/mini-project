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
                v-model="username"
                label="Deployer Name"
                disabled="true"
                ></v-text-field>


                <v-text-field
                v-model="name"
                label="Deployement Name"
                disabled="true"
                ></v-text-field>
                
                <v-text-field
                v-model="app"
                label="Container Name"
                disabled="true"
                ></v-text-field>
                
                <v-text-field
                v-model="image"
                label="Image Name"
                disabled="true"
                ></v-text-field>

                <v-text-field
                v-model="status"
                label="Status"
                disabled="true"
                ></v-text-field>
                
                <v-text-field
                v-model="port"
                label="Port Number"
                disabled="true"
                ></v-text-field>
                
                <v-text-field
                v-model="cpu"
                label="CPU Requirement"
                ></v-text-field>
                
                <v-text-field
                v-model="memory"
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
      data: null,
      valid: true, 
      name: '',
      username: '',
      app : '',
      cpu : '',
      memory : '',
      image : '',
      status: '',
      port : '',
      container_lifetime: '120',
      container_maxreplica: '5',
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
    created() {
      
      this.data = this.$route.query
      this.username = this.data.by;
      this.name = this.data.name;
      this.app = this.data.app;
      this.image = this.data.image;
      this.port = this.data.port;
      this.status = this.data.status;
      this.cpu = this.data.cpu;
      this.memory = this.data.memory;
      this.
      console.log(this.data);
    }
  }
</script>