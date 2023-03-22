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
