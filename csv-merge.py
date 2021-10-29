#!/usr/bin/env python3

import argparse
import pandas as pd
import sys

def main(args: argparse.Namespace) -> None:
    output = args.output_file if args.output_file is not None else sys.stdout
    combine_csvs(args.files, output) 

# Combine the supplied CSV files and write the output to the given output file.
def combine_csvs(files: [str], output) -> None:
    dfs = (pd.read_csv(f, sep=',', dtype=str) for f in files)
    df_merged = pd.concat(dfs, ignore_index=True)
    df_merged.to_csv(output, index=False)

# Construct argument parser.
parser = argparse.ArgumentParser(description='This script merges CSV files with shared columns.')
parser.add_argument('files', metavar='FILE', nargs='+', type=str, help='path to CSV file being merged')
parser.add_argument('-o', '--output_file', nargs='?', type=str, help='output file')

# If this script is being called directly, parse the supplied arguments and run
# the main function.
if __name__ == '__main__':
    main(parser.parse_args())
