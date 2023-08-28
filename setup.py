from setuptools import find_packages, setup

setup(
    name='elevate',
    version='1.0.0',
    description='A utility for elevating Python scripts on Windows',
    author='Balazs Horvath',
    packages=find_packages(),
    scripts=['elevate.py'],
)