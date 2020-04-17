 
#!/usr/bin/env python
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="attackerkb-api",
    version="0.0.2",
    author="Kevin Breen",
    author_email="kevin@techanarchy.net",
    description="AttackerKB API Library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kevthehermit/attackerkb-api",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)