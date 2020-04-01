import setuptools
import os

README_PATH = 'README.md'

if os.path.exists(README_PATH):
    with open(README_PATH, 'r', encoding='utf-8') as fd:
        long_description = fd.read()

setuptools.setup(
    name='cachedcomplete',
    version='1.0.1',
    url='https://github.com/Roynecro97/cachedcomplete',
    project_urls={
        "Source Code": 'https://github.com/Roynecro97/cachedcomplete'
    },
    license='MIT License',
    author='',
    author_email='',
    description='Cached wrapper for python argcomplete',
    long_description=long_description,
    long_description_content_type='text/markdown',
    install_requires=[
        'argcomplete==1.11.1'
    ],
    packages=setuptools.find_packages(exclude=['test']),
    zip_safe=False,
    include_package_data=True,
    platforms=['MacOS X', 'Posix'],
    test_suite='test',
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
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
        'Development Status :: 4 - Beta',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: System :: Shells',
        'Topic :: Terminals'
    ]
)
