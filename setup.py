from pathlib import Path
from setuptools import setup, find_packages

HERE = Path(__file__).parent

long_description = (HERE / "README.md").read_text(encoding="utf-8") if (HERE / "README.md").exists() else ""

setup(
    name="scratchxml",
    version="0.1.3",
    description="Read and write Assimilate Scratch custom-command XML as Python objects",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="antoinedurr",
    author_email="antoine@antoinedurr.com",
    url="https://github.com/antoinedurr/ScratchXML",
    license="MIT",
    packages=find_packages(exclude=("tests", "docs")),
    include_package_data=True,
    install_requires=[
        "xmltodict",
    ],
    python_requires=">=3.8",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Software Development :: Libraries",
        "Topic :: Text Processing :: Markup :: XML",
    ],
)
