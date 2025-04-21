from setuptools import setup, find_packages

setup(
    name="pmgr",
    version="1.0.0",
    author="nanaelie",
    description="A Python-based password manager with features for storing, generating, and managing passwords securely.",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/nanaelie/password-manager-python",
    packages=find_packages(),
    python_requires=">=3.6",
    install_requires=[
        "pandas"
    ],
    entry_points={
        'console_scripts': [
            'pmgr=main:main',
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Security",
        "Intended Audience :: End Users/Desktop",
        "Environment :: Console",
    ],
    include_package_data=True,
)
