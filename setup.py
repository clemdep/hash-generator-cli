import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="hash_generator_cli",
    version="0.0.1",
    author="Clem Dep",
    author_email="dev@depruneaux.com",
    description="A small CLI hash generator based on python hashlib",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/clemdep/hash-generator-cli",
    entry_points={
        "console_scripts": [
            "hash-generator=hash_generator_cli.lib.cli:run"
        ]
    },
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
