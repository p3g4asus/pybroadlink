'''
Created on 25 apr 2019

@author: Matteo
'''
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pybroadlink",
    version="1.5",
    author="p3g4asus",
    author_email="fulminedipegasus@gmail.com",
    description="Asyncio module for Broadlink devices control",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/p3g4asus/pybroadlink",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
