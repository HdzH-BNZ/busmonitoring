import Vue from 'vue'
import Router from 'vue-router'
import Accueil from '@/views/Accueil';
import Erreur from '@/views/Erreur';

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Accueil',
      component: Accueil
    },
    {
      path: '/*',
      name: 'Erreur',
      component: Erreur
    },

  ]
})
