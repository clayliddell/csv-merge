from setuptools import find_packages, setup

setup(
    name='csv-merge',
    version='0.1.0',
    description='A tool for combining CSV files.',
    author='Clayton Liddell',
    author_email='account+github@clayliddell.com',
    url='https://github.com/clayliddell/csv-merge',
    license='MIT',
    packages=find_packages(exclude=['main', 'tests', 'tests.*']),
    install_requires=[
        'pandas>=1.3.0',
    ],
)
