<template>
<div
  style="max-width:800px;margin:auto;"
>
    <v-card
      style="margin-bottom: 20px;"
    >
          <v-list>
            <v-list-item>
                <div style="margin:auto" class="text-center">
                    <div>
                      <v-btn
                        class="ma-2"
                        color="primary"
                        dark
                        @click="runContainer"
                        v-if="status!='running'"
                      >
                        Run Container
                        <v-icon
                          dark
                          right
                        >
                          mdi-checkbox-marked-circle
                        </v-icon>
                      </v-btn>

                      <v-btn
                        class="ma-2"
                        color="red"
                        dark
                        @click="stopContainer"
                        v-if="status=='running'"
                      >
                        Stop Container
                        <v-icon
                          dark
                          right
                        >
                          mdi-cancel
                        </v-icon>
                      </v-btn>

                      <v-btn
                        class="ma-2"
                        dark
                        @click="deleteContainer"
                      >
                        <v-icon
                          dark
                          left
                        >
                          mdi-minus-circle
                        </v-icon>
                        Delete Container
                      </v-btn>
                    </div>
                  </div>
            </v-list-item>
          </v-list>
    </v-card>
    <v-card>
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
                :disabled="true"
                ></v-text-field>


                <v-text-field
                v-model="name"
                label="Deployement Name"
                :disabled="true"
                ></v-text-field>
                
                
                <v-text-field
                v-model="image"
                label="Image Name"
                :disabled="true"
                ></v-text-field>

                <v-text-field
                v-model="status"
                label="Status"
                :disabled="true"
                ></v-text-field>
                
                <v-text-field
                v-model="port"
                label="Port Number"
                :disabled="true"
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
                v-model="maxRuntime"
                label="Container Max Running Time"
                ></v-text-field>

                <v-text-field
                v-model="cpuLimit"
                label="Container Max CPU Limit"
                ></v-text-field>

                <v-text-field
                v-model="memLimit"
                label="Container Max Memory Limit"
                ></v-text-field>

                <v-text-field
                v-model="maxReplicas"
                label="Container Max Replicas"
                type="text"
                required
                ></v-text-field>

                <v-btn
                color="primary"
                class="mr-4"
                @click="update"
                >
                Update
                </v-btn>

            </v-form>
            </template>
    </v-card>

</div>
</template>

<script>
import axios from 'axios';

  export default {
    data: () => ({
      data: null,
      valid: true,
      id: null, 
      name: '',
      username: '',
      cpu : '',
      memory : '',
      image : '',
      status: '',
      port : '',
      cpuLimit: '500m',
      memLimit: '500Mi',
      maxRuntime: '120',
      maxReplicas: '5',
      select: null,
      token:""
    }),
    methods: {
      async runContainer(){

              try {
              const response = await axios.post(this.$store.state.URL + "api/admin/deploy",
              {
                  id:this.id
              },
              { 
                  headers: {"Authorization" : `Bearer ${this.token}`}
              });

              console.log(response) 
              this.$router.push('/all-requests')
            } catch(err) {
              console.log(err)
            }
      },
      async stopContainer(){

              try {
              const response = await axios.post(this.$store.state.URL + "api/admin/delete",
              {
                  id:this.id
              },
              { 
                  headers: {"Authorization" : `Bearer ${this.token}`}
              });

              console.log(response) 
              this.$router.push('/all-requests')
            } catch(err) {
              console.log(err)
            }
      },
      async deleteContainer(){

              try {
              const response = await axios.post(this.$store.state.URL + "api/user/delete-entry",
              {
                  id:this.id
              },
              { 
                  headers: {"Authorization" : `Bearer ${this.token}`}
              });

              console.log(response)
              this.$router.push('/all-requests')
            } catch(err) {
              console.log(err)
            }
      },
      async update () {
        this.$refs.form.validate()
         let a = this.$refs.form.validate()
        
        if(true) {
          let token = localStorage.getItem("access");
            let requirements = {
                id: this.id,
                name : this.name,
                cpu : this.cpu,
                memory : this.memory,
                image : this.image,
                port : this.port,
                cpuLimit: this.cpuLimit,
                memLimit: this.memLimit,
                maxRuntime: this.maxRuntime,
                maxReplicas: this.maxReplicas,
            };

            try {
              const response = await axios.post(this.$store.state.URL + "api/admin/update-requirement",
              {
                  requirements
              },
              { 
                  headers: {"Authorization" : `Bearer ${this.token}`}
              });
              
              requirements = {
                _id: this.id,
                ...requirements
              }
              console.log(requirements);

              this.$router.push({
                query: requirements
              })
            } catch(err) {
              console.log(err.response)
            }
        }
      }
    },
    created() {
      
      this.data = this.$route.query
      this.username = this.data.by;
      this.name = this.data.name;
      this.image = this.data.image;
      this.port = this.data.port;
      this.status = this.data.status;
      this.cpu = this.data.cpu;
      this.memory = this.data.memory;
      this.id = this.data._id;
      this.token=localStorage.getItem("access");
      this.memLimit = this.data.memLimit;
      this.maxRuntime = this.data.maxRuntime;
      this.maxReplicas = this.data.maxReplicas;
      this.cpuLimit = this.data.cpuLimit;
      console.log(this.$route.query);
    }   
  }
</script>