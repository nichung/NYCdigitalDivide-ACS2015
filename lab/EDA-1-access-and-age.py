
# coding: utf-8

# In[12]:

import math, os
import pandas as pd
import boto
import plotly
from plotly import tools
import plotly.offline as py
import plotly.graph_objs as go
import cufflinks as cf
from filechunkio import FileChunkIO

cf.go_offline()
py.init_notebook_mode()

c = boto.connect_s3()
b = c.get_bucket('nichung-datasets')


# **Load CSV and assign to dataframe**

# In[3]:

mergeNY13_df = pd.read_csv('s3:/nichung-datasets/ss13ny.csv')


# In[13]:

mergeNY14_df = pd.read_csv('s3:/nichung-datasets/ss14ny.csv')


# In[21]:

mergeNY15_df = pd.read_csv('s3:/nichung-datasets/ss15ny.csv')


# In[22]:

ny_puma_df = pd.read_csv('s3:/nichung-datasets/puma_ny.csv')


# **Create categorical series for age array and add column to dataframes**

# In[15]:

bins = [0, 19, 25, 35, 45, 55, 65, 100]


# In[16]:

group_names = ['<18', '18-24', '25-34', '35-44', '45-54', '55-64', '>65']


# In[17]:

age_group_13 = pd.cut(mergeNY13_df['AGEP'], bins, labels=group_names)


# In[18]:

age_group_14 = pd.cut(mergeNY14_df['AGEP'], bins, labels=group_names)


# In[23]:

age_group_15 = pd.cut(mergeNY15_df['AGEP'], bins, labels=group_names)


# In[24]:

mergeNY13_df['age_group_13'] = pd.cut(mergeNY13_df['AGEP'], bins, labels=group_names)


# In[25]:

mergeNY14_df['age_group_14'] = pd.cut(mergeNY14_df['AGEP'], bins, labels=group_names)


# In[26]:

mergeNY15_df['age_group_15'] = pd.cut(mergeNY15_df['AGEP'], bins, labels=group_names)


# **Check new dataframes**

# In[27]:

age_group_13.value_counts()


# In[28]:

age_group_13.describe()


# In[29]:

age_group_14.value_counts()


# In[30]:

age_group_14.describe()


# In[31]:

age_group_15.value_counts()


# In[32]:

age_group_15.describe()


# **Write new columns to CSV for reference in other notebooks**

# In[9]:

mergeNY13_df.to_csv('/tmp/ss13ny.csv')
# get file info
source_path = '/tmp/ss13ny.csv'
source_size = os.stat(source_path).st_size

# create multipart upload request
mp = b.initiate_multipart_upload(os.path.basename(source_path))

# use chunk size of 50 MiB
chunk_size = 52428800
chunk_count = int(math.ceil(source_size / float(chunk_size)))

# send the file parts, using FileChunkIO to create a file-like object
# that points to a certain byte range within the original file.
# set bytes to never exceed original file size.

for i in range(chunk_count):
    offset = chunk_size * i
    bytes = min(chunk_size, source_size - offset)
    with FileChunkIO(source_path, 'r', offset=offset,
                    bytes=bytes) as fp:
        mp.upload_part_from_file(fp, part_num= i + 1)

# finish upload
mp.complete_upload()


# In[34]:

mergeNY14_df.to_csv('/tmp/ss14ny.csv')
# get file info
source_path = '/tmp/ss14ny.csv'
source_size = os.stat(source_path).st_size

# create multipart upload request
mp = b.initiate_multipart_upload(os.path.basename(source_path))

# use chunk size of 50 MiB
chunk_size = 52428800
chunk_count = int(math.ceil(source_size / float(chunk_size)))

# send the file parts, using FileChunkIO to create a file-like object
# that points to a certain byte range within the original file.
# set bytes to never exceed original file size.

for i in range(chunk_count):
    offset = chunk_size * i
    bytes = min(chunk_size, source_size - offset)
    with FileChunkIO(source_path, 'r', offset=offset,
                    bytes=bytes) as fp:
        mp.upload_part_from_file(fp, part_num= i + 1)

# finish upload
mp.complete_upload()


# In[35]:

mergeNY15_df.to_csv('/tmp/ss15ny.csv')
# get file info
source_path = '/tmp/ss15ny.csv'
source_size = os.stat(source_path).st_size

# create multipart upload request
mp = b.initiate_multipart_upload(os.path.basename(source_path))

# use chunk size of 50 MiB
chunk_size = 52428800
chunk_count = int(math.ceil(source_size / float(chunk_size)))

# send the file parts, using FileChunkIO to create a file-like object
# that points to a certain byte range within the original file.
# set bytes to never exceed original file size.

for i in range(chunk_count):
    offset = chunk_size * i
    bytes = min(chunk_size, source_size - offset)
    with FileChunkIO(source_path, 'r', offset=offset,
                    bytes=bytes) as fp:
        mp.upload_part_from_file(fp, part_num= i + 1)

# finish upload
mp.complete_upload()


# ## i n t e r n e t  &  c o m p u t e r  o w n e r s h i p
# 
# **explore internet access and computer access type over time**
# 
# Questions:
# + what does internet access look like across time?
# + do more or less people have internet access now?
# + how has handheld computer (smartphone or tablet) ownership changed over time?

# In[ ]:

# internet access without a subscription to an ISP, 13-15
y_wo_2013 = mergeNY13_df[mergeNY13_df['ACCESS'] == 2]; # assign variable to array of rows that match value
y_wo_13 = y_wo_2013['ACCESS'].value_counts(); # assign variable to count of integers in array
ywo_13 = y_wo_13.values[0]; # assign variable to first value in array
y_wo_2014 = mergeNY14_df[mergeNY14_df['ACCESS'] == 2]; 
y_wo_14 = y_wo_2014['ACCESS'].value_counts();
ywo_14 = y_wo_14.values[0];
y_wo_2015 = mergeNY15_df[mergeNY15_df['ACCESS'] == 2]; 
y_wo_15 = y_wo_2015['ACCESS'].value_counts();
ywo_15 = y_wo_15.values[0];

# internet access with a subscription to an ISP, 13-15
y_2013 = mergeNY13_df[mergeNY13_df['ACCESS'] == 1]; 
y_13 = y_2013['ACCESS'].value_counts();
y13 = y_13.values[0];
y_2014 = mergeNY14_df[mergeNY14_df['ACCESS'] == 1]; 
y_14 = y_2014['ACCESS'].value_counts();
y14 = y_14.values[0]; 
y_2015 = mergeNY15_df[mergeNY15_df['ACCESS'] == 1]; 
y_15 = y_2015['ACCESS'].value_counts();
y15 = y_15.values[0];


# ***
# #### to do
# 
# + figure out a simpler way of getting counts of values and passing them to variables
# + are they called variables or dataframes in the above code?
#     + at what point does one change into another?
#     + are they same?
#    
# ***

# In[ ]:

# plot internet access without a subscription to an ISP, 13-15
yes_access = go.Bar(
    x=['2013', '2014', '2015'],
    y=[y13, y14, y15],
    name='Has internet access'
);
yes_access_wo = go.Bar(
    x=['2013', '2014', '2015'],
    y=[ywo_13, ywo_14, ywo_15],
    name='Has internet access w/o subscription'
);
no_access = go.Bar(
    x=['2013', '2014', '2015'],
    y=[n_13, n_14, n_15],
    name='Does not have internet access'
);
data = [yes_access, yes_access_wo, no_access]
layout = go.Layout(barmode='stack')

access_fig = go.Figure(data=data, layout=layout)
py.iplot(access_fig, filename='access-over-time')


# In[ ]:

# has a handheld computer, 13-15
yes_handheld_2013 = mergeNY13_df[mergeNY13_df['HANDHELD'] == 1];
yes_hh_13 = yes_handheld_2013['HANDHELD'].value_counts();
y_hh_13 = yes_hh_13.values[0];
yes_handheld_2014 = mergeNY14_df[mergeNY14_df['HANDHELD'] == 1];
yes_hh_14 = yes_handheld_2014['HANDHELD'].value_counts();
y_hh_14 = yes_hh_14.values[0];
yes_handheld_2015 = mergeNY15_df[mergeNY15_df['HANDHELD'] == 1];
yes_hh_15 = yes_handheld_2015['HANDHELD'].value_counts();
y_hh_15 = yes_hh_15.values[0];

# doesn't have a handheld computer, 13-15
no_handheld_2013 = mergeNY13_df[mergeNY13_df['HANDHELD'] == 2];
no_hh_13 = no_handheld_2013['HANDHELD'].value_counts();
n_hh_13 = no_hh_13.values[0];
no_handheld_2014 = mergeNY14_df[mergeNY14_df['HANDHELD'] == 2];
no_hh_14 = no_handheld_2014['HANDHELD'].value_counts();
n_hh_14 = no_hh_14.values[0];
no_handheld_2015 = mergeNY15_df[mergeNY15_df['HANDHELD'] == 2];
no_hh_15 = no_handheld_2015['HANDHELD'].value_counts();
n_hh_15 = no_hh_15.values[0];

# did not respond, 13-15
nan_handheld_2013 = mergeNY13_df[mergeNY13_df['HANDHELD'] == 0];
nan_hh_13 = nan_handheld_2013['HANDHELD'].value_counts();
nan_hh_13 = test_nan_hh_13.values[0];
nan_handheld_2014 = mergeNY14_df[mergeNY14_df['HANDHELD'] == 0];
nan_hh_14 = nan_handheld_2014['HANDHELD'].value_counts();
nan_hh_14 = nan_hh_14.values[0];
nan_handheld_2015 = mergeNY15_df[mergeNY15_df['HANDHELD'] == 0];
nan_hh_15 = nan_handheld_2015['HANDHELD'].value_counts();
nan_hh_15 = nan_hh_15.values[0]


