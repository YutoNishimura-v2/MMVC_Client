from distutils.core import setup
from Cython.Build import cythonize
import numpy

setup(
  name = 'monotonic_align',
  ext_modules = cythonize("/home/yuto_nishimura/workspace/python/yellston/MMVC/MMVC_Client/python/monotonic_align/core.pyx"),
  include_dirs=[numpy.get_include()]
)
