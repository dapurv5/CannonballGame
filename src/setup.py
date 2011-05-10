__author__="apurv"
__date__ ="$May 10, 2011 11:06:41 AM$"

from setuptools import setup,find_packages

setup (
  name = 'CannonballGame',
  version = '0.1',
  packages = find_packages(),

  # Declare your packages' dependencies here, for eg:
  install_requires=['foo>=3'],

  # Fill in these to make your Egg ready for upload to
  # PyPI
  author = 'apurv',
  author_email = 'dapurv5@gmail.com',

  summary = 'Just another Python package for the cheese shop',
  url = '',
  license = '',
  long_description= 'Long description of the package',

  # could also include long_description, download_url, classifiers, etc.

  
)