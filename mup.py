import pandas as pd

# Creating a sample DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 35, 40],
        'Salary': [50000, 60000, 70000, 80000]}

df = pd.DataFrame(data)

# Basic manipulations
df['Age'] = df['Age'] + 1  # Incrementing age by 1
df['Bonus'] = df['Salary'] * 0.10  # Adding a new column
df_sorted = df.sort_values(by='Salary', ascending=False)  # Sorting by Salary

print(df_sorted)
