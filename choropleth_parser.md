# parser for choropleth
nicholas chung, 2017 | nich.chung@gmail.com
***

pandas parser

munge and transform raw data into choropleth-ready CSV:

 1. read raw CSV in S3 bucket
 2. create dataframe with relevant columns
 3. drop rows with missing data
 4. create frequency table 
 5. add leading zeroes to ID values to match GeoJSON IDs
 6. rename headers and drop columns with unnecessary dependent variables	
 7. save to local CSV

```python
# import modules
import boto
import numpy as np
import pandas as pd
import scipy.stats as stats


# connect Amazon S3 bucket with boto2
c = boto.connect_s3()
b = c.get_bucket('nichung-datasets')

# read and assign raw CSV to dataframe
NY13_df = pd.read_csv('s3:/nichung-datasets/ss13ny.csv')

# take relevant columns and assign to new dataframe
access_puma = NY13_df[['PUMA', 'ACCESS']]
# drop all rows with missing data
access_puma.dropna(how='all')

# frequency table of census tract against internet access without row & column totals
table = pd.crosstab(index=access_puma["PUMA"], 
                                        columns=access_puma["ACCESS"],
                                        margins=False)

# confirm values as integers
table = table.astype(int)

# add leading zeroes to PUMA to match PUMA IDs in relevant GeoJSON
table['PUMA'] = table['PUMA'].apply('{:0>5}'.format);

# rename column headers with matching key value
table = table.rename(columns={'PUMA':'id', '1.0':'yes', '2.0':'no', '3.0':'yes but not paying'})

# save dataframe as CSV tables for dependent variable
table.drop(['yes', 'yes but not paying', 'All']  axis=1, inplace=True)
table.to_csv('../data/access_yes_only_13__id.csv', index = False)
```
