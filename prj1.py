import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv('products-100.csv')

df.head()

df.describe()

df.info()

data1 = df.loc[:,["Name","Price"]]

data1.dropna()

data1.isnull().sum()

data1.head()

sns.set(style="whitegrid")

plt.figure(figsize=(12,6))

sample = data1.sort_values(by='Price', ascending=False).head(10)

sns.barplot(data=sample, x='Name', y='Price', palette='viridis')

plt.title('Price by Product Name')
plt.xlabel('Product Name')
plt.ylabel('Price')

plt.xticks(rotation=80)

plt.show()