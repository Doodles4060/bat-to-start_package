from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = "\n" + f.read()

VERSION = '0.0.1'
DESCRIPTION = 'Create batch files for your virtual environments'
LONG_DESCRIPTION = 'A package for creating batch files for your virtual environments by simply using python -m command'

# Setting up
setup(
    name="bat-to-start_package",
    version=VERSION,
    author="Doodles4060 (Vladyslav Tsymbalistenko)",
    author_email="doodles4060@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=['bat-to-start_package', 'bat-to-start', 'batToStart', 'bat to start', 'generate batch', 'utility'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