# In[ ]:

# plot handheld computer ownership, 13-15
yes_hh = go.Bar(
    x=['2013', '2014', '2015'],
    y=[y_hh_13, y_hh_14, y_hh_15],
    name='Has a smartphone/handheld computer'
);
no_hh = go.Bar(
    x=['2013', '2014', '2015'],
    y=[n_hh_13, n_hh_14, n_hh_15],
    name='Doesn\'t have a smartphone/handheld computer'
);
nan_hh = go.Bar(
    x=['2013', '2014', '2015'],
    y=[nan_hh_13, nan_hh_14, nan_hh_15],
    name='No response'
);

data = [yes_hh, no_hh, nan_hh]; 
layout = go.Layout(barmode='stack')

hh_fig = go.Figure(data=data, layout=layout); 
py.iplot(hh_fig, filename='hh-over-time')


# ## a g e  g r o u p s
# 
# **explore internet access type and computer ownership by age, 13-15**
# 
# Questions:
# + what does the distribution of access to the different types of internet look like across age?
# + is there any noticeable change over time in what proportion of the population use a particular type of internet connection? how about by age?

# In[ ]:

age_group_13.value_counts()


# In[ ]:

less_18_2013 = mergeNY13_df[mergeNY13_df['age_group_13'] == '<18'];
less_18_13 = less_18_2013['age_group_13'].value_counts();
under_eighteen_13 = less_18_13.values[0];
eighteen_to_24_2013 = mergeNY13_df[mergeNY13_df['age_group_13'] == '18-24']
eighteen_to_24_13 = eighteen_to_24_2013['age_group_13'].value_counts();
eighteen_24_13 = eighteen_to_24_13.values[0];
twentyfive_to_34_2013 = mergeNY13_df[mergeNY13_df['age_group_13'] == '25-34'];
twentyfive_to_34_13 = twentyfive_to_34_2013['age_group_13'].value_counts();
twentyfive_34_13 = twentyfive_to_34_13.values[0];
thirtyfive_to_44_2013 = mergeNY13_df[mergeNY13_df['age_group_13'] == '35-44'];
thirtyfive_to_44_13 = thirtyfive_to_44_2013['age_group_13'].value_counts(); 
thirtyfive_44_13 = thirtyfive_to_44_13.values[0];
fortyfive_to_54_2013 = mergeNY13_df[mergeNY13_df['age_group_13'] == '45-54'];
fortyfive_to_54_13 = fortyfive_to_54_2013['age_group_13'].value_counts();
fortyfive_54_13 = fortyfive_to_54_13.values[0];
fiftyfive_to_64_2013 = mergeNY13_df[mergeNY13_df['age_group_13'] == '55-64'];
fiftyfive_to_64_13 = fiftyfive_to_64_2013['age_group_13'].value_counts();
fiftyfive_64_13 = fiftyfive_to_64_13.values[0];
greater_65_2013 = mergeNY13_df[mergeNY13_df['age_group_13'] == '>65'];
greater_65_13 = greater_65_2013['age_group_13'].value_counts();
more_65_13 = greater_65_13.values[0];


# In[ ]:

data = [go.Bar(
    x=['<18', '18-24', '25-34', '35-44', '45-54', '55-64', '>65'],
    y=[under_eighteen_13, eighteen_24_13, twentyfive_34_13, thirtyfive_44_13, fortyfive_54_13, fiftyfive_64_13, more_65_13])]
py.iplot(data, filename='age_distribution_13')


# In[ ]:




# In[226]:

# crosstabs of internet type (broadband) by age group
broadband_by_age_13 = pd.crosstab(mergeNY13_df.BROADBND, mergeNY13_df.age_group_13, margins=True);
broadband_by_age_13.columns = ['<18', '18-24', '25-34', '35-44', '45-54', '55-64', '>65', 'rowtotal'];
broadband_by_age_13.index= ["yes","no","coltotal"];
broadband_by_age_14 = pd.crosstab(mergeNY14_df.BROADBND, mergeNY14_df.age_group_14, margins=True);
broadband_by_age_14.columns = ['<18', '18-24', '25-34', '35-44', '45-54', '55-64', '>65', 'rowtotal'];
broadband_by_age_14.index= ["yes","no","coltotal"];
broadband_by_age_15 = pd.crosstab(mergeNY15_df.BROADBND, mergeNY15_df.age_group_15, margins=True);
broadband_by_age_15.columns = ['<18', '18-24', '25-34', '35-44', '45-54', '55-64', '>65', 'rowtotal'];
broadband_by_age_15.index= ["yes","no","coltotal"]


# In[227]:

# crosstabs of internet type (dialup) by age group
dialup_by_age_13 = pd.crosstab(mergeNY13_df.DIALUP, mergeNY13_df.age_group_13, margins=True);
dialup_by_age_13.columns = ['<18', '18-24', '25-34', '35-44', '45-54', '55-64', '>65', 'rowtotal'];
dialup_by_age_13.index= ["yes","no","coltotal"];
dialup_by_age_14 = pd.crosstab(mergeNY14_df.DIALUP, mergeNY14_df.age_group_14, margins=True);
dialup_by_age_14.columns = ['<18', '18-24', '25-34', '35-44', '45-54', '55-64', '>65', 'rowtotal'];
dialup_by_age_14.index= ["yes","no","coltotal"];
dialup_by_age_15 = pd.crosstab(mergeNY15_df.DIALUP, mergeNY15_df.age_group_15, margins=True);
dialup_by_age_15.columns = ['<18', '18-24', '25-34', '35-44', '45-54', '55-64', '>65', 'rowtotal'];
dialup_by_age_15.index= ["yes","no","coltotal"]


# In[228]:

# crosstabs of internet type (dsl) by age group
dsl_by_age_13 = pd.crosstab(mergeNY13_df.DSL, mergeNY13_df.age_group_13, margins=True);
dsl_by_age_13.columns = ['<18', '18-24', '25-34', '35-44', '45-54', '55-64', '>65', 'rowtotal'];
dsl_by_age_13.index= ["yes","no","coltotal"];
dsl_by_age_14 = pd.crosstab(mergeNY14_df.DSL, mergeNY14_df.age_group_14, margins=True);
dsl_by_age_14.columns = ['<18', '18-24', '25-34', '35-44', '45-54', '55-64', '>65', 'rowtotal'];
dsl_by_age_14.index= ["yes","no","coltotal"];
dsl_by_age_15 = pd.crosstab(mergeNY15_df.DSL, mergeNY15_df.age_group_15, margins=True);
dsl_by_age_15.columns = ['<18', '18-24', '25-34', '35-44', '45-54', '55-64', '>65', 'rowtotal'];
dsl_by_age_15.index= ["yes","no","coltotal"]


# In[229]:

# crosstabs of internet type (fiber optic) by age group
fiberop_by_age_13 = pd.crosstab(mergeNY13_df.FIBEROP, mergeNY13_df.age_group_13, margins=True);
fiberop_by_age_13.columns = ['<18', '18-24', '25-34', '35-44', '45-54', '55-64', '>65', 'rowtotal'];
fiberop_by_age_13.index= ["yes","no","coltotal"];
fiberop_by_age_14 = pd.crosstab(mergeNY14_df.FIBEROP, mergeNY14_df.age_group_14, margins=True);
fiberop_by_age_14.columns = ['<18', '18-24', '25-34', '35-44', '45-54', '55-64', '>65', 'rowtotal'];
fiberop_by_age_14.index= ["yes","no","coltotal"];
fiberop_by_age_15 = pd.crosstab(mergeNY15_df.FIBEROP, mergeNY15_df.age_group_15, margins=True);
fiberop_by_age_15.columns = ['<18', '18-24', '25-34', '35-44', '45-54', '55-64', '>65', 'rowtotal'];
fiberop_by_age_15.index= ["yes","no","coltotal"]


# In[230]:

# crosstabs of internet type (cable) by age group
modem_by_age_13 = pd.crosstab(mergeNY13_df.MODEM, mergeNY13_df.age_group_13, margins=True);
modem_by_age_13.columns = ['<18', '18-24', '25-34', '35-44', '45-54', '55-64', '>65', 'rowtotal'];
modem_by_age_13.index= ["yes","no","coltotal"];
modem_by_age_14 = pd.crosstab(mergeNY14_df.MODEM, mergeNY14_df.age_group_14, margins=True);
modem_by_age_14.columns = ['<18', '18-24', '25-34', '35-44', '45-54', '55-64', '>65', 'rowtotal'];
modem_by_age_14.index= ["yes","no","coltotal"];
modem_by_age_15 = pd.crosstab(mergeNY15_df.MODEM, mergeNY15_df.age_group_15, margins=True);
modem_by_age_15.columns = ['<18', '18-24', '25-34', '35-44', '45-54', '55-64', '>65', 'rowtotal'];
modem_by_age_15.index= ["yes","no","coltotal"]


# In[231]:

# crosstabs of internet type (other) by age group
other_by_age_13 = pd.crosstab(mergeNY13_df.OTHSVCEX, mergeNY13_df.age_group_13, margins=True);
other_by_age_13.columns = ['<18', '18-24', '25-34', '35-44', '45-54', '55-64', '>65', 'rowtotal'];
other_by_age_13.index= ["yes","no","coltotal"];
other_by_age_14 = pd.crosstab(mergeNY14_df.OTHSVCEX, mergeNY14_df.age_group_14, margins=True);
other_by_age_14.columns = ['<18', '18-24', '25-34', '35-44', '45-54', '55-64', '>65', 'rowtotal'];
other_by_age_14.index= ["yes","no","coltotal"];
other_by_age_15 = pd.crosstab(mergeNY15_df.OTHSVCEX, mergeNY15_df.age_group_15, margins=True);
other_by_age_15.columns = ['<18', '18-24', '25-34', '35-44', '45-54', '55-64', '>65', 'rowtotal'];
other_by_age_15.index= ["yes","no","coltotal"]


