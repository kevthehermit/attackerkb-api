 
#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name='attackerkb-api',
    version='0.0.1',
    author='Kevin Breen',
    author_email='kevin@techanarchy.net',
    description="AttackerKB API Library",
    url='https://github.com/kevthehermit/attackerkb-api',
    license='MIT',
    zip_safe=False,
    packages=find_packages(),
    include_package_data=True,
    package_data={'': ['LICENSE', 'CHANGELOG.md']},
    package_dir={'attackerkb_api': 'attackerkb_api'},
    install_requires=["requests >= 2.22.0"]
)