<template>
    <v-card
        style="max-width:800px;margin:auto;"
    >
        <template>
            <center 
              style="padding:10px;font-size:30px;text-transform:uppercase;"
            >
              Sign In
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
                label="Username"
                required
                ></v-text-field>

                <v-text-field
                v-model="password"
                label="Password"
                type="password"
                required
                ></v-text-field>


                <v-btn
                color="primary"
                class="mr-4"
                @click="login"
                >
                Login
                </v-btn>

            </v-form>
            </template>
            <DialogAlert />
    </v-card>
</template>

<script>
import DialogAlert from './DialogAlert.vue'
  export default {
    components: {
      DialogAlert
    },
    data: () => ({
      valid: true,
      password: '',
      username: '',
      select: null,
      nameRules: '',
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