# -*- coding:utf-8 -*-
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pydicom-tools",
    version="0.1.2",
    author="Akihisa Wakita",
    author_email="wakita84@gmail.com",
    description="Tools for dicom RT analysis with pydicom",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/wkt84/pydicom_tools",
    packages=setuptools.find_packages(),
    install_requires=[
        "pydicom",
        "numpy",
        "itk"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)