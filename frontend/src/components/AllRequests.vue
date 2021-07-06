<template>
  <div>
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
            <v-list-item :key="item.title" @click="goTo(item)">
              <template v-slot:default="{  }">
                <v-list-item-content>
                  <v-list-item-title v-text="item.username"></v-list-item-title>


                  <v-list-item-subtitle v-text="item.container_id"></v-list-item-subtitle>
                </v-list-item-content>

                <v-spacer />
                <div>
                    <v-chip
                        class="ma-2"
                        color="red"
                        text-color="white"
                        >
                        Pending
                    </v-chip>

                    <v-btn icon
                        style="margin-left: 5px;"
                        @click="$router.push('/admin')"
                    >
                        <v-icon
                        > mdi-wrench</v-icon>
                    </v-btn>
                    
                    <v-btn icon
                        style="margin-left: 5px;"
                        @click="setDialog(index)"
                    >
                        <v-icon>mdi-checkbox-marked-circle</v-icon>
                    </v-btn>

                    <v-btn icon
                            style="margin-left: 5px;"
                        @click="setDialog(index)"
                    >
                        <v-icon>mdi-delete</v-icon>
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
  export default {
    data: () => ({
      selected: [2],
      items: [
          
      ],
      pending: [],
      running: [],
      stopped: [],
      items1: [
          "Pending",
          "Running",
          "Stopped"
      ],
      page: null,
      count: null
    }),
    methods: {
      goTo(message) {
        this.$router.push({
          name: 'MessageDetail',
          query: {
            receiver: message.receiver.username,
            content: message.content
          }
        })
      }
    },
    async created() {
      let item;
      let token = localStorage.getItem("access");
      let config = {
        headers: {"Authorization" : `Bearer ${token}`}
      }
        let link = this.$store.state.URL + "api/admin/get-requests";

        console.log(link)
        let response = await axios.post(link , {}, config)
        let items = await response.data.data;

        console.log(items)
        this.pending = items.pending;
        this.stopped = items.stopped;
        this.running = items.running;
    }
  }
</script>
