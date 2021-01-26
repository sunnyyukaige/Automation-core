from setuptools import setup, find_packages
import codecs
import os
import re

with open("README.md", "r") as fh:
    long_description = fh.read()

package_name = 'appiumcore'

setup(
    name=package_name,
    version="0.0.16",
    author="Sunny Yu",
    author_email="sunny.yu@farfetch.com",
    description="foundation tech layer for the appium",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sunnyyukaige/Automation-core",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    )
