import pandas as pd
import glob

# Read all csv files
files = glob.glob('classic_models_dataset/*.csv')
# Create list of dataframes
dfs = [pd.read_csv(file) for file in files]
# Merge all datasets
combined_df = pd.concat(dfs, ignore_index=True)

print(combined_df.head())

# Save merged dataset
combined_df.to_csv('all_sales.csv', index=False)

#Check total rows(to check all df is merge or not)
print(combined_df.shape)

print(combined_df.info())
print(combined_df.describe())

#to check missing/null values
print(combined_df.isnull().sum())
print(combined_df.fillna(0))
print(combined_df.duplicated().sum())

combined_df['revenue'] = combined_df['quantityOrdered']*combined_df['priceEach']
print('Total Revenue::')
print(combined_df['revenue'].sum())

combined_df['profit'] = (combined_df['priceEach']-combined_df['buyPrice']) * (combined_df['quantityOrdered'])

print('Total Profit::')
print(combined_df['profit'].sum())