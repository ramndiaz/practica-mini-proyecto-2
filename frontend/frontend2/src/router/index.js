import Vue from 'vue'
import Router from 'vue-router'
//import HelloWorld from '@/components/HelloWorld'
import Home from '@/components/Home'
import Login from '@/components/Login'
import Dashboard from '@/components/Dashboard'
import Test from '@/components/Test'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
    },
    {
      path: '/dashboard/',
      name: 'Dashboard',
      component: Dashboard
    },
    {
      path: '/login/',
      name: 'login',
      component: Login
    },
    {
      path: '/test/',
      name: 'test',
      component: Test
    }
  ]
})
