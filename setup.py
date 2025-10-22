"""Setup file for file_parser package."""
from setuptools import setup, find_packages

setup(
    name="file_parser",
    version="0.1.0",
    packages=find_packages(),
    python_requires=">3.7",
    install_requires=[],
    extras_require={
        'dev': [
            'pytest>=7.0.0',
            'pytest-cov>=4.0.0',
        ]
    }
)