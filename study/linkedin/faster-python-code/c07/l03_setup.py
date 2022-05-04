"""Setup for sqrt lib"""

from distutils.core import setup
from Cython.Build import cythonize
from pathlib import Path

_FILE_NAME = 'l03_cysqrt.pyx'
_FILE_PATH = f"{Path(__file__).parent.resolve()}/{_FILE_NAME}"

setup(
    ext_modules=cythonize(_FILE_PATH),
)
