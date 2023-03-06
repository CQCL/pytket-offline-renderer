# Pytket-offline-renderer

This [pytket](https://github.com/CQCL/pytket) extension package provides offline circuit rendering functionality.
To use, simply replace the usual `pytket.circuit.display` import with `pytket.extensions.offline_display`, for example:

```python
from pytket.extensions.offline_display import render_circuit_jupyter
from pytket import Circuit

circ = Circuit(2,2)
circ.H(0)
circ.CX(0,1)
circ.measure_all()

render_circuit_jupyter(circ)
```
