<template>
  <v-footer
        absolute inset app 
        height="100" width="auto" dark=""
        class="green white--text text-center"
    >
      <v-container>
          <v-layout columns align-center>
          <v-flex
                v-for="(lien, index) in liens" 
                :key="index"
                router :to="lien.url"
            >
              <a :href="lien.url" target="_blank">
                  <v-btn
                    elevation="0" 
                    class="green"
                    >
                      <v-icon>
                          {{lien.icone}}
                      </v-icon>
                  </v-btn>
              </a>
              <div>
                  {{lien.texte}}
              </div>
          </v-flex>
          </v-layout>
      </v-container>
  </v-footer>
</template>

<script>
export default {
    data() {
        return {
            liens: [
                { icone: "fab fa-linkedin", texte: "Linkedin", url:"https://www.linkedin.com/in/hicham-benza%C3%AFm-devetsig/"},
                { icone: "fab fa-gitlab", texte: "Gitlab", url:"https://gitlab.com/devetsig"},
                { icone: "fas fa-globe-europe", texte: "VeilleCarto", url:"https://veillecarto2-0.fr/author/hbel94/"}
                ],
        }
    }

}
</script>

<style>

</style>