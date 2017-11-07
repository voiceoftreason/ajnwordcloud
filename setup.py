from setuptools import setup, find_packages
from setuptools.extension import Extension

long_desc = 'ajnwordcloud - styled wordclouds in python using integral images for placement.'

setup(name='ajnwordcloud',
      version='0.2.3',
      description='simple wordcloud generator', 
      long_description=long_desc,
      url='http://github.com/voiceoftreason/ajnwordcloud',
      author='Andy Newton',
      author_email='voiceoftreason@me.com',
      license='MIT',
      classifiers=[
        'Development Status :: 4 - Beta',
        'Topic :: Multimedia :: Graphics',
        'Topic :: Multimedia :: Graphics :: Presentation',
        'Topic :: Text Processing',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        ],
      packages=find_packages(),
      install_requires=['pillow', 'numpy'],
      ext_modules=[Extension("ajnwordcloud.ii_search",
                           ["ajnwordcloud/ii_search.c"],include_dirs=['.'])],
      include_package_data=True,
      zip_safe=False)