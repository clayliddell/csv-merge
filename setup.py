from setuptools import setup

setup(
    name='csv-merge',
    version='0.1.2',
    description='A tool for combining CSV files.',
    author='Clayton Liddell',
    author_email='account+github@clayliddell.com',
    url='https://github.com/clayliddell/csv-merge',
    license='MIT',
    packages=['csvmerge'],
    install_requires=[
        'pandas>=1.3.0',
    ],
    entry_points = {
        'console_scripts': ['csvmerge=csvmerge.__main__:main'],
    },
)
