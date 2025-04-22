from setuptools import setup, find_packages
from psmgr.__version__ import __version__

setup(
    name='psmgr',
    version=__version__,
    author='nae-dev',
    author_email='elienana92@gmail.com',
    licence='MIT License',
    description='A simple and secure password manager built in Python.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/nanaelie/psmgr',
    packages=find_packages(),
    install_requires=[
        'pandas',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'psmgr=psmgr.cli:main',
        ]
    },
    include_package_data=True,
)
