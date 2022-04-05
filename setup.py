from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='functiontester',
    packages='testcode',
    version='0.1.0',
    url='https://github.com/Fort-P/functiontester',
    description='A python library that allows you to easily test functions in your code',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Fort-P',
    license='MIT',
    install_requires=[],
)