import setuptools

with open("./README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name="gamestart",
    version="0.0.1",
    author="Yu Wang (bigeyex)",
    author_email="bigeyex@gmail.com",
    description="Pygame wrapper for learners, jammers and educators",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bigeyex/python-adminui",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'pygame'
    ],
    include_package_data = True,
    python_requires='>=3.6',
)