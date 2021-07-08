<template>
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
</template>

<script>
    import axios from 'axios'
    export default {
    data: () => ({
        allUsers : [],
        items: [],
        model: 1
    }),

    props: [
        'index'
    ],
    async created(){
        let token = localStorage.getItem("access");
        const response = await axios.post("http://localhost:8000/api/admin/get-users",{},{ 
                    headers: {"Authorization" : `Bearer ${token}`}
        });

        console.log(token);

        this.allUsers = await response.data.data;
        console.log("Shiva",this.allUsers)
       
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