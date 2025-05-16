import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv("your_dataset.csv")
print(df.head())  # Display first few rows
df.fillna(df.mean(), inplace=True)  # Fill missing values with mean
print(df.info())  # Check data types and missing values
print(df.describe())  # Show summary statistics
print(df.corr())  # Check correlations between features
sns.histplot(df['column_name'], bins=30, kde=True)
plt.show()
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.show()
arr = np.array(df['column_name'])
print(np.mean(arr))  # Compute mean
print(np.std(arr))  # Compute standard deviation