# In[232]:

# crosstabs of internet type (satellite) by age group
satellite_by_age_13 = pd.crosstab(mergeNY13_df.SATELLITE, mergeNY13_df.age_group_13, margins=True);
satellite_by_age_13.columns = ['<18', '18-24', '25-34', '35-44', '45-54', '55-64', '>65', 'rowtotal'];
satellite_by_age_13.index= ["yes","no","coltotal"];
satellite_by_age_14 = pd.crosstab(mergeNY14_df.SATELLITE, mergeNY14_df.age_group_14, margins=True);
satellite_by_age_14.columns = ['<18', '18-24', '25-34', '35-44', '45-54', '55-64', '>65', 'rowtotal'];
satellite_by_age_14.index= ["yes","no","coltotal"];
satellite_by_age_15 = pd.crosstab(mergeNY15_df.SATELLITE, mergeNY15_df.age_group_15, margins=True);
satellite_by_age_15.columns = ['<18', '18-24', '25-34', '35-44', '45-54', '55-64', '>65', 'rowtotal'];
satellite_by_age_15.index= ["yes","no","coltotal"]


# In[233]:

# crosstabs of telephone access by age group > comparison group
telephone_by_age_13 = pd.crosstab(mergeNY13_df.TEL, mergeNY13_df.age_group_13, margins=True);
telephone_by_age_13.columns = ['<18', '18-24', '25-34', '35-44', '45-54', '55-64', '>65', 'rowtotal'];
telephone_by_age_13.index= ["yes","no","coltotal"];
telephone_by_age_14 = pd.crosstab(mergeNY14_df.TEL, mergeNY14_df.age_group_14, margins=True);
telephone_by_age_14.columns = ['<18', '18-24', '25-34', '35-44', '45-54', '55-64', '>65', 'rowtotal'];
telephone_by_age_14.index= ["yes","no","coltotal"];
telephone_by_age_15 = pd.crosstab(mergeNY15_df.TEL, mergeNY15_df.age_group_15, margins=True);
telephone_by_age_15.columns = ['<18', '18-24', '25-34', '35-44', '45-54', '55-64', '>65', 'rowtotal'];
telephone_by_age_15.index= ["yes","no","coltotal"]


# **Select cells and assign to variables**
# *Multiple traces per plot to show internet access type by age, 13-15*

# In[ ]:

# select crosstab by column and convert to percentile per age group
broadband_less18_13 = broadband_by_age_13['<18'];
bb_less18_13 = broadband_less18_13/broadband_less18_13.ix['coltotal', 'rowtotal'];
yes_bb_less18_13 = bb_less18_13[0];

broadband_1824_13 = broadband_by_age_13['18-24'];
bb_1824_13 = broadband_1824_13/broadband_1824_13.ix['coltotal', 'rowtotal'];
yes_bb_1824_13 = bb_1824_13[0];

broadband_2534_13 = broadband_by_age_13['25-34'];
bb_2534_13 = broadband_2534_13/broadband_2534_13.ix['coltotal', 'rowtotal'];
yes_bb_2534_13 = bb_2534_13[0];

broadband_3544_13 = broadband_by_age_13['35-44'];
bb_3544_13 = broadband_3544_13/broadband_3544_13.ix['coltotal', 'rowtotal'];
yes_bb_3544_13 = bb_3544_13[0];

broadband_4554_13 = broadband_by_age_13['45-54'];
bb_4554_13 = broadband_4554_13/broadband_4554_13.ix['coltotal', 'rowtotal'];
yes_bb_4554_13 = bb_4554_13[0];

broadband_5564_13 = broadband_by_age_13['55-64'];
bb_5564_13 = broadband_5564_13/broadband_5564_13.ix['coltotal', 'rowtotal'];
yes_bb_5564_13 = bb_5564_13[0];

broadband_more65_13 = broadband_by_age_13['>65'];
bb_more65_13 = broadband_more65_13/broadband_more65_13.ix['coltotal', 'rowtotal'];
yes_bb_more65_13 = bb_more65_13[0];

broadband_less18_14 = broadband_by_age_14['<18'];
bb_less18_14 = broadband_less18_14/broadband_less18_14.ix['coltotal', 'rowtotal'];
yes_bb_less18_14 = bb_less18_14[0];

broadband_1824_14 = broadband_by_age_14['18-24'];
bb_1824_14 = broadband_1824_13/broadband_1824_13.ix['coltotal', 'rowtotal'];
yes_bb_1824_14 = bb_1824_14[0];

broadband_2534_14 = broadband_by_age_14['25-34'];
bb_2534_14 = broadband_2534_14/broadband_2534_14.ix['coltotal', 'rowtotal'];
yes_bb_2534_14 = bb_2534_14[0];

broadband_3544_14 = broadband_by_age_14['35-44'];
bb_3544_14 = broadband_3544_14/broadband_3544_14.ix['coltotal', 'rowtotal'];
yes_bb_3544_14 = bb_3544_14[0];

broadband_4554_14 = broadband_by_age_14['45-54'];
bb_4554_14 = broadband_4554_14/broadband_4554_14.ix['coltotal', 'rowtotal'];
yes_bb_4554_14 = bb_4554_14[0];

broadband_5564_14 = broadband_by_age_14['55-64'];
bb_5564_14 = broadband_5564_14/broadband_5564_14.ix['coltotal', 'rowtotal'];
yes_bb_5564_14 = bb_5564_14[0];

broadband_more65_14 = broadband_by_age_14['>65'];
bb_more65_14 = broadband_more65_14/broadband_more65_14.ix['coltotal', 'rowtotal'];
yes_bb_more65_14 = bb_more65_14[0];

broadband_less18_15 = broadband_by_age_15['<18'];
bb_less18_15 = broadband_less18_15/broadband_less18_15.ix['coltotal', 'rowtotal'];
yes_bb_less18_15 = bb_less18_15[0];

broadband_1824_15 = broadband_by_age_15['18-24'];
bb_1824_15 = broadband_1824_15/broadband_1824_15.ix['coltotal', 'rowtotal'];
yes_bb_1824_15 = bb_1824_15[0];

broadband_2534_15 = broadband_by_age_15['25-34'];
bb_2534_15 = broadband_2534_15/broadband_2534_15.ix['coltotal', 'rowtotal'];
yes_bb_2534_15 = bb_2534_15[0];

broadband_3544_15 = broadband_by_age_15['35-44'];
bb_3544_15 = broadband_3544_15/broadband_3544_15.ix['coltotal', 'rowtotal'];
yes_bb_3544_15 = bb_3544_15[0];

broadband_4554_15 = broadband_by_age_15['45-54'];
bb_4554_15 = broadband_4554_15/broadband_4554_15.ix['coltotal', 'rowtotal'];
yes_bb_4554_15 = bb_4554_15[0];

broadband_5564_15 = broadband_by_age_15['55-64'];
bb_5564_15 = broadband_5564_15/broadband_5564_15.ix['coltotal', 'rowtotal'];
yes_bb_5564_15 = bb_5564_15[0];

broadband_more65_15 = broadband_by_age_15['>65']
bb_more65_15 = broadband_more65_15/broadband_more65_15.ix['coltotal', 'rowtotal'];
yes_bb_more65_15 = bb_more65_15[0]


# In[ ]:

# select crosstab by column and convert to percentile per age group
telephone_less18_13 = telephone_by_age_13['<18'];
tel_less18_13 = telephone_less18_13/telephone_less18_13.ix['coltotal', 'rowtotal'];
yes_tel_less18_13 = tel_less18_13[0];

telephone_1824_13 = telephone_by_age_13['18-24'];
tel_1824_13 = telephone_1824_13/telephone_1824_13.ix['coltotal', 'rowtotal'];
yes_tel_1824_13 = tel_1824_13[0];

telephone_2534_13 = telephone_by_age_13['25-34'];
tel_2534_13 = telephone_2534_13/telephone_2534_13.ix['coltotal', 'rowtotal'];
yes_tel_2534_13 = tel_2534_13[0];

telephone_3544_13 = telephone_by_age_13['35-44'];
tel_3544_13 = telephone_3544_13/telephone_3544_13.ix['coltotal', 'rowtotal'];
yes_tel_3544_13 = tel_3544_13[0];

telephone_4554_13 = telephone_by_age_13['45-54'];
tel_4554_13 = telephone_4554_13/telephone_4554_13.ix['coltotal', 'rowtotal'];
yes_tel_4554_13 = tel_4554_13[0];

telephone_5564_13 = telephone_by_age_13['55-64'];
tel_5564_13 = telephone_5564_13/telephone_5564_13.ix['coltotal', 'rowtotal'];
yes_tel_5564_13 = tel_5564_13[0];

telephone_more65_13 = telephone_by_age_13['>65'];
tel_more65_13 = telephone_more65_13/telephone_more65_13.ix['coltotal', 'rowtotal'];
yes_tel_more65_13 = tel_more65_13[0];

telephone_less18_14 = telephone_by_age_14['<18'];
tel_less18_14 = telephone_less18_14/telephone_less18_14.ix['coltotal', 'rowtotal'];
yes_tel_less18_14 = tel_less18_14[0];

