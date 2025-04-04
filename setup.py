import os
import subprocess
from setuptools import setup, find_packages
from setuptools.command.build_py import build_py as _build_py

HERE = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(HERE, "README.md")) as f:
    README = f.read()


class build_py(_build_py):
    def run(self):
        # Path to your C source file
        c_file = os.path.join(HERE, "src", "pyvcon", "vcontacts", "Vcontacts.c")
        out_bin = os.path.join(HERE, "src", "pyvcon", "vcontacts", "vcon")
        subprocess.check_call(["gcc", c_file, "-o", out_bin])

        super().run()


setup(
    name="pyvcon",
    version="1.0.2",
    author="Olivier Mailhot",
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
    python_requires=">=3.6",
    cmdclass={"build_py": build_py},  # register the custom build step
)