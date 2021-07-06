import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import router from '../router/index.js'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    ngo_name: "MINI PROJECT",
    ngo_title: "let's help other",
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
    username: "MINI PROJECT",
    message: "Hey!",
    selectedItem: null,
    isLoggedin: (localStorage.getItem('access') ? true: false),
<<<<<<< HEAD
    role: localStorage.getItem('user') ? JSON.parse(localStorage.getItem('user')).role : null
=======
    role: localStorage.getItem('user') && JSON.parse(localStorage.getItem('user')).role
>>>>>>> 6afffd4f2145c51c340b01af3cbdd82edd009882
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
        let res = await axios.post(state.URL + 'users/create/', data)
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
        localStorage.setItem("refresh", res.refresh);
        localStorage.setItem("access", res.access);
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
