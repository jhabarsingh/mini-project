<template>
  <v-card
    class="mx-auto overflow-hidden"
    width="256"
  >
    <v-navigation-drawer 
        v-model="$store.state.drawer"
        app
        temporary
    >
      <v-system-bar></v-system-bar>
      <v-list>
        <v-list-item>
          <v-list-item-avatar>
            <v-img src="https://raw.githubusercontent.com/jhabarsingh/SIMADIAN/main/doc/trademark.png"></v-img>
          </v-list-item-avatar>
        </v-list-item>

        <v-list-item link>
          <v-list-item-content>
            <v-list-item-title class="title">
              {{ $store.state.ngo_name }}
            </v-list-item-title>
            <v-list-item-subtitle>{{ $store.state.ngo_title }}</v-list-item-subtitle>
          </v-list-item-content>

          <v-list-item-action>
          </v-list-item-action>
        </v-list-item>
      </v-list>
      <v-divider></v-divider>
      <v-list
        nav
        dense
      >
        <v-list-item-group
          v-model="selectedItem"
          color="primary"
        >
          <v-list-item
            v-for="(item, i) in items"
            :key="i"
            @click="goTo(item.route)"
            :disabled="item.disabled"
          >
            <v-list-item-icon>
              <v-icon v-text="item.icon"></v-icon>
            </v-list-item-icon>

            <v-list-item-content>
              <v-list-item-title v-text="item.text"></v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </v-list-item-group>
      </v-list>
    </v-navigation-drawer>
  </v-card>
</template>


<script>
  export default {
    data: () => ({
      selectedItem: 0,
      items: [
        { text: 'Home', icon: 'mdi-home', route: 'home' , disabled: false},
        { text: 'Deploy Container', icon: 'mdi-cloud-upload', route: 'kube-requirements', disabled: (localStorage.getItem("access") ? false: true) },
      ],
    }),
    props: [
        "drawer",
    ],
    methods: {
      goTo(url) {
        this.$store.state.drawer = !this.$store.state.drawer
        this.$router.push(`/${url}`)
      }
    },
    created() {
      if(this.$store.state.role && this.$store.state.role.toLowerCase() == "admin") {
          this.items.push({ text: 'All Container', icon: 'mdi-cloud-upload', route: 'all-requests', disabled: (localStorage.getItem("access") ? false: true) })
          this.items.push({ text: 'All Users', icon: 'mdi-cloud-upload', route: 'all-users', disabled: (localStorage.getItem("access") ? false: true) })
        }

      else if(this.$store.state.role && this.$store.state.role.toLowerCase() == "user") {
          this.items.push({ text: 'Deployment Status', icon: 'mdi-cloud-upload', route: 'all-user-requests', disabled: (localStorage.getItem("access") ? false: true) })
        }
      }
  }
</script>