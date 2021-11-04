import pandas as pd

# Combine the supplied CSV files and write the output to the given output file.
def combine_csvs(files: [str], output) -> None:
    dfs = (pd.read_csv(f, sep=',', dtype=str) for f in files)
    df_merged = pd.concat(dfs, ignore_index=True)
    df_merged.to_csv(output, index=False)
