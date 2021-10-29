# CSV Merge

A Python executable for merging CSV files with shared columns.

## Why?

Though there are many CSV manipulation tools out there, I was seriously struggling to find a simple CLI tool for merging CSV file (while taking into consideration all of the various caveats which may be encountered; e.g. columns not being in the same order, files not sharing certain columns, etc.).
This script performs this task using the magic of the [Pandas library](https://pandas.pydata.org/).

## Dependencies

Python 3 (version 3.6 or greater) is required to run this project.

## Installation

You can either install the scripts required dependencies globally:

```sh
python3 -m pip install -r requirements.txt
```
And run it using:
```sh
python3 ./csv-merge.py -h
```

Or you can use Pipenv for dependency management:

```sh
python3 -m pip install --user pipenv
pipenv install
```
And run it using:
```sh
pipenv run ./csv-merge.py -h
```

## Usage

The script can be run as follows:

```sh
python3 ./csv-merge.py file_1.csv file_2.csv file_n.csv... -o file_combined.csv
```

## Help!

The command has an easy to access help menu using the `-h` option:
```sh
python3 ./csv-merge.py -h
```
