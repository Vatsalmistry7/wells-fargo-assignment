import glob
import os

import pandas as pd

# Constants for Input/Output directory
INPUT_DIR = "Input/"
OUTPUT_DIR = "Output"

# Regex to read sample_data file
data_files_path = glob.glob(INPUT_DIR + "*" + os.path.sep + "sample_data.*")

dfs = []
for path in data_files_path:
    dir_path = os.path.dirname(path)
    tmp_df = pd.read_csv(path)
    if len(tmp_df.columns) == 1:
        # as on of the file is `Pipe` seperated
        tmp_df = pd.read_csv(path, sep="|")
    # Adding source col to file path
    tmp_df['source'] = dir_path
    dfs.append(tmp_df)

# Combining dataframes
df = pd.concat(dfs)
df.to_csv(OUTPUT_DIR + os.path.sep + "consolidated_output.1.csv", index=False)
