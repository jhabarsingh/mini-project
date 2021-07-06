import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import router from '../router/index.js'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    ngo_name: "Kubernetes Lab Setup",
    ngo_title: "Kubernetes Lab Setup",
    URL: "http://localhost:8000/",
    drawer: null,
    user: null,
    dialog: false, 
    dialogDetail: {
      "heading": "Instructions",
      "details": [
        "Hi"
      ]
    },
    username: "Kubernetes Lab Setup",
    message: "Hey!",
    selectedItem: null,
    isLoggedin: (localStorage.getItem('access') ? true: false),
    role: localStorage.getItem('user') ? JSON.parse(localStorage.getItem('user')).role : null
  },
  getters: {

  },
  mutations: {
    changeDialog(state, {heading, details}) {
      state.dialogDetail.heading = heading;
      state.dialogDetail.details = details; 
    }
  },
  actions: {
    async userRegister({commit, state}, data) {
      try {
        let res = await axios.post(state.URL + 'api/auth/signup', data)
        return res.data;
      } catch (err) {
        throw err;
      }
    },

    async userLogin({commit, state}, data) {
      try {
        console.log(data);
        let res = await axios.post(state.URL + 'api/auth/signin', data)
        res = res.data
        console.log(res);
        // localStorage.setItem("refresh", res.refresh);
        localStorage.setItem("access", res.accessToken);
        localStorage.setItem("user", JSON.stringify(res.user));
        state.role = res.user.role;
        return res;
      } catch (err) {
        if(err.response) {
            console.log(err.response); 
        }
        throw err;
      }
    },

    async verifyToken({commit, state}, data) {
      try {
        console.log(data);
        let res = await axios.post(state.URL + 'api/token/verify/', data)
        res = res.data;

        return res;
      } catch (err) {
        if(err.response) {
            console.log(err.respons)
        }
        throw err;
      }
    },

    userLogout({commit, state}, data) {

    }
  },
  modules: {
  }
})
