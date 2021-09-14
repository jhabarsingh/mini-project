<template>
    <v-card
        style="max-width:800px;margin:auto;"
    >
        <template>
          <center 
            style="padding:10px;font-size:30px;text-transform:uppercase;"
          >
            Container Details
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
                label="Deployement Name"
                required
                ></v-text-field>
                
                
                <v-text-field
                v-model="image"
                label="Image Name"
                required
                ></v-text-field>
                
                <v-text-field
                v-model="port"
                label="Port Number"
                required
                ></v-text-field>
                
                <v-text-field
                v-model="cpu"
                label="CPU Requirement"
                required
                ></v-text-field>
                
                <v-text-field
                v-model="memory"
                label="Memory Requirement"
                required
                ></v-text-field>
                
                <v-btn
                :disabled="!valid"
                color="primary"
                class="mr-4"
                @click="validate"
                >
                Deploy
                </v-btn>

                <small
                  style="color: orange;letter-spacing:1px;font-size:15px;"
                  v-if="update_success"
                >Deployed succesfully</small>

            </v-form>
            </template>

    </v-card>
</template>

<script>
  import axios from 'axios'
  export default {
    components: {
    },
    data: vm => ({
      select: null,
      valid: true,
      name: '',
      cpu : '',
      memory : '',
      image : '',
      port : '',
      nameRules: [
        v => !!v || 'Name is required',
      ],
      update_success: false
    }),

    methods: {
      async validate () {
        let a = this.$refs.form.validate()
        if(a) {
            let token = localStorage.getItem("access");
            const requirements = {
                name : this.name,
                cpu : this.cpu,
                memory : this.memory,
                image : this.image,
                port : this.port
            };

            const response = await axios.post("http://localhost:8000/api/user/send-requirements",
                {
                    requirements
                },
                { 
                    headers: {"Authorization" : `Bearer ${token}`}
                });

              this.update_success = true;

              setTimeout(() => {
                this.update_success = false;
              }, 2000);
        }
      },

    },

    mounted () {
  
    }
  }
</script>
