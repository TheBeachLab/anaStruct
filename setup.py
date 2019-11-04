
import sys
from setuptools import setup

try:
    from Cython.Build import cythonize
    em = cythonize(['anastruct/cython/cbasic.pyx',
                    'anastruct/fem/cython/celements.pyx'])
except Exception:
    em = []

if sys.version_info[0] == 3 and sys.version_info[1] < 5:
    sys.exit('Sorry, Python < 3.5 is not supported')

setup(
    name='pySTRAN',
    version='1.01',
    description='structural engineering package',
    author='Francisco Sanchez (forked from Ritchie Vink)',
    author_email='hola@beachlab.org',
    url='http://beachlab.org',
    download_url='https://github.com/thebeachlab/pySTRAN',
    license='GPL-3.0',
    packages=['anastruct', 'anastruct.fem', 'anastruct.fem.system_components', 'anastruct.fem.examples',
              'anastruct.material', 'anastruct.cython', 'anastruct.fem.cython', 'anastruct.fem.plotter',
              'anastruct.fem.util', 'anastruct.sectionbase'],
    package_data={'': ['*.xml']},
    package_dir='',
    install_requires=[
        'matplotlib>=3.0, <3.1',
        'numpy>=1.15.4',
        'scipy>=1.1.0'
    ],
    ext_modules=em

)