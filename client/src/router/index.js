import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import HomeLogin from '../views/HomeLogin.vue'
import KubeRequirements from '../views/KubeRequirements.vue'
import AllRequests from '../views/AllRequests.vue'
import AllUserRequests from '../views/AllUserRequests.vue'
import AllUsers from '../views/AllUsers.vue'

import store from '../store/index.js';

import axios from 'axios';


Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/home',
    name: 'HomeLogin',
    component: HomeLogin
  },
  {
    path: '/kube-requirements',
    name: 'KubeRequirements',
    component: KubeRequirements
  },
  {
    path: '/all-requests',
    name: 'AllRequests',
    component: AllRequests
  },
  {
    path: '/all-user-requests',
    name: 'AllUserRequests',
    component: AllUserRequests
  },
  {
    path: '/all-users',
    name: 'AllUsers',
    component: AllUsers
  },
  {
    path: '/admin',
    name: 'Admin',
    component: KubeRequirements,
    component: () => import('../views/Admin.vue'),
  },
  {
    path: '/register',
    name: 'Register',
    component: () => import('../views/Register.vue'),
    async beforeEnter(to, from, next) {
      
      if(localStorage.getItem("access")) {
        //check token validation
        let url = store.state.URL + "api/token/verify/"
        
        try {
          let data = await axios.post(url, {
            "token": localStorage.getItem("access")
          });

          data = data.data;
          
          if(Object.keys(data).length === 0) {
            router.push('/home')
            return;
          }
        }
        catch(err) {
          // ERROR
        }
        localStorage.clear();
        next();
      }
      else {
        next();
      }
    }
  },
  {
    path: '/login',
    name: 'Login',
    component: () => import('../views/Login.vue'),
    async beforeEnter(to, from, next) {
      
      if(localStorage.getItem("access")) {
        //check token validation
        let url = store.state.URL + "api/token/verify/"
        
        try {
          let data = await axios.post(url, {
            "token": localStorage.getItem("access")
          });

          data = data.data;
          
          if(Object.keys(data).length === 0) {
            router.push('/home')
            return;
          }
        }
        catch(err) {
          // ERROR
        }
        localStorage.clear();
        next();
      }
      else {
        next();
      }
    }
  },
  {
    path: '/update-profile',
    name: 'UserUpdate',
    component: () => import('../views/UserUpdate.vue'),
    async beforeEnter(to, from, next) {
      
      if(localStorage.getItem("access")) {
        //check token validation
        let url = store.state.URL + "api/token/verify/"
        
        try {
          let data = await axios.post(url, {
            "token": localStorage.getItem("access")
          });

          data = data.data;
          
          if(Object.keys(data).length === 0) {
            next();
            return;
          }
        }
        catch(err) {
          // ERROR
        }
        localStorage.clear();
        router.push("/login");
      }
      else {
        router.push("/login");
      }
    }
  },
  {
    path: '/logout',
    name: 'Logout',
    component: () => import('../views/Logout.vue'),
    async beforeEnter(to, from, next) {
      
      if(localStorage.getItem("access")) {
        localStorage.clear();
        next();
      }
      else {
        router.push("/login");
      }
    }
  },
  {
    path: '/test',
    name: 'Test',
    component: () => import('../components/others/Test.vue')
  },
  {
    path: '*',
    name: 'NotFound',
    component: () => import('../views/NotFound.vue')
  },

]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
