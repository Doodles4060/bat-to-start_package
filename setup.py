from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = "\n" + f.read()

VERSION = '0.2.0'
DESCRIPTION = 'Creates batch files for your virtual environments.'
LONG_DESCRIPTION = 'A package for creating batch files for your virtual environments by simply using python -m command'

# Setting up
setup(
    name="battostart",
    version=VERSION,
    author="Doodles4060 (Vladyslav Tsymbalistenko)",
    author_email="doodles4060@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    entry_points={
            'console_scripts': [
                'battostart = battostart.__main__:main'
            ]
        },
    install_requires=[],
    keywords=['battostart', 'batToStart', 'generate batch', 'utility'],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Operating System :: Microsoft :: Windows",
    ]
)
