from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="veilnode",
    version="1.0.0",
    author="suadatbiniqbal",
    description="Tor Hidden Service Hosting Tool",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=[
        "stem>=1.8.0",
    ],
    entry_points={
        "console_scripts": [
            "veilnode=veilnode.cli:main",
        ],
    },
)