from setuptools import setup

with open('README.md', 'r') as file:
    long_description = file.read()

setup(
    name='Complex Numbers',
    version='1.0',
    description='To find complex numbers',
    long_description=long_description,
    long_description_content_type='text/markdown',
    py_modules=['Complex Numbers'],
    package_dir={'': 'src'},
    classifiers=[
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",

        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Operating System :: OS Independent",
    ],
    install_requires=[],
    url="https://github.com/Vid-27/Complex-Numbers",
    author='Vidhya Lakshmi D , Maria Irudaya Regilan J',
    author_email='vidhyasumathi27@outlook.com'
)
