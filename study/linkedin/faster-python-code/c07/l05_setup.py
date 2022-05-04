"""Setup script for csqrt.c"""
from distutils.core import setup, Extension
from pathlib import Path

_FILE_NAME = 'l05_csqrt.c'
_FILE_PATH = f"{Path(__file__).parent.resolve()}/{_FILE_NAME}"

setup(
    name='csqrt',
    version='0.1.0',
    description='Demo C module',
    ext_modules=[Extension('csqrt', sources=[_FILE_PATH])],
)
