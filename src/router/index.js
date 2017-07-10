import Vue from 'vue';
import Router from 'vue-router';
import HomePage from '@/containers/HomePage';
import Room from '@/containers/Room';

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/',
      name: 'index',
      component: HomePage,
    },
    {
      path: '/room/:label',
      name: 'room',
      component: Room,
    },
  ],
});
