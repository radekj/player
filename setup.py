import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

setup(name='player',
      version='0.0',
      description='player',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      )
