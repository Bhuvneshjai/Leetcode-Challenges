'''
Students and Examinations: Table: Students
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| student_id    | int     |
| student_name  | varchar |
+---------------+---------+
student_id is the primary key (column with unique values) for this table.
Each row of this table contains the ID and the name of one student in the school.

Table: Subjects
+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| subject_name | varchar |
+--------------+---------+
subject_name is the primary key (column with unique values) for this table.
Each row of this table contains the name of one subject in the school.


Table: Examinations
+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| student_id   | int     |
| subject_name | varchar |
+--------------+---------+
There is no primary key (column with unique values) for this table. It may contain duplicates.
Each student from the Students table takes every course from the Subjects table.
Each row of this table indicates that a student with ID student_id attended the exam of subject_name.

Write a solution to find the number of times each student attended each exam.
Return the result table ordered by student_id and subject_name.
The result format is in the following example.

Example 1:
Input:
Students table:
+------------+--------------+
| student_id | student_name |
+------------+--------------+
| 1          | Alice        |
| 2          | Bob          |
| 13         | John         |
| 6          | Alex         |
+------------+--------------+
Subjects table:
+--------------+
| subject_name |
+--------------+
| Math         |
| Physics      |
| Programming  |
+--------------+
Examinations table:
+------------+--------------+
| student_id | subject_name |
+------------+--------------+
| 1          | Math         |
| 1          | Physics      |
| 1          | Programming  |
| 2          | Programming  |
| 1          | Physics      |
| 1          | Math         |
| 13         | Math         |
| 13         | Programming  |
| 13         | Physics      |
| 2          | Math         |
| 1          | Math         |
+------------+--------------+
Output:
+------------+--------------+--------------+----------------+
| student_id | student_name | subject_name | attended_exams |
+------------+--------------+--------------+----------------+
| 1          | Alice        | Math         | 3              |
| 1          | Alice        | Physics      | 2              |
| 1          | Alice        | Programming  | 1              |
| 2          | Bob          | Math         | 1              |
| 2          | Bob          | Physics      | 0              |
| 2          | Bob          | Programming  | 1              |
| 6          | Alex         | Math         | 0              |
| 6          | Alex         | Physics      | 0              |
| 6          | Alex         | Programming  | 0              |
| 13         | John         | Math         | 1              |
| 13         | John         | Physics      | 1              |
| 13         | John         | Programming  | 1              |
+------------+--------------+--------------+----------------+
Explanation:
The result table should contain all students and all subjects.
Alice attended the Math exam 3 times, the Physics exam 2 times, and the Programming exam 1 time.
Bob attended the Math exam 1 time, the Programming exam 1 time, and did not attend the Physics exam.
Alex did not attend any exams.
John attended the Math exam 1 time, the Physics exam 1 time, and the Programming exam 1 time.
'''

import pandas as pd

def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame,
                              examinations: pd.DataFrame) -> pd.DataFrame:
    # Step 1: Create Cartesian product
    students['key'] = 1
    print(students)
    print()

    subjects['key'] = 1
    print(subjects)
    print()

    all_combinations = pd.merge(students, subjects, on='key').drop(columns='key')
    print(all_combinations)
    print()

    # Step 2: Count exam attendance
    exam_counts = (
        examinations
        .groupby(['student_id', 'subject_name'])
        .size()
        .reset_index(name='attended_exams')  # ✅ Fixed here
    )
    print(exam_counts)
    print()

    # Step 3: Merge counts with full list
    result = pd.merge(
        all_combinations,
        exam_counts,
        on=['student_id', 'subject_name'],
        how='left'
    )
    print(result)
    print()

    # Step 4: Fill missing values and sort
    result['attended_exams'] = result['attended_exams'].fillna(0).astype(int)
    print(result)
    print()

    result = result[['student_id', 'student_name', 'subject_name', 'attended_exams']]
    result = result.sort_values(by=['student_id', 'subject_name']).reset_index(drop=True)

    return result

# Students table
students = pd.DataFrame({
    'student_id': [1, 2, 13, 6],
    'student_name': ['Alice', 'Bob', 'John', 'Alex']
})

# Subjects table
subjects = pd.DataFrame({
    'subject_name': ['Math', 'Physics', 'Programming']
})

# Examinations table
examinations = pd.DataFrame({
    'student_id': [1, 1, 1, 2, 1, 1, 13, 13, 13, 2, 1],
    'subject_name': ['Math', 'Physics', 'Programming', 'Programming', 'Physics', 'Math', 'Math', 'Programming',
                     'Physics', 'Math', 'Math']
})

result = students_and_examinations(students, subjects, examinations)
print(result)
