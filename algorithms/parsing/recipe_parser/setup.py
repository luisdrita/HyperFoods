import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="recipe_parser",  # Replace with your own username
    version="0.1",
    author="Luis Rita",
    author_email="l.rita19@imperial.ac.uk",
    description="Retrieves ingredients, quantities and units from any recipe.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/warcraft12321/HyperFoods",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[],
    python_requires='>=3.6',
    license='MIT'
)
