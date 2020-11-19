// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import vuetify from './plugins/vuetify'
import L from 'leaflet'
import 'leaflet/dist/leaflet.css'
import axios from 'axios'
import "leaflet.markercluster/dist/MarkerCluster.css";//générer les clusters, leurs couleurs/animations
import "leaflet.markercluster/dist/MarkerCluster.Default.css";


delete L.Icon.Default.prototype._getIconUrl  
L.Icon.Default.mergeOptions({  
  iconRetinaUrl: require('leaflet/dist/images/marker-icon-2x.png'),  
  iconUrl: require('leaflet/dist/images/marker-icon.png'),  
  shadowUrl: require('leaflet/dist/images/marker-shadow.png')  
})


Vue.config.productionTip = false

Vue.use(axios)

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  vuetify,
  components: { App },
  template: '<App/>'
})