telephone_1824_14 = telephone_by_age_14['18-24'];
tel_1824_14 = telephone_1824_13/telephone_1824_13.ix['coltotal', 'rowtotal'];
yes_tel_1824_14 = tel_1824_14[0];

telephone_2534_14 = telephone_by_age_14['25-34'];
tel_2534_14 = telephone_2534_14/telephone_2534_14.ix['coltotal', 'rowtotal'];
yes_tel_2534_14 = tel_2534_14[0];

telephone_3544_14 = telephone_by_age_14['35-44'];
tel_3544_14 = telephone_3544_14/telephone_3544_14.ix['coltotal', 'rowtotal'];
yes_tel_3544_14 = tel_3544_14[0];

telephone_4554_14 = telephone_by_age_14['45-54'];
tel_4554_14 = telephone_4554_14/telephone_4554_14.ix['coltotal', 'rowtotal'];
yes_tel_4554_14 = tel_4554_14[0];

telephone_5564_14 = telephone_by_age_14['55-64'];
tel_5564_14 = telephone_5564_14/telephone_5564_14.ix['coltotal', 'rowtotal'];
yes_tel_5564_14 = tel_5564_14[0];

telephone_more65_14 = telephone_by_age_14['>65'];
tel_more65_14 = telephone_more65_14/telephone_more65_14.ix['coltotal', 'rowtotal'];
yes_tel_more65_14 = tel_more65_14[0];

telephone_less18_15 = telephone_by_age_15['<18'];
tel_less18_15 = telephone_less18_15/telephone_less18_15.ix['coltotal', 'rowtotal'];
yes_tel_less18_15 = tel_less18_15[0];

telephone_1824_15 = telephone_by_age_15['18-24'];
tel_1824_15 = telephone_1824_15/telephone_1824_15.ix['coltotal', 'rowtotal'];
yes_tel_1824_15 = tel_1824_15[0];

telephone_2534_15 = telephone_by_age_15['25-34'];
tel_2534_15 = telephone_2534_15/telephone_2534_15.ix['coltotal', 'rowtotal'];
yes_tel_2534_15 = tel_2534_15[0];

telephone_3544_15 = telephone_by_age_15['35-44'];
tel_3544_15 = telephone_3544_15/telephone_3544_15.ix['coltotal', 'rowtotal'];
yes_tel_3544_15 = tel_3544_15[0];

telephone_4554_15 = telephone_by_age_15['45-54'];
tel_4554_15 = telephone_4554_15/telephone_4554_15.ix['coltotal', 'rowtotal'];
yes_tel_4554_15 = tel_4554_15[0];

telephone_5564_15 = telephone_by_age_15['55-64'];
tel_5564_15 = telephone_5564_15/telephone_5564_15.ix['coltotal', 'rowtotal'];
yes_tel_5564_15 = tel_5564_15[0];

telephone_more65_15 = telephone_by_age_15['>65']
tel_more65_15 = telephone_more65_15/telephone_more65_15.ix['coltotal', 'rowtotal'];
yes_tel_more65_15 = tel_more65_15[0]


# In[ ]:

# select crosstab by column and convert to percentile per age group
dialup_less18_13 = dialup_by_age_13['<18'];
dup_less18_13 = dialup_less18_13/dialup_less18_13.ix['coltotal', 'rowtotal'];
yes_dup_less18_13 = dup_less18_13[0];

dialup_1824_13 = dialup_by_age_13['18-24'];
dup_1824_13 = dialup_1824_13/dialup_1824_13.ix['coltotal', 'rowtotal'];
yes_dup_1824_13 = dup_1824_13[0];

dialup_2534_13 = dialup_by_age_13['25-34'];
dup_2534_13 = dialup_2534_13/dialup_2534_13.ix['coltotal', 'rowtotal'];
yes_dup_2534_13 = dup_2534_13[0];

dialup_3544_13 = dialup_by_age_13['35-44'];
dup_3544_13 = dialup_3544_13/dialup_3544_13.ix['coltotal', 'rowtotal'];
yes_dup_3544_13 = dup_3544_13[0];

dialup_4554_13 = dialup_by_age_13['45-54'];
dup_4554_13 = dialup_4554_13/dialup_4554_13.ix['coltotal', 'rowtotal'];
yes_dup_4554_13 = dup_4554_13[0];

dialup_5564_13 = dialup_by_age_13['55-64'];
dup_5564_13 = dialup_5564_13/dialup_5564_13.ix['coltotal', 'rowtotal'];
yes_dup_5564_13 = dup_5564_13[0];

dialup_more65_13 = dialup_by_age_13['>65'];
dup_more65_13 = dialup_more65_13/dialup_more65_13.ix['coltotal', 'rowtotal'];
yes_dup_more65_13 = dup_more65_13[0];

dialup_less18_14 = dialup_by_age_14['<18'];
dup_less18_14 = dialup_less18_14/dialup_less18_14.ix['coltotal', 'rowtotal'];
yes_dup_less18_14 = dup_less18_14[0];

dialup_1824_14 = dialup_by_age_14['18-24'];
dup_1824_14 = dialup_1824_13/dialup_1824_13.ix['coltotal', 'rowtotal'];
yes_dup_1824_14 = dup_1824_14[0];

dialup_2534_14 = dialup_by_age_14['25-34'];
dup_2534_14 = dialup_2534_14/dialup_2534_14.ix['coltotal', 'rowtotal'];
yes_dup_2534_14 = dup_2534_14[0];

dialup_3544_14 = dialup_by_age_14['35-44'];
dup_3544_14 = dialup_3544_14/dialup_3544_14.ix['coltotal', 'rowtotal'];
yes_dup_3544_14 = dup_3544_14[0];

dialup_4554_14 = dialup_by_age_14['45-54'];
dup_4554_14 = dialup_4554_14/dialup_4554_14.ix['coltotal', 'rowtotal'];
yes_dup_4554_14 = dup_4554_14[0];

dialup_5564_14 = dialup_by_age_14['55-64'];
dup_5564_14 = dialup_5564_14/dialup_5564_14.ix['coltotal', 'rowtotal'];
yes_dup_5564_14 = dup_5564_14[0];

dialup_more65_14 = dialup_by_age_14['>65'];
dup_more65_14 = dialup_more65_14/dialup_more65_14.ix['coltotal', 'rowtotal'];
yes_dup_more65_14 = dup_more65_14[0];

dialup_less18_15 = dialup_by_age_15['<18'];
dup_less18_15 = dialup_less18_15/dialup_less18_15.ix['coltotal', 'rowtotal'];
yes_dup_less18_15 = dup_less18_15[0];

dialup_1824_15 = dialup_by_age_15['18-24'];
dup_1824_15 = dialup_1824_15/dialup_1824_15.ix['coltotal', 'rowtotal'];
yes_dup_1824_15 = dup_1824_15[0];

dialup_2534_15 = dialup_by_age_15['25-34'];
dup_2534_15 = dialup_2534_15/dialup_2534_15.ix['coltotal', 'rowtotal'];
yes_dup_2534_15 = dup_2534_15[0];

dialup_3544_15 = dialup_by_age_15['35-44'];
dup_3544_15 = dialup_3544_15/dialup_3544_15.ix['coltotal', 'rowtotal'];
yes_dup_3544_15 = dup_3544_15[0];

dialup_4554_15 = dialup_by_age_15['45-54'];
dup_4554_15 = dialup_4554_15/dialup_4554_15.ix['coltotal', 'rowtotal'];
yes_dup_4554_15 = dup_4554_15[0];

dialup_5564_15 = dialup_by_age_15['55-64'];
dup_5564_15 = dialup_5564_15/dialup_5564_15.ix['coltotal', 'rowtotal'];
yes_dup_5564_15 = dup_5564_15[0];

dialup_more65_15 = dialup_by_age_15['>65']
dup_more65_15 = dialup_more65_15/dialup_more65_15.ix['coltotal', 'rowtotal'];
yes_dup_more65_15 = dup_more65_15[0]


# In[ ]:

# select crosstab by column and convert to percentile per age group
dsl_less18_13 = dsl_by_age_13['<18'];
dsl_less18_13 = dsl_less18_13/dsl_less18_13.ix['coltotal', 'rowtotal'];
yes_dsl_less18_13 = dsl_less18_13[0];

dsl_1824_13 = dsl_by_age_13['18-24'];
dsl_1824_13 = dsl_1824_13/dsl_1824_13.ix['coltotal', 'rowtotal'];
yes_dsl_1824_13 = dsl_1824_13[0];

dsl_2534_13 = dsl_by_age_13['25-34'];
dsl_2534_13 = dsl_2534_13/dsl_2534_13.ix['coltotal', 'rowtotal'];
yes_dsl_2534_13 = dsl_2534_13[0];

dsl_3544_13 = dsl_by_age_13['35-44'];
dsl_3544_13 = dsl_3544_13/dsl_3544_13.ix['coltotal', 'rowtotal'];
yes_dsl_3544_13 = dsl_3544_13[0];

dsl_4554_13 = dsl_by_age_13['45-54'];
dsl_4554_13 = dsl_4554_13/dsl_4554_13.ix['coltotal', 'rowtotal'];
yes_dsl_4554_13 = dsl_4554_13[0];

dsl_5564_13 = dsl_by_age_13['55-64'];
dsl_5564_13 = dsl_5564_13/dsl_5564_13.ix['coltotal', 'rowtotal'];
yes_dsl_5564_13 = dsl_5564_13[0];

dsl_more65_13 = dsl_by_age_13['>65'];
dsl_more65_13 = dsl_more65_13/dsl_more65_13.ix['coltotal', 'rowtotal'];
yes_dsl_more65_13 = dsl_more65_13[0];

