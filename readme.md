# Pytket-offline-display

This [pytket](https://github.com/CQCL/pytket) extension package provides offline circuit rendering functionality.
To use, first install the package with `pip`:

```shell
pip install pytket-offline-display
```

Then replace the usual `pytket.circuit.display` import with `pytket.extensions.offline_display`. For example:

```python
from pytket.extensions.offline_display import render_circuit_jupyter
from pytket import Circuit

circ = Circuit(2,2)
circ.H(0)
circ.CX(0,1)
circ.measure_all()

render_circuit_jupyter(circ)
```

If you want to control the default options, you can instead load a configurable instance.
(Note that this requires pytket >= 1.15)
```python
from pytket.extensions.offline_display import get_circuit_renderer

circuit_renderer = get_circuit_renderer()
circuit_renderer.set_render_options(zx_style=False)  # set the default options.
circuit_renderer.dark_mode = True  # You can also set them directly.

circuit_renderer.render_circuit_jupyter(circ)
```
