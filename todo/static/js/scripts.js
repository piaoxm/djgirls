// Full spec-compliant TodoMVC with localStorage persistence
// and hash-based routing in ~120 effective lines of JavaScript.

// localStorage persistence
Vue.prototype.$http = axios;
// axios라는 HTTp 클라이언트 라이브러리 입니다. Promise 베이스이기 때문에 사용하기 까다롭지만
// Vue.js의 HTTP 클라이언트로 가장 많이 사용됩니다. axios를 Vue에서 기본으로 사용하도록 prototype에 추가

var todoStorage = {
    // 가장 많은 변경이 있는 부분입니다. 원래 코드는 데이터를 웹 스토리지에 저장하는데 이를 장고를 통해
    // 데이터베이스에 저장하고 꺼내와야 하기 때문에 axios를 사용해서 데이터를 저장하고 Vue.js의 기본 통신
    // 메서드를 사용해 데이터를 얻어오도록 코드를 변경햇습니다. Promise 패턴을 사용하는 fetch부분은
    // 자바스크립트가 익숙하지 않으신 분들에게는 어려울 수 있습니다.
  fetch: function (app) {
    app.fetch('fetch/').then((response) => {
        return response.json();
    })
    .then((todos) => {
        todos.forEach(function (todo, index) {
          todo.id = index
        });
        this.uid = todos.length
        app.app.todos = todos;

    });
    return []
  },
  save: function (todos) {
    app.$http.post('save/',{todos:todos});
  }
}

// visibility filters
var filters = {
  all: function (todos) {
    return todos
  },
  active: function (todos) {
    return todos.filter(function (todo) {
      return !todo.completed
    })
  },
  completed: function (todos) {
    return todos.filter(function (todo) {
      return todo.completed
    })
  }
}

// app Vue instance
var app = new Vue({
    // Vus.js 앱을 작성합니다.
  // app initial state
  delimiters: ['[[', ']]'], // 장고 템플릿 엔진과 충돌을 막기 위해 데이터를 적용하는 부분을 [[ ]] 로 변경
  data: {
    todos: todoStorage.fetch(this),
    newTodo: '',
    editedTodo: null,
    visibility: 'all'
  },

  // watch todos change for localStorage persistence
  watch: {
    todos: {
      handler: function (todos) {
        todoStorage.save(todos)
      },
      deep: true
    }
  },

  // computed properties
  // http://vuejs.org/guide/computed.html
  computed: {
    filteredTodos: function () {
      return filters[this.visibility](this.todos)
    },
    remaining: function () {
      return filters.active(this.todos).length
    },
    allDone: {
      get: function () {
        return this.remaining === 0
      },
      set: function (value) {
        this.todos.forEach(function (todo) {
          todo.completed = value
        })
      }
    }
  },

  filters: {
    pluralize: function (n) {
      return n === 1 ? 'item' : 'items'
    }
  },

  // methods that implement data logic.
  // note there's no DOM manipulation here at all.
  methods: {
    addTodo: function () {
      var value = this.newTodo && this.newTodo.trim()
      if (!value) {
        return
      }
      this.todos.push({
        id: todoStorage.uid++,
        title: value,
        completed: false
      })
      this.newTodo = ''
    },

    removeTodo: function (todo) {
      this.todos.splice(this.todos.indexOf(todo), 1)
    },

    editTodo: function (todo) {
      this.beforeEditCache = todo.title
      this.editedTodo = todo
    },

    doneEdit: function (todo) {
      if (!this.editedTodo) {
        return
      }
      this.editedTodo = null
      todo.title = todo.title.trim()
      if (!todo.title) {
        this.removeTodo(todo)
      }
    },

    cancelEdit: function (todo) {
      this.editedTodo = null
      todo.title = this.beforeEditCache
    },

    removeCompleted: function () {
      this.todos = filters.active(this.todos)
    }
  },

  // a custom directive to wait for the DOM to be updated
  // before focusing on the input field.
  // http://vuejs.org/guide/custom-directive.html
  directives: {
    'todo-focus': function (el, binding) {
      if (binding.value) {
        el.focus()
      }
    }
  }
})

// handle routing
function onHashChange () {
  var visibility = window.location.hash.replace(/#\/?/, '')
  if (filters[visibility]) {
    app.visibility = visibility
  } else {
    window.location.hash = ''
    app.visibility = 'all'
  }
}

window.addEventListener('hashchange', onHashChange)
onHashChange()

// mount
app.$mount('.todoapp')