dsl_less18_14 = dsl_by_age_14['<18'];
dsl_less18_14 = dsl_less18_14/dsl_less18_14.ix['coltotal', 'rowtotal'];
yes_dsl_less18_14 = dsl_less18_14[0];

dsl_1824_14 = dsl_by_age_14['18-24'];
dsl_1824_14 = dsl_1824_13/dsl_1824_13.ix['coltotal', 'rowtotal'];
yes_dsl_1824_14 = dsl_1824_14[0];

dsl_2534_14 = dsl_by_age_14['25-34'];
dsl_2534_14 = dsl_2534_14/dsl_2534_14.ix['coltotal', 'rowtotal'];
yes_dsl_2534_14 = dsl_2534_14[0];

dsl_3544_14 = dsl_by_age_14['35-44'];
dsl_3544_14 = dsl_3544_14/dsl_3544_14.ix['coltotal', 'rowtotal'];
yes_dsl_3544_14 = dsl_3544_14[0];

dsl_4554_14 = dsl_by_age_14['45-54'];
dsl_4554_14 = dsl_4554_14/dsl_4554_14.ix['coltotal', 'rowtotal'];
yes_dsl_4554_14 = dsl_4554_14[0];

dsl_5564_14 = dsl_by_age_14['55-64'];
dsl_5564_14 = dsl_5564_14/dsl_5564_14.ix['coltotal', 'rowtotal'];
yes_dsl_5564_14 = dsl_5564_14[0];

dsl_more65_14 = dsl_by_age_14['>65'];
dsl_more65_14 = dsl_more65_14/dsl_more65_14.ix['coltotal', 'rowtotal'];
yes_dsl_more65_14 = dsl_more65_14[0];

dsl_less18_15 = dsl_by_age_15['<18'];
dsl_less18_15 = dsl_less18_15/dsl_less18_15.ix['coltotal', 'rowtotal'];
yes_dsl_less18_15 = dsl_less18_15[0];

dsl_1824_15 = dsl_by_age_15['18-24'];
dsl_1824_15 = dsl_1824_15/dsl_1824_15.ix['coltotal', 'rowtotal'];
yes_dsl_1824_15 = dsl_1824_15[0];

dsl_2534_15 = dsl_by_age_15['25-34'];
dsl_2534_15 = dsl_2534_15/dsl_2534_15.ix['coltotal', 'rowtotal'];
yes_dsl_2534_15 = dsl_2534_15[0];

dsl_3544_15 = dsl_by_age_15['35-44'];
dsl_3544_15 = dsl_3544_15/dsl_3544_15.ix['coltotal', 'rowtotal'];
yes_dsl_3544_15 = dsl_3544_15[0];

dsl_4554_15 = dsl_by_age_15['45-54'];
dsl_4554_15 = dsl_4554_15/dsl_4554_15.ix['coltotal', 'rowtotal'];
yes_dsl_4554_15 = dsl_4554_15[0];

dsl_5564_15 = dsl_by_age_15['55-64'];
dsl_5564_15 = dsl_5564_15/dsl_5564_15.ix['coltotal', 'rowtotal'];
yes_dsl_5564_15 = dsl_5564_15[0];

dsl_more65_15 = dsl_by_age_15['>65']
dsl_more65_15 = dsl_more65_15/dsl_more65_15.ix['coltotal', 'rowtotal'];
yes_dsl_more65_15 = dsl_more65_15[0]


# In[ ]:

# select crosstab by column and convert to percentile per age group
fbr_less18_13 = fbr_by_age_13['<18'];
fbr_less18_13 = fbr_less18_13/fbr_less18_13.ix['coltotal', 'rowtotal'];
yes_fbr_less18_13 = fbr_less18_13[0];

fbr_1824_13 = fbr_by_age_13['18-24'];
fbr_1824_13 = fbr_1824_13/fbr_1824_13.ix['coltotal', 'rowtotal'];
yes_fbr_1824_13 = fbr_1824_13[0];

fbr_2534_13 = fbr_by_age_13['25-34'];
fbr_2534_13 = fbr_2534_13/fbr_2534_13.ix['coltotal', 'rowtotal'];
yes_fbr_2534_13 = fbr_2534_13[0];

fbr_3544_13 = fbr_by_age_13['35-44'];
fbr_3544_13 = fbr_3544_13/fbr_3544_13.ix['coltotal', 'rowtotal'];
yes_fbr_3544_13 = fbr_3544_13[0];

fbr_4554_13 = fbr_by_age_13['45-54'];
fbr_4554_13 = fbr_4554_13/fbr_4554_13.ix['coltotal', 'rowtotal'];
yes_fbr_4554_13 = fbr_4554_13[0];

fbr_5564_13 = fbr_by_age_13['55-64'];
fbr_5564_13 = fbr_5564_13/fbr_5564_13.ix['coltotal', 'rowtotal'];
yes_fbr_5564_13 = fbr_5564_13[0];

fbr_more65_13 = fbr_by_age_13['>65'];
fbr_more65_13 = fbr_more65_13/fbr_more65_13.ix['coltotal', 'rowtotal'];
yes_fbr_more65_13 = fbr_more65_13[0];

fbr_less18_14 = fbr_by_age_14['<18'];
fbr_less18_14 = fbr_less18_14/fbr_less18_14.ix['coltotal', 'rowtotal'];
yes_fbr_less18_14 = fbr_less18_14[0];

fbr_1824_14 = fbr_by_age_14['18-24'];
fbr_1824_14 = fbr_1824_13/fbr_1824_13.ix['coltotal', 'rowtotal'];
yes_fbr_1824_14 = fbr_1824_14[0];

fbr_2534_14 = fbr_by_age_14['25-34'];
fbr_2534_14 = fbr_2534_14/fbr_2534_14.ix['coltotal', 'rowtotal'];
yes_fbr_2534_14 = fbr_2534_14[0];

fbr_3544_14 = fbr_by_age_14['35-44'];
fbr_3544_14 = fbr_3544_14/fbr_3544_14.ix['coltotal', 'rowtotal'];
yes_fbr_3544_14 = fbr_3544_14[0];

fbr_4554_14 = fbr_by_age_14['45-54'];
fbr_4554_14 = fbr_4554_14/fbr_4554_14.ix['coltotal', 'rowtotal'];
yes_fbr_4554_14 = fbr_4554_14[0];

fbr_5564_14 = fbr_by_age_14['55-64'];
fbr_5564_14 = fbr_5564_14/fbr_5564_14.ix['coltotal', 'rowtotal'];
yes_fbr_5564_14 = fbr_5564_14[0];

fbr_more65_14 = fbr_by_age_14['>65'];
fbr_more65_14 = fbr_more65_14/fbr_more65_14.ix['coltotal', 'rowtotal'];
yes_fbr_more65_14 = fbr_more65_14[0];

fbr_less18_15 = fbr_by_age_15['<18'];
fbr_less18_15 = fbr_less18_15/fbr_less18_15.ix['coltotal', 'rowtotal'];
yes_fbr_less18_15 = fbr_less18_15[0];

fbr_1824_15 = fbr_by_age_15['18-24'];
fbr_1824_15 = fbr_1824_15/fbr_1824_15.ix['coltotal', 'rowtotal'];
yes_fbr_1824_15 = fbr_1824_15[0];

fbr_2534_15 = fbr_by_age_15['25-34'];
fbr_2534_15 = fbr_2534_15/fbr_2534_15.ix['coltotal', 'rowtotal'];
yes_fbr_2534_15 = fbr_2534_15[0];

fbr_3544_15 = fbr_by_age_15['35-44'];
fbr_3544_15 = fbr_3544_15/fbr_3544_15.ix['coltotal', 'rowtotal'];
yes_fbr_3544_15 = fbr_3544_15[0];

fbr_4554_15 = fbr_by_age_15['45-54'];
fbr_4554_15 = fbr_4554_15/fbr_4554_15.ix['coltotal', 'rowtotal'];
yes_fbr_4554_15 = fbr_4554_15[0];

fbr_5564_15 = fbr_by_age_15['55-64'];
fbr_5564_15 = fbr_5564_15/fbr_5564_15.ix['coltotal', 'rowtotal'];
yes_fbr_5564_15 = fbr_5564_15[0];

fbr_more65_15 = fbr_by_age_15['>65']
fbr_more65_15 = fbr_more65_15/fbr_more65_15.ix['coltotal', 'rowtotal'];
yes_fbr_more65_15 = fbr_more65_15[0]


# In[ ]:

# select crosstab by column and convert to percentile per age group
mod_less18_13 = mod_by_age_13['<18'];
mod_less18_13 = mod_less18_13/mod_less18_13.ix['coltotal', 'rowtotal'];
yes_mod_less18_13 = mod_less18_13[0];

mod_1824_13 = mod_by_age_13['18-24'];
mod_1824_13 = mod_1824_13/mod_1824_13.ix['coltotal', 'rowtotal'];
yes_mod_1824_13 = mod_1824_13[0];

mod_2534_13 = mod_by_age_13['25-34'];
mod_2534_13 = mod_2534_13/mod_2534_13.ix['coltotal', 'rowtotal'];
yes_mod_2534_13 = mod_2534_13[0];

mod_3544_13 = mod_by_age_13['35-44'];
mod_3544_13 = mod_3544_13/mod_3544_13.ix['coltotal', 'rowtotal'];
yes_mod_3544_13 = mod_3544_13[0];

mod_4554_13 = mod_by_age_13['45-54'];
mod_4554_13 = mod_4554_13/mod_4554_13.ix['coltotal', 'rowtotal'];
yes_mod_4554_13 = mod_4554_13[0];

