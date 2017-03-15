
# coding: utf-8

# In[27]:

import boto
import pandas as pd
import numpy as np
import cufflinks as cf
import scipy.stats as stats
from scipy.stats import chi2_contingency
import plotly.graph_objs as go
import plotly.offline as py
from plotly import tools
import statsmodels.formula.api as sm

cf.go_offline()
py.init_notebook_mode()

c = boto.connect_s3()
b = c.get_bucket('nichung-datasets')


# **Load CSV and assign to dataframe**

# In[3]:

mergeNY13_df = pd.read_csv('s3:/nichung-datasets/ss13ny.csv')


# In[5]:

mergeNY14_df = pd.read_csv('s3:/nichung-datasets/ss14ny.csv')


# In[7]:

mergeNY15_df = pd.read_csv('s3:/nichung-datasets/ss15ny.csv')


# In[8]:

ny_puma_df = pd.read_csv('s3:/nichung-datasets/puma_ny.csv')


# ***
# 
# ## r a c e  &  o t h e r  s e s  i n d i c a t o r s 
# 
# Questions (test):
# + what does internet access look like against health insurance coverage type, by age group?
# + what does internet access look like against health insurance coverage type, by age group?
# 
# ***

# In[9]:

#health insurance coverage

#by age
coverage_by_age_13 = pd.crosstab(mergeNY13_df.HICOV, mergeNY13_df.age_group_13, margins=True)
coverage_by_age_13.columns = ['<18', '18-24', '25-34', '35-44', '45-54', '55-64', '>65', 'rowtotal']
coverage_by_age_13.index= ["yes","no","coltotal"] 

coverage_by_age_13


# In[10]:

#by race
coverage_by_race_13 = pd.crosstab(mergeNY13_df.RAC1P, mergeNY13_df.HICOV, margins=True)
coverage_by_race_13.columns= ["yes","no","rowtotal"] 
coverage_by_race_13.index = ['white', 'black', 'american indian', 'alaska native', 'catch-all native', 'asian', 'pacific islander', 'other', '2+ races', 'coltotal']

insured_by_race_13 = coverage_by_race_13/coverage_by_race_13.ix['coltotal', 'rowtotal']

insured_by_race_13_no_total = insured_by_race_13.ix[0:9,0:2]
insured_by_race_13_no_total


# In[11]:

insured_by_race_13_no_total.iplot(kind='bar', barmode='stack', filename='charts/health-coverage-by-race.html')


# In[12]:

#by race
coverage_by_race_13 = pd.crosstab(mergeNY13_df.HICOV, mergeNY13_df.RAC1P, margins=True)
coverage_by_race_13.columns = ['white', 'black', 'american indian', 'alaska native', 'catch-all native', 'asian', 'pacific islander', 'other', '2+ races', 'rowtotal']
coverage_by_race_13.index = ["yes","no","coltotal"]

coverage_by_race_13_no_total = coverage_by_race_13.ix[0:2,0:9]
coverage_by_race_13_no_total


# In[13]:

coverage_by_race_13_no_total.iplot(kind='bar', barmode='stack', filename='charts/health-coverage-by-race.html')


# In[14]:

#private coverage
privcov_by_age_13 = pd.crosstab(mergeNY13_df.PRIVCOV, mergeNY13_df.age_group_13, margins=True)
privcov_by_age_13.columns = ['<18', '18-24', '25-34', '35-44', '45-54', '55-64', '>65', 'rowtotal']
privcov_by_age_13.index= ["yes","no","coltotal"]

#public coverage
pubcov_by_age_13 = pd.crosstab(mergeNY13_df.PUBCOV, mergeNY13_df.age_group_13, margins=True)
pubcov_by_age_13.columns = ['<18', '18-24', '25-34', '35-44', '45-54', '55-64', '>65', 'rowtotal']
pubcov_by_age_13.index= ["yes","no","coltotal"]

#internet access
access_by_age_13 = pd.crosstab(mergeNY13_df.ACCESS, mergeNY13_df.age_group_13, margins=True)
access_by_age_13.columns = ['<18', '18-24', '25-34', '35-44', '45-54', '55-64', '>65', 'rowtotal']
access_by_age_13.index= ["yes","kinda", "no","coltotal"]


# In[15]:

pubcov_by_age_13 = pd.crosstab(mergeNY13_df.PUBCOV, mergeNY13_df.age_group_13, margins=True);
pubcov_by_age_13.columns = ['<18', '18-24', '25-34', '35-44', '45-54', '55-64', '>65', 'rowtotal'];
pubcov_by_age_13.index= ["yes","no","coltotal"];
access_by_age_13 = pd.crosstab(mergeNY13_df.ACCESS, mergeNY13_df.age_group_13, margins=True);
access_by_age_13.columns = ['<18', '18-24', '25-34', '35-44', '45-54', '55-64', '>65', 'rowtotal'];
access_by_age_13.index= ["yes","kinda", "no","coltotal"];


# In[16]:

