<template>
  <div>

    <Alert
      class="mx-auto"
      style="max-width:1000px;margin-top:40px;"
      :message='message' :alert="alert" />

    <v-card
      class="mx-auto"
      max-width="1000"
      style="margin-top: 20px"
    >
      <v-toolbar
        color="pink"
        dark
      >

            <v-toolbar-title>Containers</v-toolbar-title>
           
            <v-spacer></v-spacer>
            
            <v-col
                class="d-flex"
                cols="12"
                sm="4"
            >
                <v-select
                :items="items1"
                v-model="filter"
                label="Filters"
                solo
                light
                ></v-select>
            </v-col>

        
      </v-toolbar>

      <v-list two-line>
        <v-list-item-group
          v-model="selected"
          active-class="pink--text"
          multiple
        >
          <template v-for="(item, index) in items">
            <v-list-item :key="item.title">
              <template v-slot:default="{  }">
                <v-list-item-content>
                  <v-list-item-title v-text="item.name"></v-list-item-title>


                  <v-list-item-subtitle v-text="item.image"></v-list-item-subtitle>
                </v-list-item-content>

                <v-spacer />
                <div>
                    <v-chip
                        class="ma-2"
                        color="primary"
                        >
                        {{ item.status }}
                    </v-chip>

                    <v-btn icon
                            style="margin-left: 5px;"
                        @click="deleteFromDB(index)"
                    >
                        <v-icon>mdi-delete</v-icon>
                    </v-btn>
                        <v-btn icon
                            style="margin-left: 5px;"
                            v-if="item.status=='running'"
                        @click="deleteContainer(index)"

                    >
                        <v-icon>mdi-cancel</v-icon>
                    </v-btn>
                                 <v-btn icon
                            style="margin-left: 5px;"
                            v-if="item.status=='stopped'"
                        @click="runStoppedContainer(index)"

                    >
                        <v-icon>mdi-reload</v-icon>
                    </v-btn>
                    <v-btn icon
                            style="margin-left: 5px;"
                            v-if="item.status=='running'"
                            :href="`http://172.16.16.102:${item.exposedPort}`"

                    >
                        <v-icon>mdi-send</v-icon>
                    </v-btn>

                </div>

              </template>
            </v-list-item>

            <v-divider
              v-if="index < items.length - 1"
              :key="index"
            ></v-divider>
          </template>
        </v-list-item-group>
      </v-list>
    </v-card>

      <template>
        <div class="text-center">
          <v-container>
            <v-row justify="center">
              <v-col cols="8">
                <v-container class="max-width">
                  <v-pagination
                    v-model="page"
                    class="my-4"
                    :length="Math.ceil(+count / 10)"
                  ></v-pagination>
                </v-container>
              </v-col>
            </v-row>
          </v-container>
        </div>
      </template>

  </div>
</template>

<script>
  import axios from 'axios';
  import Alert from './Alert.vue';
  export default {
    data: () => ({
      selected: [2],
      items: [
          
      ],
      pending: [],
      running: [],
      stopped: [],
      all: [],
      items1: [
          "Pending",
          "Running",
          "Stopped",
          "All"
      ],
      filter: "All",
      page: null,
      count: null,
      token:"",
      message: "",
      alert: false,
    }),
    components: {
      Alert
    },
    watch: {
      filter: function(val) {
        let a = val[0];
        switch(a) {
          case 'P': this.items = this.pending; break;
          case 'R': this.items = this.running; break;
          case 'S': this.items = this.stopped; break;
          case 'A': this.items = this.all; break;
        }
      }

    },  
    methods: {
          async deleteFromDB(index){
            console.log(this.items[index]._id)
              try {
              const response = await axios.post(this.$store.state.URL + "api/user/delete-entry",
              {
                  id:this.items[index]._id
              },
              { 
                  headers: {"Authorization" : `Bearer ${this.token}`}
              });
              
              this.message = "Container Deleted Successfully";
              this.alert = true;
              setTimeout(() => {
                this.$router.go(this.$router.currentRoute)
              }, 2000);
              
            } catch(err) {
              console.log(err)
            }
      },
          async deleteContainer(index){
            console.log(this.items[index]._id)
              try {
              const response = await axios.post(this.$store.state.URL + "api/admin/delete",
              {
                  id:this.items[index]._id
              },
              { 
                  headers: {"Authorization" : `Bearer ${this.token}`}
              });

              this.message = "Container Stopped Successfully";
              this.alert = true;
              setTimeout(() => {
                this.$router.go(this.$router.currentRoute)
              }, 2000);

            } catch(err) {
              console.log(err)
            }
      },
          async runStoppedContainer(index){
           
              try {
              const response = await axios.post(this.$store.state.URL + "api/admin/re-request",
              {
                  id:this.items[index]._id
              },
              { 
                  headers: {"Authorization" : `Bearer ${this.token}`}
              });

              this.message = "Container Running Successfully";
              this.alert = true;
              setTimeout(() => {
                this.$router.go(this.$router.currentRoute)
              }, 2000);

            } catch(err) {
              console.log(err)
            }
      },
      goTo(message) {
        this.$router.push({
          name: 'Admin',
          query: message
        })
      }
    },
    async created() {
      let item;
     this.token=localStorage.getItem("access");
      let config = {
        headers: {"Authorization" : `Bearer ${this.token}`}
      }
        let link = this.$store.state.URL + "api/admin/get-requests";

        console.log(link)
        let response = await axios.post(link , {}, config)
        let items = await response.data.data;

        this.pending = await items.pending;
        this.stopped = await items.stopped;
        this.running = await items.running;

        this.pending = this.pending.array;
        this.stopped = this.stopped.array;
        this.running = this.running.array;

        this.all = [...this.pending, ...this.stopped, ...this.running];
        this.items = this.all;
    }
  }
</script>
