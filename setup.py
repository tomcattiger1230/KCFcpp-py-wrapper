# -*-coding:utf-8-*-
# cython:language_level=3

from distutils.core import setup, Extension
from Cython.Distutils import build_ext
import numpy
import platform

if platform.system() == 'Windows':
	# libdr = ['C:\\Develop\\opencv_win\\build\\x64\\vc16\\lib']
	# incdr = [numpy.get_include(), 'C:\\Develop\\opencv_win\\build\\include']
	libdr = ['C:\\Develop\\opencv\\x64\\vc16\\lib']
	incdr = [numpy.get_include(), 'C:\\Develop\\opencv\\include']
    # cvlib = ['opencv_world340d']
	ext = [
	Extension('cvt', ['python/cvt.pyx'],
		language = 'c++',
		# extra_compile_args = ['-std=c++11'],
		include_dirs = incdr,
		library_dirs = libdr,
		libraries = ['opencv_core346']),
	Extension('KCF', ['python/KCF.pyx', 'src/kcftracker.cpp', 'src/fhog.cpp'],
		language = 'c++',
		# extra_compile_args = ['-std=c++11'],
		include_dirs = incdr,
		library_dirs = libdr,
		libraries = ['opencv_core346', 'opencv_imgproc346'])]
else:
	libdr = ['/usr/local/lib']
	incdr = [numpy.get_include(), '/usr/local/include/']
	ext = [
		Extension('cvt', ['python/cvt.pyx'],
			language = 'c++',
			extra_compile_args = ['-std=c++11'],
			include_dirs = incdr,
			library_dirs = libdr,
			libraries = ['opencv_core']),
		Extension('KCF', ['python/KCF.pyx', 'src/kcftracker.cpp', 'src/fhog.cpp'],
			language = 'c++',
			extra_compile_args = ['-std=c++11'],
			include_dirs = incdr,
			library_dirs = libdr,
			libraries = ['opencv_core', 'opencv_imgproc'])
	]

setup(
	name = 'app',
	cmdclass = {'build_ext':build_ext},
	ext_modules = ext
)

#python setup.py build_ext --inplace