mod_5564_13 = mod_by_age_13['55-64'];
mod_5564_13 = mod_5564_13/mod_5564_13.ix['coltotal', 'rowtotal'];
yes_mod_5564_13 = mod_5564_13[0];

mod_more65_13 = mod_by_age_13['>65'];
mod_more65_13 = mod_more65_13/mod_more65_13.ix['coltotal', 'rowtotal'];
yes_mod_more65_13 = mod_more65_13[0];

mod_less18_14 = mod_by_age_14['<18'];
mod_less18_14 = mod_less18_14/mod_less18_14.ix['coltotal', 'rowtotal'];
yes_mod_less18_14 = mod_less18_14[0];

mod_1824_14 = mod_by_age_14['18-24'];
mod_1824_14 = mod_1824_13/mod_1824_13.ix['coltotal', 'rowtotal'];
yes_mod_1824_14 = mod_1824_14[0];

mod_2534_14 = mod_by_age_14['25-34'];
mod_2534_14 = mod_2534_14/mod_2534_14.ix['coltotal', 'rowtotal'];
yes_mod_2534_14 = mod_2534_14[0];

mod_3544_14 = mod_by_age_14['35-44'];
mod_3544_14 = mod_3544_14/mod_3544_14.ix['coltotal', 'rowtotal'];
yes_mod_3544_14 = mod_3544_14[0];

mod_4554_14 = mod_by_age_14['45-54'];
mod_4554_14 = mod_4554_14/mod_4554_14.ix['coltotal', 'rowtotal'];
yes_mod_4554_14 = mod_4554_14[0];

mod_5564_14 = mod_by_age_14['55-64'];
mod_5564_14 = mod_5564_14/mod_5564_14.ix['coltotal', 'rowtotal'];
yes_mod_5564_14 = mod_5564_14[0];

mod_more65_14 = mod_by_age_14['>65'];
mod_more65_14 = mod_more65_14/mod_more65_14.ix['coltotal', 'rowtotal'];
yes_mod_more65_14 = mod_more65_14[0];

mod_less18_15 = mod_by_age_15['<18'];
mod_less18_15 = mod_less18_15/mod_less18_15.ix['coltotal', 'rowtotal'];
yes_mod_less18_15 = mod_less18_15[0];

mod_1824_15 = mod_by_age_15['18-24'];
mod_1824_15 = mod_1824_15/mod_1824_15.ix['coltotal', 'rowtotal'];
yes_mod_1824_15 = mod_1824_15[0];

mod_2534_15 = mod_by_age_15['25-34'];
mod_2534_15 = mod_2534_15/mod_2534_15.ix['coltotal', 'rowtotal'];
yes_mod_2534_15 = mod_2534_15[0];

mod_3544_15 = mod_by_age_15['35-44'];
mod_3544_15 = mod_3544_15/mod_3544_15.ix['coltotal', 'rowtotal'];
yes_mod_3544_15 = mod_3544_15[0];

mod_4554_15 = mod_by_age_15['45-54'];
mod_4554_15 = mod_4554_15/mod_4554_15.ix['coltotal', 'rowtotal'];
yes_mod_4554_15 = mod_4554_15[0];

mod_5564_15 = mod_by_age_15['55-64'];
mod_5564_15 = mod_5564_15/mod_5564_15.ix['coltotal', 'rowtotal'];
yes_mod_5564_15 = mod_5564_15[0];

mod_more65_15 = mod_by_age_15['>65']
mod_more65_15 = mod_more65_15/mod_more65_15.ix['coltotal', 'rowtotal'];
yes_mod_more65_15 = mod_more65_15[0]


# In[ ]:

# select crosstab by column and convert to percentile per age group
oth_less18_13 = oth_by_age_13['<18'];
oth_less18_13 = oth_less18_13/oth_less18_13.ix['coltotal', 'rowtotal'];
yes_oth_less18_13 = oth_less18_13[0];

oth_1824_13 = oth_by_age_13['18-24'];
oth_1824_13 = oth_1824_13/oth_1824_13.ix['coltotal', 'rowtotal'];
yes_oth_1824_13 = oth_1824_13[0];

oth_2534_13 = oth_by_age_13['25-34'];
oth_2534_13 = oth_2534_13/oth_2534_13.ix['coltotal', 'rowtotal'];
yes_oth_2534_13 = oth_2534_13[0];

oth_3544_13 = oth_by_age_13['35-44'];
oth_3544_13 = oth_3544_13/oth_3544_13.ix['coltotal', 'rowtotal'];
yes_oth_3544_13 = oth_3544_13[0];

oth_4554_13 = oth_by_age_13['45-54'];
oth_4554_13 = oth_4554_13/oth_4554_13.ix['coltotal', 'rowtotal'];
yes_oth_4554_13 = oth_4554_13[0];

oth_5564_13 = oth_by_age_13['55-64'];
oth_5564_13 = oth_5564_13/oth_5564_13.ix['coltotal', 'rowtotal'];
yes_oth_5564_13 = oth_5564_13[0];

oth_more65_13 = oth_by_age_13['>65'];
oth_more65_13 = oth_more65_13/oth_more65_13.ix['coltotal', 'rowtotal'];
yes_oth_more65_13 = oth_more65_13[0];

oth_less18_14 = oth_by_age_14['<18'];
oth_less18_14 = oth_less18_14/oth_less18_14.ix['coltotal', 'rowtotal'];
yes_oth_less18_14 = oth_less18_14[0];

oth_1824_14 = oth_by_age_14['18-24'];
oth_1824_14 = oth_1824_13/oth_1824_13.ix['coltotal', 'rowtotal'];
yes_oth_1824_14 = oth_1824_14[0];

oth_2534_14 = oth_by_age_14['25-34'];
oth_2534_14 = oth_2534_14/oth_2534_14.ix['coltotal', 'rowtotal'];
yes_oth_2534_14 = oth_2534_14[0];

oth_3544_14 = oth_by_age_14['35-44'];
oth_3544_14 = oth_3544_14/oth_3544_14.ix['coltotal', 'rowtotal'];
yes_oth_3544_14 = oth_3544_14[0];

oth_4554_14 = oth_by_age_14['45-54'];
oth_4554_14 = oth_4554_14/oth_4554_14.ix['coltotal', 'rowtotal'];
yes_oth_4554_14 = oth_4554_14[0];

oth_5564_14 = oth_by_age_14['55-64'];
oth_5564_14 = oth_5564_14/oth_5564_14.ix['coltotal', 'rowtotal'];
yes_oth_5564_14 = oth_5564_14[0];

oth_more65_14 = oth_by_age_14['>65'];
oth_more65_14 = oth_more65_14/oth_more65_14.ix['coltotal', 'rowtotal'];
yes_oth_more65_14 = oth_more65_14[0];

oth_less18_15 = oth_by_age_15['<18'];
oth_less18_15 = oth_less18_15/oth_less18_15.ix['coltotal', 'rowtotal'];
yes_oth_less18_15 = oth_less18_15[0];

oth_1824_15 = oth_by_age_15['18-24'];
oth_1824_15 = oth_1824_15/oth_1824_15.ix['coltotal', 'rowtotal'];
yes_oth_1824_15 = oth_1824_15[0];

oth_2534_15 = oth_by_age_15['25-34'];
oth_2534_15 = oth_2534_15/oth_2534_15.ix['coltotal', 'rowtotal'];
yes_oth_2534_15 = oth_2534_15[0];

oth_3544_15 = oth_by_age_15['35-44'];
oth_3544_15 = oth_3544_15/oth_3544_15.ix['coltotal', 'rowtotal'];
yes_oth_3544_15 = oth_3544_15[0];

oth_4554_15 = oth_by_age_15['45-54'];
oth_4554_15 = oth_4554_15/oth_4554_15.ix['coltotal', 'rowtotal'];
yes_oth_4554_15 = oth_4554_15[0];

oth_5564_15 = oth_by_age_15['55-64'];
oth_5564_15 = oth_5564_15/oth_5564_15.ix['coltotal', 'rowtotal'];
yes_oth_5564_15 = oth_5564_15[0];

oth_more65_15 = oth_by_age_15['>65']
oth_more65_15 = oth_more65_15/oth_more65_15.ix['coltotal', 'rowtotal'];
yes_oth_more65_15 = oth_more65_15[0]


# In[ ]:

# select crosstab by column and convert to percentile per age group
sat_less18_13 = sat_by_age_13['<18'];
sat_less18_13 = sat_less18_13/sat_less18_13.ix['coltotal', 'rowtotal'];
yes_sat_less18_13 = sat_less18_13[0];

sat_1824_13 = sat_by_age_13['18-24'];
sat_1824_13 = sat_1824_13/sat_1824_13.ix['coltotal', 'rowtotal'];
yes_sat_1824_13 = sat_1824_13[0];

sat_2534_13 = sat_by_age_13['25-34'];
sat_2534_13 = sat_2534_13/sat_2534_13.ix['coltotal', 'rowtotal'];
yes_sat_2534_13 = sat_2534_13[0];

sat_3544_13 = sat_by_age_13['35-44'];
sat_3544_13 = sat_3544_13/sat_3544_13.ix['coltotal', 'rowtotal'];
yes_sat_3544_13 = sat_3544_13[0];

sat_4554_13 = sat_by_age_13['45-54'];
sat_4554_13 = sat_4554_13/sat_4554_13.ix['coltotal', 'rowtotal'];
yes_sat_4554_13 = sat_4554_13[0];

sat_5564_13 = sat_by_age_13['55-64'];
sat_5564_13 = sat_5564_13/sat_5564_13.ix['coltotal', 'rowtotal'];
yes_sat_5564_13 = sat_5564_13[0];

