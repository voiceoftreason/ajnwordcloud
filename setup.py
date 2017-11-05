from setuptools import setup, find_packages
from setuptools.extension import Extension

setup(name='ajnwordcloud',
      version='0.1',
      description='simple wordcloud generator',
      url='http://github.com/voiceoftreason/ajnwordcloud',
      author='Andy Newton',
      author_email='voiceoftreason@me.com',
      license='MIT',
      packages=find_packages(),
      install_requires=['numpy>=1.6.1', 'pillow'],
      ext_modules=[Extension("ajnwordcloud.ii_search",
                           ["ajnwordcloud/ii_search.c"],include_dirs=['.'])],
       zip_safe=False)