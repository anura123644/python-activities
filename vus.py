import seaborn as sns
import matplotlib.pyplot as plt

# Sample dataset
tips = sns.load_dataset('tips')

# Creating a basic Seaborn visualization
sns.histplot(tips['total_bill'], bins=20, kde=True)

# Adding labels and title
plt.xlabel('Total Bill')
plt.ylabel('Frequency')
plt.title('Seaborn Histogram Example')

# Display the plot
plt.show()

