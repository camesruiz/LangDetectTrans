from setuptools import setup

setup(
    name='langdetecttrans',
    version='0.0.1',
    url='https://github.com/camesruiz/LangDetectTrans',
    author='Camilo Ruiz',
    author_email='ruiznho123@gmail.com',
    py_modules=["langdetecttrans"],
    package_dir={'': 'src'},
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    install_requires=[
        "transformers",
        "torch",
        "textblob",
    ],
)