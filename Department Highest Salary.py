'''
Department Highest Salary: Table: Employee
+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| id           | int     |
| name         | varchar |
| salary       | int     |
| departmentId | int     |
+--------------+---------+
id is the primary key (column with unique values) for this table.
departmentId is a foreign key (reference columns) of the ID from the Department table.
Each row of this table indicates the ID, name, and salary of an employee. It also contains the ID of their department.

Table: Department
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| name        | varchar |
+-------------+---------+
id is the primary key (column with unique values) for this table. It is guaranteed that department name is not NULL.
Each row of this table indicates the ID of a department and its name.

Write a solution to find employees who have the highest salary in each of the departments.
Return the result table in any order.
The result format is in the following example.

Example 1:
Input:
Employee table:
+----+-------+--------+--------------+
| id | name  | salary | departmentId |
+----+-------+--------+--------------+
| 1  | Joe   | 70000  | 1            |
| 2  | Jim   | 90000  | 1            |
| 3  | Henry | 80000  | 2            |
| 4  | Sam   | 60000  | 2            |
| 5  | Max   | 90000  | 1            |
+----+-------+--------+--------------+
Department table:
+----+-------+
| id | name  |
+----+-------+
| 1  | IT    |
| 2  | Sales |
+----+-------+
Output:
+------------+----------+--------+
| Department | Employee | Salary |
+------------+----------+--------+
| IT         | Jim      | 90000  |
| Sales      | Henry    | 80000  |
| IT         | Max      | 90000  |
+------------+----------+--------+
Explanation: Max and Jim both have the highest salary in the IT department and Henry has the highest salary in the
Sales department.
'''

import pandas as pd
def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    merged = employee.merge(department, left_on='departmentId', right_on='id', suffixes=('', '_dept'))
    print(merged)
    print()

    max_salary_per_dept = merged.groupby('departmentId')['salary'].transform('max')
    print(max_salary_per_dept)
    print()

    highest_paid = merged[merged['salary'] == max_salary_per_dept]
    print(highest_paid)
    print()

    result = highest_paid[['name_dept', 'name', 'salary']]
    result.columns = ['Department', 'Employee', 'Salary']

    print(result)
    print()

    return result

# Employee table
employee_data = {
    'id': [1, 2, 3, 4, 5],
    'name': ['Joe', 'Jim', 'Henry', 'Sam', 'Max'],
    'salary': [70000, 90000, 80000, 60000, 90000],
    'departmentId': [1, 1, 2, 2, 1]
}
employee = pd.DataFrame(employee_data)

# Department table
department_data = {
    'id': [1, 2],
    'name': ['IT', 'Sales']
}
department = pd.DataFrame(department_data)

# Test the function
result = department_highest_salary(employee, department)
print(result)