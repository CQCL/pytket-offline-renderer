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

import os
import subprocess
import setuptools  # type: ignore
from setuptools import setup
from setuptools.command.build_py import build_py


class NPMBuild(build_py):
    def run(self):
        # Build the circuit renderer app for (offline) inclusion within pytket.
        try:
            out = subprocess.check_output(
                "npm --version", shell=True  # Needed for windows?
            )
        except OSError:
            raise RuntimeError("NPM must be installed to build the circuit renderer.")

        subprocess.run("npm ci", check=True, shell=True)
        subprocess.run("npm run build", check=True, shell=True)

        build_py.run(self)


setup(
    name="pytket-offline-display",
    author="TKET development team",
    author_email="tket-support@cambridgequantum.com",
    python_requires=">=3.9",
    version="0.0.9",
    project_urls={
        "Documentation": "https://cqcl.github.io/tket/pytket/api/index.html",
        "Source": "https://github.com/CQCL/pytket-offline-renderer",
        "Tracker": "https://github.com/CQCL/pytket-offline-renderer/issues",
    },
    description="Python module for displaying pytket circuits when offline.",
    long_description=open("readme.md", "r").read(),
    long_description_content_type="text/markdown",
    license="Apache 2",
    packages=setuptools.find_namespace_packages(),
    install_requires=[
        "jinja2 ~= 3.0",
        "pytket >= 1.31.1",
    ],
    cmdclass={
        "build_py": NPMBuild,
    },
    include_package_data=True,
    zip_safe=False,
)
