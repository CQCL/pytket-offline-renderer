import 'pytket-circuit-renderer/dist/pytket-circuit-renderer.css'
import { createApp } from 'vue'
import CircuitDisplayContainer from 'pytket-circuit-renderer'


// Create the root Vue component
function displayCircuit () {
  const app = createApp({
    delimiters: ['[[#', '#]]'],
    components: { CircuitDisplayContainer },
    data () {
      return {
        initRenderOptions: displayOptions, // inserted by jinja in parent
      }
    }
  })
  app.config.unwrapInjectedRef = true
  app.mount('#circuit-display-vue-container-'+circuitRendererUid)  // inserted by jinja
  return app
}

if (typeof window.pytketCircuitDisplays === "undefined") {
    window.pytketCircuitDisplays = {};
}
window.pytketCircuitDisplays[circuitRendererUid] = displayCircuit()
