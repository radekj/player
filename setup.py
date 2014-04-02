import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.md')) as f:
    README = f.read()
with open(os.path.join(here, 'CHANGES.txt')) as f:
    CHANGES = f.read()

requires = [
    'pokereval',
]

setup(name='player',
      version='0.1',
      description='Poker player application',
      long_description=README + '\n\n' + CHANGES,
      author='Radosław Jankiewicz',
      author_email='radoslaw.jankiewicz@gmail.com',
      url='',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      tests_require=requires,
      )
