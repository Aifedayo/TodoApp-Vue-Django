<template>
  <!-- eslint-disable vue/no-use-v-if-with-v-for,vue/no-confusing-v-for-v-if -->
  <div class="home">
    <legend>
      <h1 class="title">Vuengo</h1>
    </legend>

    <div class="columns">
      <div class="column is-3 is-offset-3">
        <form v-on:submit.prevent="addTask">
          <h2 class="subtitle">Add task</h2>

          <div class="field">
            <label class="label">Title</label>
            <div class="control">
              <input class="input" type="text" v-model="title">
            </div>
          </div>

          <div class="field">
            <label class="label">Description</label>
            <div class="control">
              <input class="input" type="text" v-model="description">
            </div>
          </div>

          <div class="field">
            <label class="label">Status</label>
            <div class="control">
              <div class="select">
                <select v-model="status">
                  <option value="todo">To Do</option>
                  <option value="done">Done</option>
                </select>
              </div>
            </div>
          </div>

          <div class="field">
            <div class="control">
              <button class="button is-link">Submit</button>
            </div>
          </div>
        </form>
      </div>
    </div>

    <div class="columns">
      <div class="column is-5">
        <h2 class="subtitle">To do</h2>

        <div class="todo">
          <div class="card" 
            v-for="task in tasks" 
            v-bind:key="task.id"
          >
            <div v-if="task.status === 'todo'" class="card">
              <div class="card-content">{{ task.title }}</div>
              <div class="card-content">{{ task.description }}</div>
              <footer class="card-footer">
                <a class="card-footer-item" @click="setStatus(task.id, 'done')">Done</a>
              </footer>
            </div>
          </div>
        </div>
      </div>
      <div class="column is-5">
        <h2 class="subtitle">Done</h2>

        <div>
          <div class="card" 
            v-for="task in tasks" 
            v-bind:key="task.id"
          >
            <div v-if="task.status === 'done'" class="done">
              <div class="card-content">{{ task.title }}</div>
              <div class="card-content">{{ task.description }}</div>

              <footer class="card-footer">
                <a class="card-footer-item" @click="setStatus(task.id, 'todo')">To do</a>
              </footer>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>

import axios from 'axios'

export default {
  name: "Home",
  data() {
    return {
      tasks: [],
      title: '',
      description: '',
      status: 'todo',
    }
  },

  mounted() {
    this.getTasks()
  },

  methods: {
    getTasks() {
      axios({
        method: 'get',
        url: 'http://127.0.0.1:8001/tasks/',
        auth: {
          username: 'admin',
          password: 'testing'
        }
      }).then(response => this.tasks = response.data)
    },
    addTask() {
      if (this.description) {
        axios({
          method: 'post',
          url: 'http://127.0.0.1:8001/tasks/',
          data: {
            title: this.title,
            description: this.description,
            status: this.status
          },
          auth: {
            username: 'admin',
            password: 'testing'
          }
        }).then((response) => {
          let newTask = {
            'id': response.data.id,
            'title': this.title,
            'description': this.description,
            'status': this.status
          }

          this.tasks.push(newTask)
          this.title = ''
          this.description = ''
          this.status = 'todo'
        }).catch((error) => {
          console.log(error)
        })
      }
    },

    setStatus(task_id, status) {

      const task = this.tasks.filter(task => task.id === task_id)[0]
      const title = title
      const description = task.description
      axios({
        method: 'put',
        url: 'http://127.0.0.1:8001/tasks/' + task_id + '/',
        headers: {
          'Content-Type': 'application/json',
        },
        data: {
          title: title,
          description: description,
          status: status
        },
        auth: {
          username: 'admin',
          password: 'testing'
        }
      }).then(() => {
        task.status = status
      })
    }
  }
};

</script>

<style lang="scss">

.select, select {
  width: 100%;
}

.card {
  margin-bottom: 20px;
}

.done{
  opacity: 0.4;
}
</style>