access_by_age_13 = pd.crosstab(mergeNY13_df.ACCESS, mergeNY13_df.age_group_13, margins=True);
access_by_age_13.columns = ['<18', '18-24', '25-34', '35-44', '45-54', '55-64', '>65', 'rowtotal'];
access_by_age_13.index= ["yes","kinda", "no","coltotal"];


# In[17]:

# select crosstab by column and convert to percentile per age group
privc_less18_13 = privcov_by_age_13['<18'];
private_less18_13 = privc_less18_13/privc_less18_13.ix['coltotal', 'rowtotal'];
yes_private_less18_13 = private_less18_13[0];

privc_1824_13 = privcov_by_age_13['18-24'];
private_1824_13 = privc_1824_13/privc_1824_13.ix['coltotal', 'rowtotal'];
yes_private_1824_13 = private_1824_13[0];

privc_2534_13 = privcov_by_age_13['25-34'];
private_2534_13 = privc_2534_13/privc_2534_13.ix['coltotal', 'rowtotal'];
yes_private_2534_13 = private_2534_13[0];

privc_3544_13 = privcov_by_age_13['35-44'];
private_3544_13 = privc_3544_13/privc_3544_13.ix['coltotal', 'rowtotal'];
yes_private_3544_13 = private_3544_13[0];

privc_4554_13 = privcov_by_age_13['45-54'];
private_4554_13 = privc_4554_13/privc_4554_13.ix['coltotal', 'rowtotal'];
yes_private_4554_13 = private_4554_13[0];

privc_5564_13 = privcov_by_age_13['55-64'];
private_5564_13 = privc_5564_13/privc_5564_13.ix['coltotal', 'rowtotal'];
yes_private_5564_13 = private_5564_13[0];

privc_more65_13 = privcov_by_age_13['>65'];
private_more65_13 = privc_more65_13/privc_more65_13.ix['coltotal', 'rowtotal'];
yes_private_more65_13 = private_more65_13[0];

# select crosstab by column and convert to percentile per age group
pubc_less18_13 = pubcov_by_age_13['<18'];
public_less18_13 = pubc_less18_13/pubc_less18_13.ix['coltotal', 'rowtotal'];
yes_public_less18_13 = public_less18_13[0];

pubc_1824_13 = pubcov_by_age_13['18-24'];
public_1824_13 = pubc_1824_13/pubc_1824_13.ix['coltotal', 'rowtotal'];
yes_public_1824_13 = public_1824_13[0];

pubc_2534_13 = pubcov_by_age_13['25-34'];
public_2534_13 = pubc_2534_13/pubc_2534_13.ix['coltotal', 'rowtotal'];
yes_public_2534_13 = public_2534_13[0];

pubc_3544_13 = pubcov_by_age_13['35-44'];
public_3544_13 = pubc_3544_13/pubc_3544_13.ix['coltotal', 'rowtotal'];
yes_public_3544_13 = public_3544_13[0];

pubc_4554_13 = pubcov_by_age_13['45-54'];
public_4554_13 = pubc_4554_13/pubc_4554_13.ix['coltotal', 'rowtotal'];
yes_public_4554_13 = public_4554_13[0];

pubc_5564_13 = pubcov_by_age_13['55-64'];
public_5564_13 = pubc_5564_13/pubc_5564_13.ix['coltotal', 'rowtotal'];
yes_public_5564_13 = public_5564_13[0];

pubc_more65_13 = pubcov_by_age_13['>65'];
public_more65_13 = pubc_more65_13/pubc_more65_13.ix['coltotal', 'rowtotal'];
yes_public_more65_13 = public_more65_13[0];

# select crosstab by column and convert to percentile per age group
iacc_less18_13 = access_by_age_13['<18'];
access_less18_13 = iacc_less18_13/iacc_less18_13.ix['coltotal', 'rowtotal'];
yes_access_less18_13 = access_less18_13[0];

iacc_1824_13 = access_by_age_13['18-24'];
access_1824_13 = iacc_1824_13/iacc_1824_13.ix['coltotal', 'rowtotal'];
yes_access_1824_13 = access_1824_13[0];

iacc_2534_13 = access_by_age_13['25-34'];
access_2534_13 = iacc_2534_13/iacc_2534_13.ix['coltotal', 'rowtotal'];
yes_access_2534_13 = access_2534_13[0];

iacc_3544_13 = access_by_age_13['35-44'];
access_3544_13 = iacc_3544_13/iacc_3544_13.ix['coltotal', 'rowtotal'];
yes_access_3544_13 = access_3544_13[0];

iacc_4554_13 = access_by_age_13['45-54'];
access_4554_13 = iacc_4554_13/iacc_4554_13.ix['coltotal', 'rowtotal'];
yes_access_4554_13 = access_4554_13[0];

iacc_5564_13 = access_by_age_13['55-64'];
access_5564_13 = iacc_5564_13/iacc_5564_13.ix['coltotal', 'rowtotal'];
yes_access_5564_13 = access_5564_13[0];

iacc_more65_13 = access_by_age_13['>65'];
access_more65_13 = iacc_more65_13/iacc_more65_13.ix['coltotal', 'rowtotal'];
yes_access_more65_13 = access_more65_13[0];


