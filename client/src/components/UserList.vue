<template>
<div>
  <Alert 
    :message="message"
    :alert="alert"
    style="max-width:600px; margin:auto"
  />

  <v-card
    class="mx-auto"
    max-width="600"
    :elevation="3"
    v-if="items.length != 0"
  >
    <v-list class="list">
      <v-list-item-group v-model="model">
        <v-list-item
          v-for="(item, i) in items"
          :key="i"
          style="margin-top:1px;"
        >
          <v-list-item-icon>        
            <v-icon
            md
            color="green darken-2"
            @click="deleteUser(item.username)"
            >
                mdi-delete
            </v-icon>
          </v-list-item-icon>
          <v-list-item-content>
            <v-list-item-title v-text="item.username"></v-list-item-title>
          </v-list-item-content>
          <v-btn
            class="mx-1"
            color="primary"
            @click="getContainers(item.username)"
          >
            Containers
          </v-btn>
        </v-list-item>
      </v-list-item-group>
    </v-list>
  </v-card>
</div>
</template>

<script>
    import axios from 'axios'
    import Alert from './Alert.vue'
    export default {
    data: () => ({
        allUsers : [],
        items: [],
        model: 1,
        message: "",
        alert: false
    }),

    props: [
        'index'
    ],
    components: {
      Alert
    },
    async created(){
        let token = localStorage.getItem("access");
        const response = await axios.post("http://localhost:8000/api/admin/get-users",{},{ 
                    headers: {"Authorization" : `Bearer ${token}`}
        });

        console.log(token);

        this.allUsers = await response.data.data;
        let counter = this.allUsers.users.array.length + this.allUsers.admins.array.length;
        
        this.$store.state.users_count = counter;
        console.log(this.allUsers)
        if(this.index == 'b'){
            this.items = this.allUsers.users.array
        }
        else{
            this.items = this.allUsers.admins.array
        }
    },
    
    methods: {
        getContainers(user) {
          this.$router.push({
            name: 'AllRequests',
            query: {
              user: user
            }
          })
        },
        async deleteUser(user) {
          let token = localStorage.getItem("access");

          try {
            const response = await axios.post(this.$store.state.URL + "api/admin/delete-user",
            {
              username: user
            },
            { 
                        headers: {"Authorization" : `Bearer ${token}`}
            });

            this.message = `Sucessfully Deleted the User`
            this.alert = true;
            setTimeout(() => {
              this.$router.push("/all-users")
              }, 2000);

          }
          catch(err) {
            if(err.response.status == 404) {
              this.message = `Please delete ${user}'s all containers first`
              this.alert = true;
              setTimeout(() => {
                  this.alert = false;
                  this.message = "";
                }, 5000);

            }
            console.log(err.response.status);
            console.log(err.response);
          }

        }
    },
    watch: {
        index(){
            
          if(this.index == 'b'){
              this.items = this.allUsers.users.array
          }
          else{
              this.items = this.allUsers.admins.array
          }
        }
    },

    }
    </script>

    <style scoped>
    .list {
    padding: 10px;
    }
</style>