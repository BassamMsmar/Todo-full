<template>
  <body>
    <div class="container">
      <h2 class="text-center pt-4 text-white">Todo App</h2>
      <div class="d-flex mt-5">
        <input
          type="text"
          placeholder="Enter Task"
          class="form-control"
          v-model="task"
        />
        <button type="button" class="btn btn-warning ms-3" @click="submitTask">
          Add
        </button>
      </div>
      <div class="mt-5">
        <table class="table table-hover">
          <thead class="table-light">
            <tr>
              <th scope="col">Task</th>
              <th scope="col">Status</th>
              <th scope="col">#</th>
              <th scope="col">#</th>
            </tr>
          </thead>

          <tbody>
            <tr v-for="task in tasks" :key="task.id">
              <th scope="row">
                <span :class="{ finished: task.status == 'doing' }">
                  {{ task.name }}
                </span>
              </th>

              <th>
                <span 
                @click="changesStatus(task.id)"
                class="poinyrt"
                :class="{
                  'text-danger': task.status == 'todo',
                  'text-warning': task.status == 'inprogress',
                  'text-success': task.status == 'doing',
                }"
                >
                  {{ task.status }}
                </span>
              </th>

              <th>
                <span @click="editTask(task.id)">
                  <i class="fa-regular fa-pen-to-square"></i>
                </span>
              </th>

              <th>
                <span @click="deleteTask(task.id)">
                  <i class="fa-regular fa-trash-can"></i>
                </span>
              </th>

            </tr>
          </tbody>
        </table>
      </div>

      
    </div>
  </body>
</template>

<script>
import axios from 'axios';

export default {
  name: "todo-app",
  props: {
    msg: String,
  },
  data() {
    return {
      task: "",
      isEditTask: null,
      availableStatus:['todo', 'inprogress', 'doing'],
      tasks: [],
    };
  },

  mounted() {
    this.getTasks();
  },

  methods: {
    getTasks(){
      axios({
        method: "get",
        url: "http://127.0.0.1:8000/tasks/api/",
        }).then(response =>this.tasks = response.data)
    },
    submitTask() {
      if (this.task == 0) return;
      if (this.isEditTask==null){

        axios({
        method: "post",
        url: "http://127.0.0.1:8000/tasks/api/",
        data: {
          name: this.task,
          status: 'todo',
        }
        }).then(() => {this.getTasks()})
          
       
      }
      else{
        this.tasks.find(task => task.id === this.isEditTask).name  = this.task
      }
      
      this.task = ""
      this.isEditTask = null
    },
    changesStatus(index){
      let newIndex = this.availableStatus.indexOf(this.tasks.find(task => task.id === index).status)
      if (++newIndex > 2 ) newIndex = 0
      this.tasks.find(task => task.id === index).status = this.availableStatus[newIndex]
    },
    deleteTask(index) {
      axios({
        method: "delete",
        url: 'http://127.0.0.1:8000/tasks/api/'+index+'/',
      }).then(() => {
        this.getTasks();
      })
    },
    editTask(index) {
      this.task = this.tasks.find(task => task.id === index).name
      this.isEditTask = index
    },
  },
};
</script>

<style scoped>
body {
  background-color: rgb(26, 69, 105);
  width: 100%;
  height: 1200px;
}
.poinyrt {
  cursor: pointer;
}
.finished {
  text-decoration: line-through;
}
</style>
