<template>
    <v-card
        style="max-width:800px;margin:auto;"
    >
        <template>
          <center 
            style="padding:10px;font-size:30px;text-transform:uppercase;"
          >
            Requirements
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
                required
                ></v-text-field>
                
                <v-text-field
                v-model="app"
                :rules="nameRules"
                label="Container Name"
                required
                ></v-text-field>
                
                <v-text-field
                v-model="image"
                :rules="nameRules"
                label="Image Name"
                required
                ></v-text-field>
                
                <v-text-field
                v-model="port"
                :rules="nameRules"
                label="Port Number"
                required
                ></v-text-field>
                
                <v-text-field
                v-model="cpu"
                :rules="nameRules"
                label="CPU Requirement"
                required
                ></v-text-field>
                
                <v-text-field
                v-model="memory"
                :rules="nameRules"
                label="Memory Requirement"
                required
                ></v-text-field>
                
                <v-btn
                :disabled="!valid"
                color="primary"
                class="mr-4"
                @click="validate"
                >
                Send
                </v-btn>

            </v-form>
            </template>

            <DialogAlert />
    </v-card>
</template>

<script>
  import DialogAlert from './DialogAlert.vue'
  import axios from 'axios'
  export default {
    components: {
      DialogAlert
    },
    data: vm => ({
      select: null,
      valid: true,
      name: '',
      app : '',
      cpu : '',
      memory : '',
      image : '',
      port : '',
      nameRules: [
        v => !!v || 'Name is required',
      ],
    }),

    methods: {
      async validate () {
        let a = this.$refs.form.validate()
        if(a) {
            const requirements = {
                name : this.name,
                app : this.app,
                cpu : this.cpu,
                memory : this.memory,
                image : this.image,
                port : this.port
            };

            console.log(requirements);
            const response = await axios.post("http://localhost:8000/api/user/send-requirements",{requirements});
            console.log(response.data);
        }
      },

    },

    mounted () {
  
    }
  }
</script>
