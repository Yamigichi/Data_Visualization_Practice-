#Exploring Datasets with pandas
#The Dataset: Immigration to Canada from 1980 to 2013
#pandas Basics
import numpy as np  # useful for many scientific computing in Python
import pandas as pd # primary data structure library

df_can = pd.read_excel('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/Canada.xlsx',
                       sheet_name='Canada by Citizenship',
                       skiprows=range(20),
                       skipfooter=2)
print ('Data read into a pandas dataframe!')
df_can.head()
df_can.tail()
       
df_can.info(verbose=False)
df_can.columns.values
df_can.index.values

print(type(df_can.columns))
print(type(df_can.index))

df_can.columns.tolist()
df_can.index.tolist()

print (type(df_can.columns.tolist()))
print (type(df_can.index.tolist()))

# size of dataframe (rows, columns)
df_can.shape 

# in pandas axis=0 represents rows (default) and axis=1 represents columns.
df_can.drop(['AREA','REG','DEV','Type','Coverage'], axis=1, inplace=True)
df_can.head(2)
#rename the columns 
df_can.rename(columns={'OdName':'Country', 'AreaName':'Continent', 'RegName':'Region'}, inplace=True)
df_can.columns

df_can['Total'] = df_can.sum(axis=1)
df_can.describe()

#pandas Intermediate: Indexing and Selection (slicing)
df_can.Country  # returns a series
df_can[['Country', 1980, 1981, 1982, 1983, 1984, 1985]] # returns a dataframe
# notice that 'Country' is string, and the years are integers. 
# for the sake of consistency, we will convert all column names to string later on.

df_can.set_index('Country', inplace=True)
# tip: The opposite of set is reset. So to reset the index, we can use df_can.reset_index()
df_can.head(3)
# optional: to remove the name of the index
df_can.index.name = None

#1. The full row data (all columns)
#2. For year 2013
#3. For years 1980 to 1985

# 1. the full row data (all columns)
print(df_can.loc['Japan'])
# alternate methods
print(df_can.iloc[87])
print(df_can[df_can.index == 'Japan'].T.squeeze())

# 2. for year 2013
print(df_can.loc['Japan', 2013])
# alternate method
print(df_can.iloc[87, 36]) # year 2013 is the last column, with a positional index of 36

# 3. for years 1980 to 1985
print(df_can.loc['Japan', [1980, 1981, 1982, 1983, 1984, 1984]])
print(df_can.iloc[87, [3, 4, 5, 6, 7, 8]])

df_can.columns = list(map(str, df_can.columns))
# [print (type(x)) for x in df_can.columns.values] #<-- uncomment to check type of column headers

# useful for plotting later on
years = list(map(str, range(1980, 2014)))
years

#Filtering based on a criteria
#To filter the dataframe based on a condition, we simply pass the condition as a boolean vector.

# 1. create the condition boolean series
condition = df_can['Continent'] == 'Asia'
print(condition)
# 2. pass this condition into the dataFrame
df_can[condition]
# we can pass mutliple criteria in the same line. 
# let's filter for AreaNAme = Asia and RegName = Southern Asia
df_can[(df_can['Continent']=='Asia') & (df_can['Region']=='Southern Asia')]
# note: When using 'and' and 'or' operators, pandas requires we use '&' and '|' instead of 'and' and 'or'
# don't forget to enclose the two conditions in parentheses
#review the changes we have made to our dataframe.
print('data dimensions:', df_can.shape)
print(df_can.columns)
df_can.head(2)

#Visualizing Data using Matplotlib
# we are using the inline backend
%matplotlib inline 

import matplotlib as mpl
import matplotlib.pyplot as plt

#*optional: check if Matplotlib is loaded.
#print ('Matplotlib version: ', mpl.__version__) # >= 2.0.0
#*optional: apply a style to Matplotlib.
print(plt.style.available)
mpl.style.use(['ggplot']) # optional: for ggplot-like style

#Line Pots (Series/Dataframe)
#Immgration from country 
haiti = df_can.loc['Haiti', years] # passing in years 1980 - 2013 to exclude the 'total' column
haiti.plot()

haiti.index = haiti.index.map(int) # let's change the index values of Haiti to type integer for plotting
haiti.plot(kind='line')
plt.title('Immigration from Haiti')
plt.ylabel('Number of immigrants')
plt.xlabel('Years')
plt.show() # need this line to show the updates made to the figure
haiti.head()

haiti.plot(kind='line')
plt.title('Immigration from Haiti')
plt.ylabel('Number of Immigrants')
plt.xlabel('Years')
# annotate the 2010 Earthquake. 
# syntax: plt.text(x, y, label)
plt.text(2000, 6000, '2010 Earthquake') # see note below
plt.show() 
plt.text(2000, 6000, '2010 Earthquake') # years stored as type int
plt.text(20, 6000, '2010 Earthquake') # years stored as type int


df_CI = df_can.loc[['India', 'China'], years]
df_CI.head()

df_CI.plot(kind='line')

df_CI.index = df_CI.index.map(int) # let's change the index values of df_CI to type integer for plotting
df_CI.plot(kind='line')

plt.title('Immigrants from China and India')
plt.ylabel('Number of Immigrants')
plt.xlabel('Years')

plt.show()

inplace = True #paramemter saves the changes to the original df_can dataframe
df_can.sort_values(by='Total', ascending=False, axis=0, inplace=True)

    # get the top 5 entries
df_top5 = df_can.head(5)

    # transpose the dataframe
df_top5 = df_top5[years].transpose() 

print(df_top5)


    #Step 2: Plot the dataframe. To make the plot more readeable, we will change the size using the `figsize` parameter.
df_top5.index = df_top5.index.map(int) # let's change the index values of df_top5 to type integer for plotting
df_top5.plot(kind='line', figsize=(14, 8)) # pass a tuple (x, y) size



plt.title('Immigration Trend of Top 5 Countries')
plt.ylabel('Number of Immigrants')
plt.xlabel('Years')


plt.show()
df_CI = df_CI.transpose()
df_CI.head()


