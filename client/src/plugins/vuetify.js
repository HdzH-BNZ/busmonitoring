import Vue from 'vue'
import Vuetify from 'vuetify'
import colors from 'vuetify/lib/util/colors'
import 'vuetify/dist/vuetify.min.css'
import '@fortawesome/fontawesome-free/css/all.css'
import 'material-design-icons-iconfont/dist/material-design-icons.css'

Vue.use(Vuetify)

const opts = {
    icons: {
        iconfont: 'md' || 'fa'
    },
    themes: {
        light: {
            background: colors.blue.accent4
        },
        dark: {
            bakground: colors.blue.ligthen5
        }
    }
}

export default new Vuetify(opts)