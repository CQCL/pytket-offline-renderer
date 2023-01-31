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
from jinja2 import PrefixLoader, FileSystemLoader, ChoiceLoader, Environment

from pytket.circuit import Circuit  # type: ignore
from pytket.circuit.display import (
    IncludeRawExtension,
    CircuitRenderer,
    html_loader,
    js_loader,
)


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
circuit_renderer = CircuitRenderer(env)

render_circuit_as_html = circuit_renderer.render_circuit_as_html
render_circuit_jupyter = circuit_renderer.render_circuit_jupyter
view_browser = circuit_renderer.view_browser
