




from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="create-pypi-project",
    version="0.0.4",
    author="Haider Ali",
    author_email="ali075398@gmail.com",
    description="A command line for creating Pypi projects",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    project_urls={
        "Bug Tracker": "https://github.com/pypa/sampleproject/issues",
    },
    packages = find_packages(),
    entry_points = {
            'console_scripts': [
                'createpypiproject = createpypiproject.main:create_project'
            ]
        },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires= [
        'click'
    ],
    python_requires=">=3.6",
    zip_safe = False
)