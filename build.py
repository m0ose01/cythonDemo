from setuptools import Extension
from Cython.Build import cythonize

module_name = "cythondemo"

extensions = [
    Extension(name = f"{module_name}.addone", sources = [f"src/{module_name}/addone.pyx"]),
    Extension(name = f"{module_name}.shopping_list", sources = [f"src/{module_name}/shopping_list.pyx", "c_lib/items.c"], include_dirs = ["c_lib"]),
]

def build(setup_kwargs):
    setup_kwargs.update(
        {
            "ext_modules": cythonize(extensions),
        }
    )
