import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="suedoename", 
    version="0.0.1",
    author="sanctus91",
    author_email="author@example.com",
    description="Pseudoname generator",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sanctus91/suedoename",
    project_urls={
        "Bug Tracker": "https://github.com/sanctus91/suedoename/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=["suedoename"],
    python_requires='>=3.6',
    scripts = ["bin/suedoename"],
    include_package_data = True

)

