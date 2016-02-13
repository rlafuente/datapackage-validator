#!/usr/bin/env python

from distutils.core import setup

setup(name='datapkg-validator',
      version='0.1',
      description='Validate data packages on the commandline using datapackage-validate',
      author='Ricardo Lafuente',
      author_email='r@manufacturaindependente.org',
      url='http://github.com/rlafuente/datapackage-validator/',
      download_url='https://github.com/rlafuente/datapackage-validator/tarball/master',
      packages=['datapackage-validator'],
      license="GPL",
      install_requires=['datapackage-validate'],
      )
