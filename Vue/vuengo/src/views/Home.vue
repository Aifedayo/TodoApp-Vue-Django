<template>
  <div class="home">
    <legend>
      <h1 class="title">Vuengo</h1>
    </legend>

    <div class="columns">
      <div class="column is-3 is-offset-3">
        <form>
          <h2 class="subtitle">Add task</h2>

          <div class="field">
            <label class="label">Description</label>
            <div class="control">
              <input class="input" type="text">
            </div>
          </div>

          <div class="field">
            <label class="label">Status</label>
            <div class="control">
              <div class="select">
                <select>
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
      <div class="columns is-6">
        <h2 class="subtitle">To do</h2>

        <div class="todo">
          <div class="card">
            <div class="card-content">Task description</div>

            <footer class="card-footer">
              <a class="card-footer-item">Done</a>
            </footer>
          </div>
        </div>
      
        <div class="columns is-6">
          <h2 class="subtitle">Done</h2>

          <div class="todo">
          <div class="card">
            <div class="card-content">Task description</div>

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
      tasks: []
    }
  },

  mounted() {
    this.getTask()
  },

  methods: {
    getTask() {
      axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/tasks/',
        auth: {
          username: 'admin',
          password: 'testing'
        }
      }).then(respond => this.tasks = response.data)
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
