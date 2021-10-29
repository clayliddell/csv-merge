#!/usr/bin/env python3

import argparse
import pandas as pd

def main(args: argparse.Namespace) -> None:
   combine_csvs(files, output_file) 

# Combine the supplied CSV files and write the output to the given output file.
def combine_csvs(files: [str], output_file) -> None:
    dfs = (pd.read_csv(f, sep=',') for f in files)
    df_merged = pd.concat(dfs, ignore_index=True)
    df_merged.to_csv(output_file)

# Construct argument parser.
parser = argparse.ArgumentParser(description='This script merges CSV files with shared columns.')
parser.add_argument('files', type=str, nargs='+', help='paths to CSV files to be merged.')
parser.add_argument('-o', '--output_file', type=str, help='output file')

# If this script is being called directly, parse the supplied arguments and run
# the main function.
if __name__ == '__main__':
    main(parser.parse_args())
