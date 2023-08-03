import pandas as pd

# Sample data for df1 and df2
data1 = {'schema': ['A', 'B', 'A', 'C'],
         'tbl': ['table1', 'table2', 'table1', 'table3'],
         'partition': ['p1', 'p1', 'p2', 'p1'],
         'count': [10, 20, 15, 5]}

data2 = {'schema': ['A', 'B', 'A', 'C'],
         'tbl': ['table1', 'table2', 'table1', 'table3'],
         'partition': ['p1', 'p1', 'p2', 'p1'],
         'count': [12, 20, 10, 7]}

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

# Merge the two dataframes on the specified columns and calculate count changes
merged_df = pd.merge(df1, df2, on=['schema', 'tbl', 'partition'], suffixes=('_old', '_new'))
merged_df['count_change'] = merged_df['count_new'] - merged_df['count_old']

# Create a new dataframe with schema, tbl, partition, and count_change columns
count_change_df = merged_df[['schema', 'tbl', 'partition', 'count_change']].copy()

print(count_change_df)
