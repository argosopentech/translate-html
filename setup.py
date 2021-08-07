from setuptools import setup, find_packages

with open("requirements.txt") as f:
    required_packages = f.read().splitlines()

with open("README.md") as f:
    long_description = f.read()

setup(
    name="translatehtml",
    version="1.5.1",
    description="Translate HTML using Beautiful Soup and Argos Translate",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="P.J. Finlay",
    author_email="admin@argosopentech.com",
    url="https://www.argosopentech.com",
    packages=find_packages(),
    install_requires=required_packages,
)
