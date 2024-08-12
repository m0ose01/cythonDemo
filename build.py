from setuptools import Extension
from Cython.Build import cythonize

module_name = "cythontest"

extensions = [
    Extension(name = f"{module_name}.addone", sources = ["src/cythontest/addone.pyx"])
]

def build(setup_kwargs):
    setup_kwargs.update(
        {
            "ext_modules": cythonize(extensions),
        }
    )
