import string
from anyio import typed_attribute
import numpy as np
import pandas as pd
from sqlalchemy import true

### Define a pandas data frame
#Method 1: Define rows as list entry
list_seasons =  [   ['spring', 3, 5, 'warm'],
                    ['summer', 6, 8, 'hot'],
                    ['autumn', 9, 11, 'cool'],
                    ['winter', 12, 2, 'cold']   ]
index_seasons   =   [i for i in range(4)]
title_seasons   =   ['season', 'start_month', 'end_month', 'temperature']
df_1_seasons    =   pd.DataFrame( list_seasons, index=index_seasons, columns=title_seasons )
print(f"Define rows as list entry:\n{df_1_seasons}\n")

# Method 2 : Define by using dictionary
column_season =         ['spring', 'summer', 'autumn', 'winter']
column_start_month =    [3, 6, 9, 12]
column_end_month =      [5, 8, 11, 2]
column_temperature  =   ['warm', 'hot', 'cool', 'cold']
dict_seasons =          {   'season':       column_season,
                            'start_month':  column_start_month,
                            'end_month':    column_end_month,
                            'temperature':  column_temperature  }
df_2_seasons =  pd.DataFrame(dict_seasons)
print(f"Define by using dictionary:\n{df_2_seasons}\n")

# Method 3 : Define by reading csv with 'season' column being the index column
df_3_seasons = pd.read_csv('pandas_sample_1a.csv', index_col='season')
print(f"Define by reading csv:\n{df_3_seasons}\n")


### Select Rows
# select the initial 2 rows
print(df_1_seasons.head(2)) # print the first 2 rows. If input parameter is not specified, the default value is 5

# select the last 3 rows
print(df_1_seasons.tail(3)) # print the last 3 rows.

# select the 3rd row
print(df_1_seasons.iloc[2])

# select from row 2 to 3 inclusive
print(df_1_seasons.iloc[1:3])

# select rows meeting a specific criteria
print(df_1_seasons.loc[ df_1_seasons['season'].str.startswith('a') ]) # select rows with column season start with a


## Selct columns
# select the first column
print(df_1_seasons.iloc[:,0])

# select a specific column
print(df_1_seasons['season'])

# select multiple columns
print(df_1_seasons[['season', 'start_month']])

## Select a particular element/ block of elements
print(df_1_seasons.iloc[0,2]) # Select value of the first row and third column
print(df_1_seasons.iloc[[1,2], [0,3]]) # second & third rows, first & fourth columns
print(df_1_seasons.loc[[0,1],['season', 'start_month']]) # first & second rows, column 'season' and 'start_month'
print(df_1_seasons.loc[ 0:2, 'season':'end_month']) # first 3 rows, columns from 'season' to 'end_month'
print(df_1_seasons.loc[ df_1_seasons['season'] == 'spring', 'end_month':'temperature']) # records with season = spring & only extract columns from end_month to temperature

## Index (set, reset, sort)
df_1_indexed= df_1_seasons.set_index('season')  # Set the column 'season' as index
print(df_1_indexed)
print(df_1_seasons)

# if we want to do the update, we need to add the parameter inplace=True
df_2_seasons.set_index('season', inplace=True)
print(df_2_seasons)

# Reset the index
df_2_seasons.reset_index(inplace=True)
print(df_2_seasons)

# Show the role with season = 'Autumn'
print(df_1_indexed.loc['winter'])

# Sort index
df_1_indexed.sort_index(inplace=True)

## Write the dataframe to csv
df_2_seasons.to_csv('./pandas_sample_1b.csv', index=False) # with index=False to prevent the numeric index is shown in the file



