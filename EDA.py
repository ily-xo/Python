import pandas as pd
import ast
import json
import seaborn as sns
import matplotlib.pyplot as plt

# JSON data
with open('TC.json') as f:
    data = json.load(f)

# JSON data to DataFrame
df = pd.DataFrame(data)

df = pd.concat([df.drop(['FT'], axis=1), df['FT'].apply(pd.Series)], axis=1)
df['value'] = df['value'].str.strip() # remove redundant text

# EDA
unique_types = df['type'].unique()
unique_files = df['fileName'].unique()
unique_clauses = df['SC'].unique()
unique_keywords = df['keywords'].unique()
unique_values = df['value'].unique()
unique_compares = df['compare'].unique()

compare_counts = df['compare'].value_counts() # check matched or unmatched in compare column

#  DataFrame to CSV
df.to_csv('your_data.csv', index=False, escapechar='\\')

import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv('your_data.csv') # load csv

# pivot table with 'compare'
compare_counts = df['compare'].value_counts()

compare_df = pd.DataFrame(compare_counts).transpose()
sns.heatmap(compare_df, annot=True, fmt='d', cmap='Pastel1')
plt.title('Comparison of Matched vs. Unmatched')
plt.xlabel('State')
plt.ylabel('Count')

plt.show()


df = pd.read_csv('your_data.csv')

compare_counts = df['compare'].value_counts()
sns.barplot(x=compare_counts.index, y=compare_counts.values)
plt.title('Comparison of M and UM')
plt.xlabel('State')
plt.ylabel('Frequency')
plt.show


df = pd.concat([df.drop(['FT'], axis=1), df['FT'].apply(pd.Series)], axis=1)
df['value'] = df['value'].str.strip()  # remove redundant text

# Remove redundant in 'keywords' column
df['keywords'] = df['keywords'].apply(lambda x: re.sub(r'\b(\w+)(?:\W+\1\b)+', r'\1', x))

# Transform 'compare' column values
df['compare'] = df['compare'].replace({'equal': 'matched', 'less': 'unmatched', 'more': 'unmatched'})

# DataFrame to CSV
df.to_csv('your_data.csv', index=False, escapechar='\\')

import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv('your_data.csv') # load csv

# pivot table with 'compare'
compare_counts = df['compare'].value_counts()

compare_df = pd.DataFrame(compare_counts).transpose()
sns.heatmap(compare_df, annot=True, fmt='d', cmap='Pastel1')
plt.title('Comparison of M vs. UM')
plt.xlabel('State')
plt.ylabel('Count')

plt.show()


df = pd.read_csv('your_data.csv')

compare_counts = df['compare'].value_counts()
sns.barplot(x=compare_counts.index, y=compare_counts.values)
plt.title('Comparison of M and UM')
plt.xlabel('State')
plt.ylabel('Frequency')
plt.show

import re
from random import sample

#filter subset of data
matched_samples = df[df['compare'] == 'matched'].sample(n=50, random_state=1)
unmatched_samples = df[df['compare'] == 'unmatched'].sample(n=50, random_state=1)

subset_df = pd.concat([matched_samples,unmatched_samples])

# CSV
subset_df.to_csv('subset_data.csv', index=False, escapechar = '\\')

import pandas as pd
import ast
import json
import re

# JSON data
with open('test.contracts.json') as f:
    data = json.load(f)

# JSON data to DataFrame
df = pd.DataFrame(data)

df = pd.concat([df.drop(['FT'], axis=1), df['FT'].apply(pd.Series)], axis=1)
df['value'] = df['value'].str.strip()  # remove redundant text

# Remove redundant in 'keywords' column
df['keywords'] = df['keywords'].apply(lambda x: re.sub(r'\b(\w+)(?:\W+\1\b)+', r'\1', x))

# Remove 'text' words
df['keywords'] = df['keywords'].apply(lambda x: re.sub(r'\btext\b', '', x))

df['keywords'] = df['keywords'].str.replace(r'\bnone\b', '', case=False, regex=True)

# Transform 'compare' column values
df.loc[:, 'compare'] = df['compare'].replace({'equal': 'matched', 'less': 'unmatched', 'more': 'unmatched'})

# DataFrame to CSV
df.to_csv('your_data_two.csv', index=False, escapechar='\\')