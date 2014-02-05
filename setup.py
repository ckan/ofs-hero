from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='ofs-hero',
      version=version,
      description="Regnerate persisted_state.json from a ckan instance",
      long_description="""\
Renerate persisted_state.json from a ckan instance.""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='ckan, script',
      author='Nigel Babu',
      author_email='nigel.babu@okfn.org',
      url='http://github.com/ckan/ofs-hero',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      [paste.paster_command]
      regenerate = ofshero.commands:Regenerate
      """,
      )
