<template>
    <v-card
        style="max-width:800px;margin:auto;"
    >
        <template>
          <center 
            style="padding:10px;font-size:30px;text-transform:uppercase;"
          >
            Sign Up
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

                <v-select
                  :items="items"
                  v-model="role"
                  label="Role"
                  solo
                  required
                ></v-select>

                <v-text-field
                v-model="password"
                label="Password"
                required
                type="password"
                ></v-text-field>

                <v-text-field
                v-model="confirm_password"
                label="Confirm Password"
                required
                type="password"
                ></v-text-field>

                <v-btn
                :disabled="!valid"
                color="primary"
                class="mr-4"
                @click="validate"
                >
                Register
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
    data: vm => ({
      select: null,
      valid: true,
      items: ['user'],
      username: '',
      password: '',
      role : 'user', // admin,user
      confirm_password: '',
      nameRules: [
        v => !!v || 'Name is required',
      ],
    }),

    methods: {
      formatDate (date) {
        if (!date) return null

        const [year, month, day] = date.split('-')
        return `${year}-${month}-${day}`
      },
      validate () {
        let a = this.$refs.form.validate()
        
        if(true) {
         this.$store.dispatch('userRegister', {
            username: this.username,
            password: this.password,
            role : this.role
          })
          
          .then(res => {
            this.$router.push("/login");
          })
          
          .catch(err => {
            this.$store.commit('changeDialog', {
              'heading': 'Instructions',
              details: [
                'username should not be blank',
                'username and email should be unique',
                'email should be valid',
                'password should contain alphabet, number and punctuation',
                'password shouldn\'t match with your name'
              ]
            })
            this.$store.state.dialog = true;
          })
        }
      },
      handlePassword () {
        if(this.password != this.confirm_password)  {
          return 'Password mismatch'
        }
        return true;
      }
    },

    mounted () {
  
    }
  }
</script>
