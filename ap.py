import seaborn as sns
import matplotlib.pyplot as plt

# Sample dataset
tips = sns.load_dataset('tips')

# Compute correlation matrix
corr = tips.corr()

# Create a heatmap
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Feature Correlation Heatmap")
plt.show()
sns.pairplot(tips, hue='sex', diag_kind='kde')
plt.show()
sns.violinplot(x='day', y='total_bill', data=tips, palette='pastel')
plt.title("Total Bill Distribution Across Days")
plt.show()
sns.boxenplot(x='day', y='total_bill', data=tips)
plt.title("Boxen Plot of Total Bill Across Days")
plt.show()

