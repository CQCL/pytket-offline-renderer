# Copyright 2019-2023 Cambridge Quantum Computing
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Display a circuit as html locally."""

import os
import tempfile
import time
from typing import Optional, cast
from jinja2 import PrefixLoader, FileSystemLoader, ChoiceLoader, Environment

from pytket.circuit import Circuit  # type: ignore
from pytket.circuit.display import (
    RenderCircuit,
    IncludeRawExtension,
    CircuitRenderer,
    html_loader,
    js_loader,
)


class OfflineRenderer(CircuitRenderer):
    """Class to manage circuit rendering within a given jinja2 environment."""

    def render_circuit_as_html(
        self, circuit: RenderCircuit, jupyter: bool = False
    ) -> Optional[str]:
        """
        Render a circuit as HTML for inline display.

        :param circuit: the circuit to render.
        :param jupyter: set to true to render generated HTML in cell output.
        """
        html = super().render_circuit_as_html(circuit, jupyter=False)

        if jupyter:
            # If we are in a notebook, we can tell jupyter to display the html.
            # We don't import at the top in case we are not in a notebook environment.
            import warnings
            from IPython.display import (  # type: ignore
                HTML,
                display,
            )  # pylint: disable=C0415
            # Output is large, so must serve it from a file.
            fp = tempfile.NamedTemporaryFile(
                mode="w", suffix=".html", delete=False, dir=os.getcwd()
            )
            fp.write(cast(str, html))
            fp.close()
            try:
                with warnings.catch_warnings(record=True):
                    display(HTML(
                        f'<iframe src="./{os.path.relpath(fp.name)}" width="100%" height="200px" '
                        f'style="border: none; outline: none; resize: vertical; overflow: auto">'
                        f'</iframe>'
                    ))
                return None
            finally:
                # Wait to make sure the file has time to be loaded first.
                time.sleep(5)
                os.remove(fp.name)
        return html


# Set up jinja to access our templates
dirname = os.path.dirname(__file__)

# Loader falls back on base display module if not overriden.
loader = PrefixLoader({
    'html': ChoiceLoader([
        FileSystemLoader(searchpath=os.path.join(dirname, "static")),
        html_loader,
    ]),
    'js': ChoiceLoader([
        FileSystemLoader(searchpath=os.path.join(dirname, "dist")),
        js_loader
    ])
})

env = Environment(
    loader=loader, extensions=[IncludeRawExtension]
)

# Expose the rendering methods with the local jinja env.
circuit_renderer = OfflineRenderer(env)

render_circuit_as_html = circuit_renderer.render_circuit_as_html
render_circuit_jupyter = circuit_renderer.render_circuit_jupyter
view_browser = circuit_renderer.view_browser
