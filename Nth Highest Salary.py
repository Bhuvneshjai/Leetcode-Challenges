'''
Nth Highest Salary: Table: Employee
+-------------+------+
| Column Name | Type |
+-------------+------+
| id          | int  |
| salary      | int  |
+-------------+------+
id is the primary key (column with unique values) for this table.
Each row of this table contains information about the salary of an employee.

Write a solution to find the nth highest distinct salary from the Employee table. If there are less than n distinct salaries,
return null.

The result format is in the following example.

Example 1:
Input:
Employee table:
+----+--------+
| id | salary |
+----+--------+
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |
+----+--------+
n = 2
Output:
+------------------------+
| getNthHighestSalary(2) |
+------------------------+
| 200                    |
+------------------------+

Example 2:
Input:
Employee table:
+----+--------+
| id | salary |
+----+--------+
| 1  | 100    |
+----+--------+
n = 2
Output:
+------------------------+
| getNthHighestSalary(2) |
+------------------------+
| null                   |
+------------------------+
'''

import pandas as pd


def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    # Get distinct salaries in descending order
    unique_salaries = employee['salary'].drop_duplicates().sort_values(ascending=False).reset_index(drop=True)

    # Validate N
    if N <= 0 or N > len(unique_salaries):
        nth_salary = None
    else:
        nth_salary = unique_salaries.iloc[N - 1]

    # Return result in the expected format
    return pd.DataFrame({f'getNthHighestSalary({N})': [nth_salary]})


data = {
        'id': [1, 2, 3],
        'salary': [100, 200, 300]
    }
df = pd.DataFrame(data)
print(nth_highest_salary(df, 2))
