import setuptools
import os

README_PATH = "README.md"

if os.path.exists(README_PATH):
    with open(README_PATH, "r") as fd:
        long_description = fd.read()

setuptools.setup(
    name="fastcomplete",
    version="0.0.1",
    author="",
    author_email="",
    description="Fast semi-static autocomplete for python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Roynecro97/fastcomplete",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=[
        "argcomplete==1.11.1",
    ],
)
