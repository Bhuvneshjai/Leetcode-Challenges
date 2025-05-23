'''
Number of Unique Subjects Taught by Each Teacher: Table: Teacher
+-------------+------+
| Column Name | Type |
+-------------+------+
| teacher_id  | int  |
| subject_id  | int  |
| dept_id     | int  |
+-------------+------+
(subject_id, dept_id) is the primary key (combinations of columns with unique values) of this table.
Each row in this table indicates that the teacher with teacher_id teaches the subject subject_id in the department dept_id.

Write a solution to calculate the number of unique subjects each teacher teaches in the university.
Return the result table in any order.
The result format is shown in the following example.

Example 1:
Input:
Teacher table:
+------------+------------+---------+
| teacher_id | subject_id | dept_id |
+------------+------------+---------+
| 1          | 2          | 3       |
| 1          | 2          | 4       |
| 1          | 3          | 3       |
| 2          | 1          | 1       |
| 2          | 2          | 1       |
| 2          | 3          | 1       |
| 2          | 4          | 1       |
+------------+------------+---------+
Output:
+------------+-----+
| teacher_id | cnt |
+------------+-----+
| 1          | 2   |
| 2          | 4   |
+------------+-----+
Explanation:
Teacher 1:
  - They teach subject 2 in departments 3 and 4.
  - They teach subject 3 in department 3.
Teacher 2:
  - They teach subject 1 in department 1.
  - They teach subject 2 in department 1.
  - They teach subject 3 in department 1.
  - They teach subject 4 in department 1.
'''

import pandas as pd
def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:
    result = (
        teacher
        .drop_duplicates(subset=['teacher_id', 'subject_id'])
        .groupby('teacher_id')['subject_id']
        .nunique()
        .reset_index(name='cnt')
    )
    r1 = teacher.drop_duplicates(subset=['teacher_id','subject_id'])
    print(r1)
    print()

    r2 = r1.groupby('teacher_id')['subject_id']
    print(r2)
    print()

    r3 = r2.nunique()
    print(r3)
    print()

    r4 = r3.reset_index(name='cnt')
    print(r4)
    print()

    return result

import pandas as pd

# Sample data
data = {
    'teacher_id': [1, 1, 1, 2, 2, 2, 2],
    'subject_id': [2, 2, 3, 1, 2, 3, 4],
    'dept_id':    [3, 4, 3, 1, 1, 1, 1]
}

# Create DataFrame
teacher = pd.DataFrame(data)

# Use the function
result = count_unique_subjects(teacher)
print(result)
