<template>
  <v-app>

    <headerApp></headerApp>

    <v-main>
      <router-view/>
    </v-main>

    <footerApp></footerApp>

  </v-app>
</template>

<script>
import headerApp from './components/commons/Header'
import footerApp from './components/commons/Footer'

export default {
  name: 'App',
  components: {
    headerApp,
    footerApp
  }
}
</script>

<style>
@import "../node_modules/leaflet/dist/leaflet.css";
</style>
