from setuptools import find_packages
name='sample',
version='1.2.0',
description='A sample Python project',
long_description='''''',
url='https://github.com/pypa/sampleproject',
author='The Python Packaging Authority',
author_email='pypa-dev@googlegroups.com',
license='MIT',
classifiers=[
    # How mature is this project? Common values are
    #   3 - Alpha
    #   4 - Beta
    #   5 - Production/Stable
    'Development Status :: 3 - Alpha',

    # Indicate who your project is intended for
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',

    # Pick your license as you wish (should match "license" above)
     'License :: OSI Approved :: MIT License',

    # Specify the Python versions you support here. In particular, ensure
    # that you indicate whether you support Python 2, Python 3 or both.
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.6',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.2',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
],
keywords='sample setuptools development',
packages=find_packages(exclude=['TheEyes']),
#install_requires=['peppercorn'],
package_data={
    'sample': ['package_data.dat'],
},
data_files=[('my_data', ['data/data_file'])],
