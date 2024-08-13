from setuptools import Extension
from Cython.Build import cythonize

module_name = "cythontest"

extensions = [
    Extension(name = f"{module_name}.addone", sources = ["src/cythontest/addone.pyx"]),
    Extension(name = f"{module_name}.shopping_list", sources = ["src/cythontest/shopping_list.pyx", "c_lib/items.c"], include_dirs = ["c_lib"]),
]

def build(setup_kwargs):
    setup_kwargs.update(
        {
            "ext_modules": cythonize(extensions),
        }
    )
