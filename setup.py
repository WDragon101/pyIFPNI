import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyIFPNI",
    version="0.2.1",
    author="Bailong Zhao",
    author_email="bailongzhao@163.com",
    description="A package accessing to IFPNI",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/WDragon101/pyIFPNI",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)