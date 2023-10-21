from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("requirements.txt") as f:
    lines = f.read().splitlines()
    requirements = lines[1:] if lines[0] == "-i https://pypi.org/simple" else lines

setup(
    name="nutri_app_core",
    version="0.0.1",
    description="Core of NutriApp",
    author="Henrique Marcuzzo",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(where="nutri_app_core"),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10",
    package_dir={"": "nutri_app_core"},
    install_requires=requirements,
)
