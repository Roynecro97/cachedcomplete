import setuptools
import os

README_PATH = 'README.md'

if os.path.exists(README_PATH):
    with open(README_PATH, 'r') as fd:
        long_description = fd.read()

setuptools.setup(
    name='cachedcomplete',
    version='0.0.1',
    author='',
    author_email='',
    description='Cached wrapper for python argcomplete',
    license='MIT License',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/Roynecro97/cachedcomplete',
    packages=setuptools.find_packages(),
    platforms=['MacOS X', 'Posix'],
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: Implementation :: CPython',
        # 'Programming Language :: Python :: Implementation :: PyPy',
        'Development Status :: 3 - Alpha',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: System :: Shells',
        'Topic :: Terminals'
    ],
    install_requires=[
        'argcomplete==1.11.1'
    ],
    zip_safe=False
)
