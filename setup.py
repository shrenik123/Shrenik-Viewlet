##############################################################################
#
# Copyright (c) 2006 Zope Foundation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
# This package is developed by the Zope Toolkit project, documented here:
# http://docs.zope.org/zopetoolkit
# When developing and releasing this package, please follow the documented
# Zope Toolkit policies as described by this documentation.
##############################################################################
"""Setup for zope.viewlet package
"""
import os
from setuptools import setup, find_packages

def read(*rnames):
    with open(os.path.join(os.path.dirname(__file__), *rnames)) as f:
        return f.read()

setup(name='zope.viewlet',
      version='4.0.0.dev0',
      author='Zope Foundation and Contributors',
      author_email='zope-dev@zope.org',
      description='Zope Viewlets',
      long_description=(
          read('README.rst')
          + '\n\n' +
          'Detailed Documentation\n' +
          '**********************\n\n'
          + '\n\n' +
          read('src', 'zope', 'viewlet', 'README.txt')
          + '\n\n' +
          read('src', 'zope', 'viewlet', 'directives.txt')
          + '\n\n' +
          read('CHANGES.rst')
          ),
      keywords = "zope web html ui viewlet pattern",
      classifiers = [
          'Development Status :: 5 - Production/Stable',
          'Environment :: Web Environment',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: Zope Public License',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: Implementation :: CPython',
          'Natural Language :: English',
          'Operating System :: OS Independent',
          'Topic :: Internet :: WWW/HTTP',
          'Framework :: Zope3'],
      url='http://pypi.python.org/pypi/zope.viewlet',
      license='ZPL 2.1',
      packages=find_packages('src'),
      package_dir = {'': 'src'},
      namespace_packages=['zope'],
      extras_require = dict(
          test=[
            'zope.testing',
            'zope.size',
            ]),
      install_requires=[
          'setuptools',
          'zope.browserpage>=3.10.1',
          'zope.component',
          'zope.configuration',
          'zope.contentprovider',
          'zope.event',
          'zope.i18nmessageid',
          'zope.interface',
          'zope.location',
          'zope.publisher',
          'zope.schema',
          'zope.security',
          'zope.traversing',
          ],
      tests_require = [
          'zope.size',
          'zope.testing',
          ],
      test_suite = 'zope.viewlet.tests.test_suite',
      include_package_data = True,
      zip_safe = False,
      )
