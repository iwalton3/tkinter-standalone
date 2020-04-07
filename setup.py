from distutils.core import setup, Extension

module1 = Extension('_tkinter',
                    libraries=['tcl8.6', 'tk8.6'],
                    sources=['_tkinter.c'],
                    include_dirs=['/app/include/'])

setup(
    name='tkinter-standalone',
    version='3.7',
    description='Tkinter packaged as an external package for flatpak.',
    ext_modules=[module1],
    packages=["tkinter"]
)
