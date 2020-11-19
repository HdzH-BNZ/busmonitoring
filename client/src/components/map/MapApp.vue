<template>
  <v-container>
      <v-layout>
            <l-map
                :zoom="zoom"
                :center="center"
                :options="mapOptions"
                style="height: 500px; border: 2px solid green;"
            >
                <l-control-layers position="topright"></l-control-layers>
                <l-tile-layer
                    v-for="tileProvider in tileProviders"
                    :key="tileProvider.name"
                    :name="tileProvider.name"
                    :visible="tileProvider.visible"
                    :url="tileProvider.url"
                    :attribution="tileProvider.attribution"
                    layer-type="base"
                />

                <l-control position="bottomleft" >
                    <div style="text-align:center;padding:5px;font-size:17px;">Légende</div>
                    <input type="checkbox" name="arrets_bus" id="box1" checked=checked v-on:click="showBusMarker = !showBusMarker">
                    <i class="fas fa-map-marker-alt" style="color:#007ecc; margin:6px;"></i>
                    <span>arrêts de bus</span>
                    <br>
                    <input type="checkbox" name="lignes_bus" id="box2" checked=checked v-on:click="showCacpLignes = !showCacpLignes">
                    <span class="material-icons" style="color:blue;">minimize</span>
                    <span>lignes de bus</span>
                </l-control>

                <l-geo-json 
                    :geojson="cacpLignes"
                    :options="{color: 'blue', weight: '2', opacity:'0.5'}"
                    :visible="showCacpLignes"
                >
                </l-geo-json>

                <v-marker-cluster :options="{foo: 'bar'}">
                    <l-marker 
                            :visible="showBusMarker"
                            :key="index"
                            v-for="(busMarker, index) in busMarkers"
                            :lat-lng="latLng(busMarker.geometry.coordinates[1], busMarker.geometry.coordinates[0])"
                    >
                            <l-popup :options="{maxHeight: '200'}">
                                
                                <div>Exploitant : {{busMarker.properties.nom_exploit}}</div>
                                <div>Nom de l'arrêt : {{busMarker.properties.nom_arret}}</div>
                                <div v-if="busMarker.properties.nom_lignesBis.length>1">
                                     Lignes : 
                                    <li>
                                        <ul :key="index" 
                                            v-for="(ligne, index) in busMarker.properties.nom_lignesBis"
                                            >
                                            • {{ligne}}
                                        </ul>
                                    </li>
                                   
                                </div>
                                <div v-else>
                                    Ligne : {{busMarker.properties.nom_lignesBis}}
                                </div>
                                <div>Nom de la commune : {{busMarker.properties.nom_commune}}</div>
                                <div>Etat de l'arrêt : {{busMarker.properties.etat_arret}}</div>
                                <div>Accès PMR : {{busMarker.properties.acces_pmr}}</div>
                                <div>Marquage au sol : {{busMarker.properties.marquage_sol}}</div>
                                <p></p>
                                <div>Présence :</div>
                                <div>- d'une poubelle : {{busMarker.properties.poubelle}}</div>
                                <div>- d'un banc : {{busMarker.properties.banc}}</div>
                                <div>- d'un toit : {{busMarker.properties.toit}}</div>
                                <div>- des horaires de passage : {{busMarker.properties.horaires}}</div>
                                <div>- des cartes des trajets : {{busMarker.properties.carte_trajets}}</div>                             
                                <p></p>
                                <div>Commentaire : {{busMarker.properties.comment}}</div>
                                <div>Dernière MAJ : {{busMarker.properties.date}}</div>
                                <div>
                                    <img :src="busMarker.properties.img" alt="" width="150" height="150" class="center">
                                </div>
                             
                            </l-popup>
                    </l-marker>
                </v-marker-cluster>
            </l-map>
      </v-layout>
  </v-container>
</template>

<script>
import { latLng } from "leaflet"
import axios from 'axios'
import {LMap, LTileLayer, LMarker, LPopup, LGeoJson, LControl,LControlLayers} from 'vue2-leaflet'
import Vue2LeafletMarkerCluster from 'vue2-leaflet-markercluster'//pr importer le plugin de clustering
import cacpGeojson from '@/data/lignes_cacp.json'

export default {
    components: {
        LMap, 
        LTileLayer,
        LMarker,
        LPopup,
        'v-marker-cluster': Vue2LeafletMarkerCluster,
        LGeoJson,
        LControl,
        LControlLayers,
    },
    mounted(){
        axios.get('http://localhost:8000/api/arrets/?format=json')
         .then(response => {
           this.busMarkers = response.data.features;
           console.log(this.busMarkers)
           console.log(this.busMarkers[0].properties.nom_lignesBis.isArray)
           });
    },
    methods: {
        latLng: function(lat, lng) {//on crée une new fonction qui prendra 2 paramètres
            return L.latLng(lat, lng)//on appelle la méthode latLng()
        },
        },
    data() {
        return {
            busMarkers: [],
            showBusMarker: true,
            cacpLignes: cacpGeojson,
            showCacpLignes: true,
            zoom: 13,
            center: [49.03898, 2.07501],
            url: 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
            attribution:
                '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors',
            mapOptions: {
                attributionControl: true,
            },
            tileProviders: [
                {
                name: 'OpenTopoMap',
                visible: true,
                url: 'https://{s}.tile.opentopomap.org/{z}/{x}/{y}.png',
                attribution:
                    '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>, <a href="http://viewfinderpanoramas.org">SRTM</a> | &copy; <a href="https://opentopomap.org">OpenTopoMap</a> (<a href="https://creativecommons.org/licenses/by-sa/3.0/">CC-BY-SA</a>)',
                },
                {
                name: 'OpenStreetMap',
                visible: false,
                attribution:
                    '&copy; <a target="_blank" href="http://osm.org/copyright">OpenStreetMap</a> contributors',
                url: 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
                },
            ],
        }
    }
}
</script>

<style>
div[class="leaflet-control"] {
    background: rgba(240,240,240,0.8);
    box-shadow: 0 0 15px rgba(0,0,0,0.2);
    border-radius: 5px;
    width: 200px;
    height: 100px;
    padding: 4px 6px;
    font: Arial;
    font-size: 15px;
}
</style>