sat_more65_13 = sat_by_age_13['>65'];
sat_more65_13 = sat_more65_13/sat_more65_13.ix['coltotal', 'rowtotal'];
yes_sat_more65_13 = sat_more65_13[0];

sat_less18_14 = sat_by_age_14['<18'];
sat_less18_14 = sat_less18_14/sat_less18_14.ix['coltotal', 'rowtotal'];
yes_sat_less18_14 = sat_less18_14[0];

sat_1824_14 = sat_by_age_14['18-24'];
sat_1824_14 = sat_1824_13/sat_1824_13.ix['coltotal', 'rowtotal'];
yes_sat_1824_14 = sat_1824_14[0];

sat_2534_14 = sat_by_age_14['25-34'];
sat_2534_14 = sat_2534_14/sat_2534_14.ix['coltotal', 'rowtotal'];
yes_sat_2534_14 = sat_2534_14[0];

sat_3544_14 = sat_by_age_14['35-44'];
sat_3544_14 = sat_3544_14/sat_3544_14.ix['coltotal', 'rowtotal'];
yes_sat_3544_14 = sat_3544_14[0];

sat_4554_14 = sat_by_age_14['45-54'];
sat_4554_14 = sat_4554_14/sat_4554_14.ix['coltotal', 'rowtotal'];
yes_sat_4554_14 = sat_4554_14[0];

sat_5564_14 = sat_by_age_14['55-64'];
sat_5564_14 = sat_5564_14/sat_5564_14.ix['coltotal', 'rowtotal'];
yes_sat_5564_14 = sat_5564_14[0];

sat_more65_14 = sat_by_age_14['>65'];
sat_more65_14 = sat_more65_14/sat_more65_14.ix['coltotal', 'rowtotal'];
yes_sat_more65_14 = sat_more65_14[0];

sat_less18_15 = sat_by_age_15['<18'];
sat_less18_15 = sat_less18_15/sat_less18_15.ix['coltotal', 'rowtotal'];
yes_sat_less18_15 = sat_less18_15[0];

sat_1824_15 = sat_by_age_15['18-24'];
sat_1824_15 = sat_1824_15/sat_1824_15.ix['coltotal', 'rowtotal'];
yes_sat_1824_15 = sat_1824_15[0];

sat_2534_15 = sat_by_age_15['25-34'];
sat_2534_15 = sat_2534_15/sat_2534_15.ix['coltotal', 'rowtotal'];
yes_sat_2534_15 = sat_2534_15[0];

sat_3544_15 = sat_by_age_15['35-44'];
sat_3544_15 = sat_3544_15/sat_3544_15.ix['coltotal', 'rowtotal'];
yes_sat_3544_15 = sat_3544_15[0];

sat_4554_15 = sat_by_age_15['45-54'];
sat_4554_15 = sat_4554_15/sat_4554_15.ix['coltotal', 'rowtotal'];
yes_sat_4554_15 = sat_4554_15[0];

sat_5564_15 = sat_by_age_15['55-64'];
sat_5564_15 = sat_5564_15/sat_5564_15.ix['coltotal', 'rowtotal'];
yes_sat_5564_15 = sat_5564_15[0];

sat_more65_15 = sat_by_age_15['>65']
sat_more65_15 = sat_more65_15/sat_more65_15.ix['coltotal', 'rowtotal'];
yes_sat_more65_15 = sat_more65_15[0]


# **Implement plots**
# *Multiple traces per plot to show internet access type by age, 13-15*

# In[ ]:

# Create and style traces
yes_bb_less18 = go.Scatter(
    x=['2013', '2014', '2015'],
    y=[yes_bb_less18_13, yes_bb_less18_14, yes_bb_less18_15],
    name = 'broadband'
);
yes_dup_less18 = go.Scatter(
    x=['2013', '2014', '2015'],
    y=[yes_dup_less18_13, yes_dup_less18_14, yes_dup_less18_15],
    name = 'dialup'
);
yes_dsl_less18 = go.Scatter(
    x=['2013', '2014', '2015'],
    y=[yes_dsl_less18_13, yes_dsl_less18_14, yes_dsl_less18_15],
    name = 'dsl'
);
yes_fbr_less18 = go.Scatter(
    x=['2013', '2014', '2015'],
    y=[yes_fbr_less18_13, yes_fbr_less18_14, yes_fbr_less18_15],
    name = 'fiber optic'
);
yes_mod_less18 = go.Scatter(
    x=['2013', '2014', '2015'],
    y=[yes_mod_less18_13, yes_mod_less18_14, yes_mod_less18_15],
    name = 'modem'
);
yes_sat_less18 = go.Scatter(
    x=['2013', '2014', '2015'],
    y=[yes_sat_less18_13, yes_sat_less18_14, yes_sat_less18_15],
    name = 'satellite'
);
yes_oth_less18 = go.Scatter(
    x=['2013', '2014', '2015'],
    y=[yes_oth_less18_13, yes_oth_less18_14, yes_oth_less18_15],
    name = 'other'
);
#yes_tel_less18 = go.Scatter(
#    x=['2013', '2014', '2015'],
#    y=[yes_tel_less18_13, yes_tel_less18_14, yes_tel_less18_15],
#    name = 'telephone'
#)

data = [yes_bb_less18, yes_dup_less18, yes_dsl_less18, yes_fbr_less18, yes_mod_less18, yes_sat_less18, yes_oth_less18]

# Edit the layout
layout = dict(title = 'Internet Access by Type for New Yorkers Ages 18 and Under, 2013-15',
             xaxis = dict(title = 'Year'),
             yaxis = dict(title = 'Percent'),
             )

fig = dict(data=data, layout=layout)
py.iplot(fig, filename='internet-access-type-less18-13-15')


# In[ ]:

# Create and style traces
yes_bb_1824 = go.Scatter(
    x=['2013', '2014', '2015'],
    y=[yes_bb_1824_13, yes_bb_1824_14, yes_bb_1824_15],
    name = 'broadband'
);
yes_dup_1824 = go.Scatter(
    x=['2013', '2014', '2015'],
    y=[yes_dup_1824_13, yes_dup_1824_14, yes_dup_1824_15],
    name = 'dialup'
);
yes_dsl_1824 = go.Scatter(
    x=['2013', '2014', '2015'],
    y=[yes_dsl_1824_13, yes_dsl_1824_14, yes_dsl_1824_15],
    name = 'dsl'
);
yes_fbr_1824 = go.Scatter(
    x=['2013', '2014', '2015'],
    y=[yes_fbr_1824_13, yes_fbr_1824_14, yes_fbr_1824_15],
    name = 'fiber optic'
);
yes_mod_1824 = go.Scatter(
    x=['2013', '2014', '2015'],
    y=[yes_mod_1824_13, yes_mod_1824_14, yes_mod_1824_15],
    name = 'modem'
);
yes_sat_1824 = go.Scatter(
    x=['2013', '2014', '2015'],
    y=[yes_sat_1824_13, yes_sat_1824_14, yes_sat_1824_15],
    name = 'satellite'
);
yes_oth_1824 = go.Scatter(
    x=['2013', '2014', '2015'],
    y=[yes_oth_1824_13, yes_oth_1824_14, yes_oth_1824_15],
    name = 'other'
);
#yes_tel_1824 = go.Scatter(
#    x=['2013', '2014', '2015'],
#    y=[yes_tel_1824_13, yes_tel_1824_14, yes_tel_1824_15],
#    name = 'telephone'
#)

data = [yes_bb_1824, yes_dup_1824, yes_dsl_1824, yes_fbr_1824, yes_mod_1824, yes_sat_1824, yes_oth_1824] 

# Edit the layout
layout = dict(title = 'Internet Access by Type for New Yorkers Ages 18 to 24, 2013-15',
             xaxis = dict(title = 'Year'),
             yaxis = dict(title = 'Percent'),
             )

fig = dict(data=data, layout=layout)
py.iplot(fig, filename='internet-access-type-1824-13-15')


# In[ ]:

# Create and style traces
yes_bb_2534 = go.Scatter(
    x=['2013', '2014', '2015'],
    y=[yes_bb_2534_13, yes_bb_2534_14, yes_bb_2534_15],
    name = 'broadband'
);
yes_dup_2534 = go.Scatter(
    x=['2013', '2014', '2015'],
    y=[yes_dup_2534_13, yes_dup_2534_14, yes_dup_2534_15],
    name = 'dialup'
);
yes_dsl_2534 = go.Scatter(
    x=['2013', '2014', '2015'],
    y=[yes_dsl_2534_13, yes_dsl_2534_14, yes_dsl_2534_15],
    name = 'dsl'
);
yes_fbr_2534 = go.Scatter(
    x=['2013', '2014', '2015'],
    y=[yes_fbr_2534_13, yes_fbr_2534_14, yes_fbr_2534_15],
    name = 'fiber optic'
);
yes_mod_2534 = go.Scatter(
    x=['2013', '2014', '2015'],
    y=[yes_mod_2534_13, yes_mod_2534_14, yes_mod_2534_15],
    name = 'modem'
);
yes_sat_2534 = go.Scatter(
    x=['2013', '2014', '2015'],
    y=[yes_sat_2534_13, yes_sat_2534_14, yes_sat_2534_15],
    name = 'satellite'
);
yes_oth_2534 = go.Scatter(
    x=['2013', '2014', '2015'],
    y=[yes_oth_2534_13, yes_oth_2534_14, yes_oth_2534_15],
    name = 'other'
);
#yes_tel_2534 = go.Scatter(
#    x=['2013', '2014', '2015'],
#    y=[yes_tel_2534_13, yes_tel_2534_14, yes_tel_2534_15],
#    name = 'telephone'
#)

