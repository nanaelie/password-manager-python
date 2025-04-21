from setuptools import setup, find_packages

setup(
    name='psmgr',
    version='1.0.0',
    author='nae-dev',
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
            'pmgr=main:main',
        ]
    },
    include_package_data=True,
)
