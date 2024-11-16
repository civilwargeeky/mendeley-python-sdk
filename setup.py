# NOTICE: This distribution has been modified from the original, found at https://github.com/Mendeley/mendeley-python-sdk/tree/master

from setuptools import setup

__version__ = None
with open('mendeley/version.py') as f:
    exec(f.read())

setup(
    name='mendeley_fixed',
    version=__version__,
    packages=['mendeley', 'mendeley.models', 'mendeley.resources'],
    url='https://github.com/civilwargeeky/mendeley-python-sdk',
    license='Apache',
    author='Daniel Klinger',
    author_email='civilwargeeky@yahoo.com',
    description='A fork of the Python SDK for the Mendeley API. Includes updates to requirements and forks that were never merged.',

    install_requires=[
        'arrow>=0.4.4',
        'memoized-property>=1.0.2',
        'requests>=2.4.3',
        'requests-oauthlib>=0.4.2',
        'oauthlib>=0.7.2'
    ],

    tests_require=[
        'pytest==2.6.4',
        'vcrpy==1.2.0'
    ],

    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Topic :: Scientific/Engineering",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ]
)
