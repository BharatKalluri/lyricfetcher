"""The Setup for packaging the application."""
from setuptools import setup

setup(name='lyricfetcher',
      version='0.5',
      description='lyricfetcher',
      url='http://github.com/bharatkalluri/lyricfetcher',
      author='Bharat Kalluri',
      author_email='bharatkalluri@protonmail.com',
      license='MIT',
      packages=['lyricfetcher', 'lyricfetcher.sources'],
      zip_safe=False,
      install_requires=[
          'requests',
          'bs4',
          'requests',
          'beautifulsoup4',
          'lxml'
      ],
      entry_points={
          'console_scripts': ['lyricfetcher=lyricfetcher.main:main']
      })
