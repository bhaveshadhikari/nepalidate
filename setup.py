from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="samaya",
    version="0.1.1",
    author="Bhavesh Adhikari",
    description="A lightweight Python library for Nepali BS/AD date conversion and calendar utilities",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bhaveshadhikari/nepalidate",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.7",
    install_requires=[
        "pytz>=2021.1",
    ],
    keywords=["nepali date", "date converter", "nepali samaya","bikram sambat AD BS"],
)
