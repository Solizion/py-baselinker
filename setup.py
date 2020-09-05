import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="py-baselinker", # Replace with your own username
    version="0.0.1",
    author="Solizion Associations",
    author_email="kontakt@solizion.pl",
    description="Python library to communication with baselinker",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Solizion/py-baselinker",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)
