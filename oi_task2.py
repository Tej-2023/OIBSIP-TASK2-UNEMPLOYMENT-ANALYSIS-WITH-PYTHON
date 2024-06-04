

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import warnings
warnings.filterwarnings('ignore')

data=pd.read_csv('Unemployment in India.csv')
data=pd.read_csv('Unemployment_Rate_upto_11_2020.csv')
data

data.head()

data.dtypes
data.describe()

data.info()

data.isnull().sum()

plt.figure(figsize=(17, 5))
fig, ax = plt.subplots()

# Convert 'Region' column to string type
diag = plt.bar(data['Region'], data[' Estimated Unemployment Rate (%)'])

ax.set_xticklabels(ax.get_xticklabels(), rotation=60, ha='right')
plt.xlabel('Region')
plt.ylabel('Estimated Unemployment Rate (%)')
plt.title('Estimated Unemployment Rate by Region')
plt.show()

import seaborn as sns
import matplotlib.pyplot as plt

# Select only numerical columns for correlation calculation
numerical_data = data.select_dtypes(include=['float', 'int'])

sns.heatmap(numerical_data.corr(), annot=True, cmap='viridis')
plt.show()

sns.pairplot(data, hue="Region", palette="Dark2")
plt.show()

sns.histplot(x=' Estimated Employed', hue='Region',data=data)

data['Date']=pd.to_datetime(data[' Date'],infer_datetime_format=True)
data['Date']
