import os
from setuptools import setup


# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="pyjd",
    version="1.0.11",
    author="Philipp Glaum",
    author_email="p@pglaum.de",
    description=("A wrapper for the JDownloader API"),
    license="GPLv3",
    keywords="api jdownloader",
    url="https://git.sr.ht/~pglaum/pyjd-api",
    packages=["pyjd"],
    install_requires=["requests", "pydantic==1.10.10", "pycryptodome"],
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)
