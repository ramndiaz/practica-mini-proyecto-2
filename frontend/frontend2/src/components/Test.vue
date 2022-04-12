<template>
  <div class="test">
    <h1>{{ msg }}</h1>
    <table class="table table-bordered table-dark">
      <thead>
        <tr>
          <th scope="col">name</th>
          <th scope="col">email</th>
          <th scope="col">username</th>
          <th scope="col">authenticated</th>
          <th scope="col">current_focus_time</th>
          <th scope="col">current_break_time</th>
          <th scope="col">record_focus_time</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="student in todos" :key="student.id">
          <!-- <th scope="row">{{user.id}}</th> -->
          <td>{{student.name}}</td>
          <td>{{student.email}}</td>
          <td>{{student.username}}</td>
          <td>{{student.authenticated}}</td>
          <td>{{student.current_focus_time}}</td>
          <td>{{student.current_break_time}}</td>
          <td>{{student.record_focus_time}}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'Test',
  data () {
    return {
      msg: 'Test Component',
      todos:null
    }
  },
  mounted(){
    //console.log('mounted')
    this.getStudents();
  },
  methods:{
    getStudents(){
      console.log('students')
      axios
        .get('http://localhost:5000/students')
        .then( response => {
          this.todos=response.data
        })
        .catch( e=> console.log(e))
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.test{
  background-color: aqua;
  color:black;
}
</style>
