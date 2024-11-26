import pandas as pd

# Read the CSV file
file_path = 'grades-template.csv'
df = pd.read_csv(file_path)

# Clean up the data by replacing missing values and handling invalid entries
df['PointsEarned'] = pd.to_numeric(df['PointsEarned'], errors='coerce').fillna(0)
df['PointsAvailable'] = pd.to_numeric(df['PointsAvailable'], errors='coerce').fillna(0)
print(df)

# Handle bonus adjustments
bonus_lab = df.loc[df['AssignmentName'] == 'Bonus Lab', 'PointsEarned'].values
final_project_bonus = df.loc[df['AssignmentName'] == 'Final Project Bonus', 'PointsEarned'].values

# Remove Bonus Lab and Final Project Bonus from the DataFrame to exclude them from calculations
df = df[~df['AssignmentName'].isin(['Bonus Lab', 'Final Project Bonus'])]

# Replace lowest Lab grade with Bonus Lab if valid
if bonus_lab.size > 0 and bonus_lab[0] > 0:
    lab_grades = df[df['Category'] == 'Lab']
    lowest_lab_index = lab_grades['PointsEarned'].idxmin()
    df.at[lowest_lab_index, 'PointsEarned'] = bonus_lab[0]

# Replace lowest HW grade with Final Project Bonus if valid
if final_project_bonus.size > 0 and final_project_bonus[0] > 0:
    hw_grades = df[df['Category'] == 'HW']
    lowest_hw_index = hw_grades['PointsEarned'].idxmin()
    df.at[lowest_hw_index, 'PointsEarned'] = final_project_bonus[0]

# Add a new column to calculate percentage for each row
df['Percentage'] = (df['PointsEarned'] / df['PointsAvailable']).replace([float('inf'), -float('inf')], 0)

# Group by Category and calculate the average percentage for each category
grouped_df = df.groupby('Category').agg({'Percentage': 'mean'}).reset_index()

# Define the weights for each category
weights = {
    'Lab': 0.40,
    'Quiz': 0.15,
    'HW': 0.15,
    'Midterm': 0.10,
    'Final': 0.20
}

# Calculate the weighted contribution of each category to the final grade
grouped_df['WeightedContribution'] = grouped_df['Category'].map(weights) * grouped_df['Percentage']

# Calculate the final grade as a percentage
final_grade = grouped_df['WeightedContribution'].sum() * 100

# Display the results
print("Grouped DataFrame with Averages:")
print(grouped_df)
print(f"\nFinal Grade: {final_grade:.2f}%")
