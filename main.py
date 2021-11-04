#!/usr/bin/env python3

import argparse
import pandas as pd
import sys

def main(args: argparse.Namespace) -> None:
    combine_csvs(args.files, sys.stdout)

# Construct argument parser.
parser = argparse.ArgumentParser(description='This script merges CSV files with shared columns.')
parser.add_argument('files', metavar='FILE', nargs='+', type=str, help='path to CSV file being merged')

# If this script is being called directly, parse the supplied arguments and run
# the main function.
if __name__ == '__main__':
    main(parser.parse_args())
