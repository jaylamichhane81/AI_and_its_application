# -*- coding: utf-8 -*-
"""Week2Exam Video Game Project.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/13NjApQ6FO7xOcpVymsWdVQhHqhmH68_h

#Video Game Sales Project

This Dataset provides up-to-date information on the sales performance and popularity of various video games worldwide. The data includes the name, platform, year of release, genre, publisher, and sales in North America, Europe, Japan, and other regions.
"""

#Import all needed libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv('vgsales.csv')
df.head()

#Creating copy

df_copy = df.copy()

"""# Step 1: Data Profiling"""

# check null value,dtpes and columns name
df_copy.info()

df_copy.head() #check 5 row

#to check how many rows and column present in dataset
df_copy.shape

#datasetko statistics patta lagako
df_copy.describe()

df_copy['Genre'].value_counts() # kun type ko game haru kati patak count vayo

df_copy['Platform'].value_counts() # kun console or device (platform) ma kati patak game xa

"""#Data Quality Check"""

# to check missing value in dataset or not
df_copy.isnull().sum()

df_copy.isnull().sum().sum() #check totall missing value altogethere.

# Fill missing Year
df_copy['Year'].fillna(df_copy['Year'].mode()[0], inplace=True)

# Fill missing Publisher
df['Publisher'].fillna(df['Publisher'].mode()[0], inplace=True)

df_copy.isnull().sum().sum() # (o null value) all 329 null value clear

# Convert 'Year' column from float to int
df_copy['Year'] = df_copy['Year'].astype(int)

df_copy.head(3)

"""#Duplicate Check"""

df_copy.duplicated().sum() #check duplicate value

"""#Visualization"""

sns.histplot(df_copy['Global_Sales'],bins=10)
plt.title('Global Sales')
plt.show()

"""#Description of this histogram plot

yo plot le Global Sales world wide distribution dekhauxa .yo plot le histogram plot show garxa ra kati ota video games le kati sales gareko xa.

bins=10 le data lai 10 bhagma (intervals) ma baadiyeko xa

X-axis ma Global Sales (sales bhayeko rakam),

Y-axis ma kati ota gameharu tyo salesbhayeko area bhitra parxa
"""

sns.scatterplot(x='Year',y='Global_Sales',data=df_copy)
plt.title('Sales over Years')
plt.show()

"""#Description of this scatter plot

harek video game ko globally sales kun year ma kati sales vayo vanera dekhauxa.

harek point (dot) ek game ho

X-axis game launched vayeko year Y-axis ma tyo gameko global sales
"""

sns.heatmap(df_copy[['NA_Sales','EU_Sales','JP_Sales','Other_Sales','Global_Sales']].corr(), annot=True, cmap='coolwarm')
plt.show()

"""#Description of this heatmap

yo heatmap plot le sales bhayeko video game different country haruko ko bichko correlation dekhauxa.

df[['NA_Sales','EU_Sales','JP_Sales','Other_Sales','Global_Sales']] yo column ko sales check garda

.corr() yesle yo sano-sano box ko bichko correlation matrix banauxa.

+1=strong positive -1=strong negative 0=no correlation

annot=True: harek box bhitra correlation number dekhauxa

cmap='coolwarm': nilo-rato colorko use hunxa (blue color ko vayo vane less coreelation hunxa .red color ko vayo vane high correlation hunxa
"""

plt.figure(figsize=(10,6))
sns.kdeplot(data=df_copy, x='Global_Sales', fill=True, color='skyblue')

plt.title('Global Sales(KDE Plot)')
plt.xlabel('Global Sales')
plt.ylabel('Density')
plt.grid(True)
plt.show()

"""#Description of this KDE plot

A smooth curve showing how video game sales are distributed globally.

The peak of the curve shows where most sales values lie (e.g., around 0.1–0.5 million units).

It's useful to identify concentration and spread in continuous data.

#Remove Outlier
"""

q1=df_copy['Global_Sales'].quantile(0.25) # first 25% vanda kam value nikaleko
q3=df_copy['Global_Sales'].quantile(0.75) #75% vanda kam value nikaleko
iqr=q3-q1 #interquartile range middle part dekhauxa
df_copy=df_copy[(df_copy['Global_Sales']>=q1-1.5*iqr) & (df_copy['Global_Sales']<=q3+1.5*iqr)] # es line le Q1 - 1.5×IQR vanda kam ra Q3 + 1.5×IQR vanda badi bhayeko value harulai hatauxa.
# esko sabaivanda sano value ra sabai vanda thulo value lai remove garera normal range ko balance ma milayera accouracy result ramro dinxa.

#After remove outliers histogram plot
sns.histplot(df_copy['Global_Sales'],bins=10)
plt.title('Global Sales')
plt.show()

#after remove outliers kde-plot
plt.figure(figsize=(10,6))
sns.kdeplot(data=df_copy, x='Global_Sales', fill=True, color='skyblue')

plt.title('Global Sales(KDE Plot)')
plt.xlabel('Global Sales')
plt.ylabel('Density')
plt.grid(True)
plt.show()

"""#Feature Engineering"""

df_copy['NA_to_Global'] = df_copy['NA_Sales'] / df_copy['Global_Sales']#yo line NA_to_Global naya naam ko column,jasma North America ko sales lai Global sales bata divide gareko hunxa
sns.scatterplot(x='NA_to_Global', y='Global_Sales', data=df_copy) #NA_to_Global (x-axis) र Global_Sales (y-axis) bichko relation dekhauna scatter plot banainxa.
plt.title("NA/Global Sales Ratio"); plt.show() #Visualized the new feature

df_copy.head(3)

"""#Summarize Findings"""

print("Top Genres by Global Sales:\n", df_copy.groupby('Genre')['Global_Sales'].sum().sort_values(ascending=False).head())
print("Top Platforms by Global Sales:\n", df_copy.groupby('Platform')['Global_Sales'].sum().sort_values(ascending=False).head())
print("Top Publishers by Global Sales:\n", df_copy.groupby('Publisher')['Global_Sales'].sum().sort_values(ascending=False).head())

"""Action Sports game haru sabai vanda badi sales bayeko xa

PlayStation 2, X360, ra PS3 sales badi dekhiyeko xa

NA, north america ma 50%.badi sales bhayeko dekhiyo 2005-2010 ko bichma.

Nintendo DS/Wii/PS2 le karanle

Outliers Wii Sports sab banda badi sales bhayeko sports
"""

