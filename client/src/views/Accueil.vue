<template>

<v-container>

    <v-container>
        <v-layout column align-start>
            <v-flex mt-2 ml-10>
              <h2 class="grey--text">Evaluation de l'état des arrêts de bus dans l'agglomération de Cergy-Pontoise</h2>
            </v-flex>
        </v-layout>
    </v-container>

    <mapApp></mapApp>

</v-container>
  
</template>

<script>
import mapApp from '../components/map/MapApp'

export default {
    components: {
        mapApp,
    }

}
</script>

<style>

</style>