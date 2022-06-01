import pandas as pd
from sqlalchemy import create_engine


def populate_db(df):
    # Stub to populate the combined data to database, replace DB_URL with correct one
    engine = create_engine('DB_URL')
    df.to_sql('table_name', engine)


# Constants for differenct file path
# not genralizable as each file has to have separate processing
sample1_file_path = "./Input/data_source_1/sample_data.1.csv"
sample2_file_path = "./Input/data_source_1/sample_data.2.dat"
sample3_file_path = "./Input/data_source_2/sample_data.3.dat"
material_file_path = "./Input/data_source_2/material_reference.csv"

# Process sample_data.1.csv
df1 = pd.read_csv(sample1_file_path)
print("Before filtering sample_data.1.csv shape is {}".format(df1.shape))
df1 = df1[df1.worth > 1.0]
print("After filtering sample_data.1.csv shape is {}".format(df1.shape))

df2 = pd.read_csv(sample2_file_path, sep='|')
print("Before aggregating sample_data.2.dat shape is {}".format(df2.shape))
tmp = df2.groupby(['product_name']).agg(
    {'worth': sum, 'material_id': max, 'quality': 'first'})
print("After aggregating sample_data.2.dat shape is {}".format(tmp.shape))

df3 = pd.read_csv(sample3_file_path)
print("Before calculating `worth` sample_data.3.dat shape is {}".format(df3.shape))
df3['worth'] = df3['worth'] * df3['material_id']
print("After calculating `worth` sample_data.3.dat shape is {}".format(df3.shape))

final_df = pd.concat([df1, tmp, df3])
print("Final df shape after combinig {}".format(final_df.shape))
material_df = pd.read_csv(material_file_path)

concatinated_df = pd.merge(final_df, material_df, left_on=[
    'material_id'], right_on=['id'], how='left')
print("Final df shape after merging with material csv {}".format(
    concatinated_df.shape))
concatinated_df.to_csv("Output/consolidated_output_bonus.csv", index=False)
# populate_db()
