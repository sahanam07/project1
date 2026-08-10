import pandas as pd
import numpy as np


data = {
    "Employee_ID": [101, 102, 103, 104, 105, 106],
    "Name": ["Rahul", "Priya", "Amit", "Sneha", "Kiran", "Anita"],
    "Department": ["IT", "HR", "IT", "Finance", "HR", "Finance"],
    "Age": [25, 28, 30, 26, 32, 29],
    "Salary": [40000, np.nan, 50000, 45000, np.nan, 55000]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)


print("\nMissing values in each column:")
print(df.isnull().sum())


df["Salary"] = df["Salary"].fillna(
    df.groupby("Department")["Salary"].transform("median")
)

print("\nDataFrame after filling missing salaries:")
print(df)


df["Annual_Bonus"] = df["Salary"] * 0.10

print("\nDataFrame with Annual Bonus:")
print(df)

avg_salary = df.groupby("Department")["Salary"].mean()

print("\nAverage Salary by Department:")
print(avg_salary)