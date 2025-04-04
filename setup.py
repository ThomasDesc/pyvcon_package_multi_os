import os
import subprocess
from setuptools import setup, find_packages
from setuptools.command.build_py import build_py as _build_py

HERE = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(HERE, "README.md")) as f:
    README = f.read()

setup(
    name="pyvcon_multi_os",
    version="1.0.2",
    author="test",
    description="Python wrapper for Vcontacts",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/gregorpatof/pyvcon_package",
    packages=find_packages("src"),
    package_dir={"": "src"},
    include_package_data=True,
    package_data={'pyvcon': ['vcontacts/*']},  # include the compiled binary
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6"
)