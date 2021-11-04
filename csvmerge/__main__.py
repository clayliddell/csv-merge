#!/usr/bin/env python3

import argparse
import sys
import csvmerge as cm

def main() -> None:
    # Construct argument parser.
    parser = argparse.ArgumentParser(description='This script merges CSV files with shared columns.')
    parser.add_argument('files', metavar='FILE', nargs='+', type=str, help='path to CSV file being merged')
    args = parser.parse_args()
    cm.merge(args.files, sys.stdout)


# If this script is being called directly, call the main function.
if __name__ == '__main__':
    main()
