'''
Count Salary Categories:
Table: Accounts
+-------------+------+
| Column Name | Type |
+-------------+------+
| account_id  | int  |
| income      | int  |
+-------------+------+
account_id is the primary key (column with unique values) for this table.
Each row contains information about the monthly income for one bank account.
Write a solution to calculate the number of bank accounts for each salary category. The salary categories are:

"Low Salary": All the salaries strictly less than $20000.
"Average Salary": All the salaries in the inclusive range [$20000, $50000].
"High Salary": All the salaries strictly greater than $50000.
The result table must contain all three categories. If there are no accounts in a category, return 0.

Return the result table in any order.
The result format is in the following example.

Example 1:
Input:
Accounts table:
+------------+--------+
| account_id | income |
+------------+--------+
| 3          | 108939 |
| 2          | 12747  |
| 8          | 87709  |
| 6          | 91796  |
+------------+--------+
Output:
+----------------+----------------+
| category       | accounts_count |
+----------------+----------------+
| Low Salary     | 1              |
| Average Salary | 0              |
| High Salary    | 3              |
+----------------+----------------+
Explanation:
Low Salary: Account 2.
Average Salary: No accounts.
High Salary: Accounts 3, 6, and 8.
'''

import pandas as pd

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    # Correct bin logic to match inclusive/exclusive boundaries as per problem
    accounts['category'] = pd.cut(
        accounts['income'],
        bins=[-float('inf'), 20000, 50001, float('inf')],
        labels=['Low Salary', 'Average Salary', 'High Salary'],
        right=False
    )

    # Count categories
    result = accounts['category'].value_counts().reset_index()
    result.columns = ['category', 'accounts_count']

    # Ensure all 3 categories are present
    all_categories = pd.DataFrame({
        'category': ['Low Salary', 'Average Salary', 'High Salary']
    })

    final = all_categories.merge(result, on='category', how='left').fillna(0)
    final['accounts_count'] = final['accounts_count'].astype(int)

    return final

data = {'account_id': [1, 2, 3, 4, 5], 'income': [15000, 22000, 50000, 51000, 18000]}
accounts = pd.DataFrame(data)

print(count_salary_categories(accounts))