# In[18]:

# Create and style traces
yes_acc_13 = go.Bar(
    x=['< 18', '18-24', '25-34', '35-44', '45-54', '55-64', '> 64'],
    y=[yes_access_less18_13, yes_access_1824_13, yes_access_2534_13, yes_access_3544_13, yes_access_4554_13, yes_access_5564_13, yes_access_more65_13],
    name = 'internet access'
);

yes_privc_13 = go.Bar(
    x=['< 18', '18-24', '25-34', '35-44', '45-54', '55-64', '> 64'],
    y=[yes_private_less18_13, yes_private_1824_13, yes_private_2534_13, yes_private_3544_13, yes_private_4554_13, yes_private_5564_13, yes_private_more65_13],
    name = 'private health insurance'
);

yes_pubc_13 = go.Bar(
    x=['< 18', '18-24', '25-34', '35-44', '45-54', '55-64', '> 64'],
    y=[yes_public_less18_13, yes_public_1824_13, yes_public_2534_13, yes_public_3544_13, yes_public_4554_13, yes_public_5564_13, yes_public_more65_13],
    name = 'public health insurance'
);

data = [yes_acc_13, yes_pubc_13, yes_privc_13]

# Edit the layout
layout = go.Layout(
    title = 'Internet Access and Health Insurance by Type for New Yorkers by Age, 2013-15',
    xaxis = dict(title = 'Age Group'),
    yaxis = dict(title = 'Percent of Population'),
    barmode = 'group'
)

fig = go.Figure(data=data, layout=layout)
py.iplot(fig, filename='internet-access-and-health-insurance-type-by-age-13')


# ###race eda
# 
# Questions:
# + distribution of race?
# + internet access type by race?

# In[19]:

# chi-squared goodness-of-fit test for categorical variable 'RAC1P'
# todo


# In[20]:

#race by age group
race_by_age_13 = pd.crosstab(mergeNY13_df.RAC1P, mergeNY13_df.age_group_13, margins=True);
race_by_age_13.columns = ['<18', '18-24', '25-34', '35-44', '45-54', '55-64', '>65', 'rowtotal'];
race_by_age_13.index= ['white', 'black', 'american indian', 'alaska native', 'catch-all native', 'asian', 'pacific islander', 'other', '2+ races', 'coltotal'];
race_by_age_13


# In[21]:

# chi-squared test of independence to test null hypothesis 
# that there is no association between race and age 
observed = race_by_age_13.ix[0:9,0:7]

observed


# In[22]:

# expected
expected = np.outer(race_by_age_13['rowtotal'][0:9],
                   race_by_age_13.ix['coltotal'][0:7]) / 194273

expected = pd.DataFrame(expected)

expected.columns = ['<18', '18-24', '25-34', '35-44', '45-54', '55-64', '>65']
expected.index= ['white', 'black', 'american indian', 'alaska native', 'catch-all native', 'asian', 'pacific islander', 'other', '2+ races']

expected


# In[29]:

stats.chi2_contingency(observed=observed)


# In[24]:

# chi-squared test of independence to test null hypothesis 
# that there is no association between access and race 
access_by_race_13 = pd.crosstab(mergeNY13_df.RAC1P, mergeNY13_df.ACCESS, margins=True);
access_by_race_13.columns = ['yes', 'yes w/o sub', 'no', 'rowtotal'];
access_by_race_13.index= ['white', 'black', 'american indian', 'alaska native', 'catch-all native', 'asian', 'pacific islander', 'other', '2+ races', 'coltotal'];
access_by_race_13


# In[25]:

race_age_observed = access_by_race_13.ix[0:9,0:3]

race_age_observed


# In[28]:

chi2_contingency(race_age_observed)
stats.chi2_contingency(race_age_observed)


# In[30]:

age = mergeNY13_df.AGEP
fam_income = mergeNY13_df.FINCP
race = mergeNY13_df.RAC1P


# In[31]:

result = sm.ols(formula="age ~ fam_income + race", data=mergeNY13_df).fit()
print result.params


# In[32]:

print result.summary()


# In[66]:

mergeNY14_df.GRPIP.describe()


# In[64]:

mergeNY13_df.GRPIP.iplot(kind='box', filename='rent-of-income-13')


# In[70]:

grpip_14 = mergeNY14_df.GRPIP.apply(pd.to_numeric, errors='coerce')


# In[71]:

grpip_14.iplot(kind='box', filename='rent-of-income-14')


# In[65]:

mergeNY15_df.GRPIP.iplot(kind='box', filename='rent-of-income-15')


# In[80]:

mergeNY13_df.FINCP.iplot(kind='box', filename='fam_income_13')


# In[79]:

mergeNY13_df.HINCP.iplot(kind='box', filename='hh_income_13')


# In[78]:

mergeNY14_df.FINCP.iplot(kind='box', filename='fam_income_14')


# In[77]:

mergeNY15_df.FINCP.iplot(kind='box', filename='fam_income_15')


# In[ ]:



