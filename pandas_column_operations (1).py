import pandas as pd

data = {
    'Employee': ['Ravi', 'Priya', 'Amit'],
    'Department': ['IT', 'HR', 'Finance'],
    'Salary': [50000, 60000, 55000]
}

df = pd.DataFrame(data)

df_dropped = df.drop('Salary', axis=1)

print(df_dropped)