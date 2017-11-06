from setuptools import setup, find_packages
from setuptools.extension import Extension

setup(name='ajnwordcloud',
      version='0.2.2',
      description='simple wordcloud generator',
      url='http://github.com/voiceoftreason/ajnwordcloud',
      author='Andy Newton',
      author_email='voiceoftreason@me.com',
      license='MIT',
      packages=find_packages(),
      install_requires=['pillow', 'numpy>=1.6.1'],
      ext_modules=[Extension("ajnwordcloud.ii_search",
                           ["ajnwordcloud/ii_search.c"],include_dirs=['.'])],
      include_package_data=True,
      zip_safe=False)