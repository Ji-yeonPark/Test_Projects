import '@babel/polyfill'
import Vue from 'vue'
import './plugins/vuetify'
import App from './App.vue'
import router from './router'
import store from './store'

Vue.config.productionTip = false

export const eventBus = new Vue({  // 객체안에 method를 이용하면 eventBus를 매번 선언하지 않아도 됨
  methods: {
    userWasEdited(date) {
      this.$emit('userWasEdited', date)
    }
  }
})

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
