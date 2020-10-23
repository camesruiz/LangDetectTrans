import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="LangDetectTrans", # Replace with your own username
    version="0.0.1",
    author="Camilo Ruiz",
    author_email="ruiznho123@gmail.com",
    description="Language detector and translation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/camesruiz/LangDetectTrans",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    # List run-time dependencies here.  These will be installed by pip when
    # your project is installed. For an analysis of "install_requires" vs pip's
    # requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    install_requires=['textblob,transformers'],
    include_package_data=True
)
