'''
Second Highest Salary: Table: Employee
+-------------+------+
| Column Name | Type |
+-------------+------+
| id          | int  |
| salary      | int  |
+-------------+------+
id is the primary key (column with unique values) for this table.
Each row of this table contains information about the salary of an employee.

Write a solution to find the second highest distinct salary from the Employee table. If there is no second highest salary,
return null (return None in Pandas).

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
Output:
+---------------------+
| SecondHighestSalary |
+---------------------+
| 200                 |
+---------------------+

Example 2:
Input:
Employee table:
+----+--------+
| id | salary |
+----+--------+
| 1  | 100    |
+----+--------+
Output:
+---------------------+
| SecondHighestSalary |
+---------------------+
| null                |
+---------------------+
'''

import pandas as pd
def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    salaries = employee['salary'].drop_duplicates().sort_values(ascending=False).reset_index(drop=True)
    if len(salaries) < 2:
        second_highest = None
    else:
        second_highest = salaries.iloc[1]
    return pd.DataFrame({'SecondHighestSalary':[second_highest]})

data = {
    'id': [1, 2, 3],
    'salary': [100, 200, 300]
}
employee = pd.DataFrame(data)
print(second_highest_salary(employee))
