from setuptools import setup, Distribution, find_packages
import platform

libExt = '.so'

if platform.system() == 'Windows':
  libraryFilename = '.dll'

  
with open("README.md", "r") as fh:
    long_description = fh.read()

    
setup(
    name="mesh_renderer",
    version="0.0.3",
    author="Multiple Authors",
    author_email="NA",
    description="Differential renderer for Tensorflow",
    long_description=long_description,
    url="",
    packages=find_packages(),
    package_data={
        'mesh_renderer': [libraryFilename + libExt],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
)