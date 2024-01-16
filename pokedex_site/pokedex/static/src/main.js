import { createApp } from 'vue/dist/vue.esm-bundler';

import HelloWorld from "./components/HelloWorld.vue";
import Navbar from "./components/Navbar.vue";
import Footer from "./components/Footer.vue";
import Items from "./components/Items.vue";

createApp({
    components: {
        'app-hello-world': HelloWorld,
        'app-navbar': Navbar,
        'app-footer': Footer,
        'app-items': Items,
    }
}).mount('#app')
