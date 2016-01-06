from setuptools import setup, find_packages
import os

version = '1.0'

requires = [
    'setuptools',
]

test_requires = requires + [
    'webtest',
    'python-coveralls',
]

entry_points = {
    'openprocurement.api.plugins': [
        'limited = openprocurement.tender.limited:includeme'
    ]
}

setup(name='openprocurement.tender.limited',
      version=version,
      description="",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
          "License :: OSI Approved :: Apache Software License",
          "Programming Language :: Python",
        ],
      keywords="web services",
      author='Quintagroup, Ltd.',
      author_email='info@quintagroup.com',
      url='https://github.com/openprocurement/openprocurement.tender.limited',
      license='Apache License 2.0',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['openprocurement', 'openprocurement.tender'],
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      extras_require={'test': test_requires},
      entry_points=entry_points)