data = [yes_bb_2534, yes_dup_2534, yes_dsl_2534, yes_fbr_2534, yes_mod_2534, yes_sat_2534, yes_oth_2534] 

# Edit the layout
layout = dict(title = 'Internet Access by Type for New Yorkers Ages 25 to 34, 2013-15',
             xaxis = dict(title = 'Year'),
             yaxis = dict(title = 'Percent'),
             )

fig = dict(data=data, layout=layout)
py.iplot(fig, filename='internet-access-type-2534-13-15')


# In[ ]:

# Create and style traces
yes_bb_3544 = go.Scatter(
    x=['2013', '2014', '2015'],
    y=[yes_bb_3544_13, yes_bb_3544_14, yes_bb_3544_15],
    name = 'broadband'
);
yes_dup_3544 = go.Scatter(
    x=['2013', '2014', '2015'],
    y=[yes_dup_3544_13, yes_dup_3544_14, yes_dup_3544_15],
    name = 'dialup'
);
yes_dsl_3544 = go.Scatter(
    x=['2013', '2014', '2015'],
    y=[yes_dsl_3544_13, yes_dsl_3544_14, yes_dsl_3544_15],
    name = 'dsl'
);
yes_fbr_3544 = go.Scatter(
    x=['2013', '2014', '2015'],
    y=[yes_fbr_3544_13, yes_fbr_3544_14, yes_fbr_3544_15],
    name = 'fiber optic'
);
yes_mod_3544 = go.Scatter(
    x=['2013', '2014', '2015'],
    y=[yes_mod_3544_13, yes_mod_3544_14, yes_mod_3544_15],
    name = 'modem'
);
yes_sat_3544 = go.Scatter(
    x=['2013', '2014', '2015'],
    y=[yes_sat_3544_13, yes_sat_3544_14, yes_sat_3544_15],
    name = 'satellite'
);
yes_oth_3544 = go.Scatter(
    x=['2013', '2014', '2015'],
    y=[yes_oth_3544_13, yes_oth_3544_14, yes_oth_3544_15],
    name = 'other'
);
#yes_tel_3544 = go.Scatter(
#    x=['2013', '2014', '2015'],
#    y=[yes_tel_3544_13, yes_tel_3544_14, yes_tel_3544_15],
#    name = 'telephone'
#)

data = [yes_bb_3544, yes_dup_3544, yes_dsl_3544, yes_fbr_3544, yes_mod_3544, yes_sat_3544, yes_oth_3544] 

# Edit the layout
layout = dict(title = 'Internet Access by Type for New Yorkers Ages 35 to 44, 2013-15',
             xaxis = dict(title = 'Year'),
             yaxis = dict(title = 'Percent'),
             )

fig = dict(data=data, layout=layout)
py.iplot(fig, filename='internet-access-type-3544-13-15')


# In[ ]:

# Create and style traces
yes_bb_4554 = go.Scatter(
    x=['2013', '2014', '2015'],
    y=[yes_bb_4554_13, yes_bb_4554_14, yes_bb_4554_15],
    name = 'broadband'
);
yes_dup_4554 = go.Scatter(
    x=['2013', '2014', '2015'],
    y=[yes_dup_4554_13, yes_dup_4554_14, yes_dup_4554_15],
    name = 'dialup'
);
yes_dsl_4554 = go.Scatter(
    x=['2013', '2014', '2015'],
    y=[yes_dsl_4554_13, yes_dsl_4554_14, yes_dsl_4554_15],
    name = 'dsl'
);
yes_fbr_4554 = go.Scatter(
    x=['2013', '2014', '2015'],
    y=[yes_fbr_4554_13, yes_fbr_4554_14, yes_fbr_4554_15],
    name = 'fiber optic'
);
yes_mod_4554 = go.Scatter(
    x=['2013', '2014', '2015'],
    y=[yes_mod_4554_13, yes_mod_4554_14, yes_mod_4554_15],
    name = 'modem'
);
yes_sat_4554 = go.Scatter(
    x=['2013', '2014', '2015'],
    y=[yes_sat_4554_13, yes_sat_4554_14, yes_sat_4554_15],
    name = 'satellite'
);
yes_oth_4554 = go.Scatter(
    x=['2013', '2014', '2015'],
    y=[yes_oth_4554_13, yes_oth_4554_14, yes_oth_4554_15],
    name = 'other'
);
#yes_tel_4554 = go.Scatter(
#    x=['2013', '2014', '2015'],
#    y=[yes_tel_4554_13, yes_tel_4554_14, yes_tel_4554_15],
#    name = 'telephone'
#)

data = [yes_bb_4554, yes_dup_4554, yes_dsl_4554, yes_fbr_4554, yes_mod_4554, yes_sat_4554, yes_oth_4554] 

# Edit the layout
layout = dict(title = 'Internet Access by Type for New Yorkers Ages 35 to 54, 2013-15',
             xaxis = dict(title = 'Year'),
             yaxis = dict(title = 'Percent'),
             )

fig = dict(data=data, layout=layout)
py.iplot(fig, filename='internet-access-type-4554-13-15')


# In[ ]:

# Create and style traces
yes_bb_5564 = go.Scatter(
    x=['2013', '2014', '2015'],
    y=[yes_bb_5564_13, yes_bb_5564_14, yes_bb_5564_15],
    name = 'broadband'
);
yes_dup_5564 = go.Scatter(
    x=['2013', '2014', '2015'],
    y=[yes_dup_5564_13, yes_dup_5564_14, yes_dup_5564_15],
    name = 'dialup'
);
yes_dsl_5564 = go.Scatter(
    x=['2013', '2014', '2015'],
    y=[yes_dsl_5564_13, yes_dsl_5564_14, yes_dsl_5564_15],
    name = 'dsl'
);
yes_fbr_5564 = go.Scatter(
    x=['2013', '2014', '2015'],
    y=[yes_fbr_5564_13, yes_fbr_5564_14, yes_fbr_5564_15],
    name = 'fiber optic'
);
yes_mod_5564 = go.Scatter(
    x=['2013', '2014', '2015'],
    y=[yes_mod_5564_13, yes_mod_5564_14, yes_mod_5564_15],
    name = 'modem'
);
yes_sat_5564 = go.Scatter(
    x=['2013', '2014', '2015'],
    y=[yes_sat_5564_13, yes_sat_5564_14, yes_sat_5564_15],
    name = 'satellite'
);
yes_oth_5564 = go.Scatter(
    x=['2013', '2014', '2015'],
    y=[yes_oth_5564_13, yes_oth_5564_14, yes_oth_5564_15],
    name = 'other'
);
#yes_tel_5564 = go.Scatter(
#    x=['2013', '2014', '2015'],
#    y=[yes_tel_5564_13, yes_tel_5564_14, yes_tel_5564_15],
#    name = 'telephone'
#)

data = [yes_bb_5564, yes_dup_5564, yes_dsl_5564, yes_fbr_5564, yes_mod_5564, yes_sat_5564, yes_oth_5564] 

# Edit the layout
layout = dict(title = 'Internet Access by Type for New Yorkers Ages 55 to 64, 2013-15',
             xaxis = dict(title = 'Year'),
             yaxis = dict(title = 'Percent'),
             )

fig = dict(data=data, layout=layout)
py.iplot(fig, filename='internet-access-type-5564-13-15')


# In[ ]:

# Create and style traces
yes_bb_more65 = go.Scatter(
    x=['2013', '2014', '2015'],
    y=[yes_bb_more65_13, yes_bb_more65_14, yes_bb_more65_15],
    name = 'broadband'
);
yes_dup_more65 = go.Scatter(
    x=['2013', '2014', '2015'],
    y=[yes_dup_more65_13, yes_dup_more65_14, yes_dup_more65_15],
    name = 'dialup'
);
yes_dsl_more65 = go.Scatter(
    x=['2013', '2014', '2015'],
    y=[yes_dsl_more65_13, yes_dsl_more65_14, yes_dsl_more65_15],
    name = 'dsl'
);
yes_fbr_more65 = go.Scatter(
    x=['2013', '2014', '2015'],
    y=[yes_fbr_more65_13, yes_fbr_more65_14, yes_fbr_more65_15],
    name = 'fiber optic'
);
yes_mod_more65 = go.Scatter(
    x=['2013', '2014', '2015'],
    y=[yes_mod_more65_13, yes_mod_more65_14, yes_mod_more65_15],
    name = 'modem'
);
yes_sat_more65 = go.Scatter(
    x=['2013', '2014', '2015'],
    y=[yes_sat_more65_13, yes_sat_more65_14, yes_sat_more65_15],
    name = 'satellite'
);
yes_oth_more65 = go.Scatter(
    x=['2013', '2014', '2015'],
    y=[yes_oth_more65_13, yes_oth_more65_14, yes_oth_more65_15],
    name = 'other'
);
#yes_tel_more65 = go.Scatter(
#    x=['2013', '2014', '2015'],
#    y=[yes_tel_more65_13, yes_tel_more65_14, yes_tel_more65_15],
#    name = 'telephone'
#)

data = [yes_bb_more65, yes_dup_more65, yes_dsl_more65, yes_fbr_more65, yes_mod_more65, yes_sat_more65, yes_oth_more65]

# Edit the layout
layout = dict(title = 'Internet Access by Type for New Yorkers Ages 65 and up, 2013-15',
             xaxis = dict(title = 'Year'),
             yaxis = dict(title = 'Percent'),
             )

fig = dict(data=data, layout=layout)
py.iplot(fig, filename='internet-access-type-more65-13-15')

