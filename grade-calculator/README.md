# Calcculate Your grade

You can use this Python script to estimate your grade for the semester (out of 100%)

1. Enter your grades into each assignment record in the `example_grades.csv` file
2. Make sure you include any bonus values you got from the bonus lab, or the final project, these are optional though
3. run the script `python3 grade_calc.py`

## Exaxmple Output
```sh
1                  Week 1            HW          10.0               10
2          Week 2 Homework           HW          10.0               10
3   HW3 (Week 3 Homeowrk)            HW           9.5               10
4                     HW4            HW          10.0               10
5                     HW5            HW           8.0               10
6                     HW6            HW          10.0               10
7                     HW7            HW           0.0               10
8                     HW8            HW           3.0               10
9                     HW9            HW           8.0               10
10                    HW10           HW          10.0               10
11                  Lab 1           Lab          20.0               25
12                  Lab 2           Lab          17.5               25
13                  Lab 4           Lab          20.0               25
14                  Lab 5           Lab          25.0               25
15                  Lab 6           Lab          20.0               25
16                   Lab3           Lab          22.5               25
17     The Midterm Project      Midterm          80.0              100
18                  Quiz 1         Quiz          20.0               20
19                  Quiz 2         Quiz          14.0               20
20                  Quiz 3         Quiz          15.0               20
21               Bonus Lab  Lab-replace          25.0               25
22     Final Project Bonus   HW-replace           0.0               10
Grouped DataFrame with Averages:
  Category  Percentage  WeightedContribution
0    Final    0.875000              0.175000
1       HW    0.785000              0.117750
2      Lab    0.883333              0.353333
3  Midterm    0.800000              0.080000
4     Quiz    0.816667              0.122500

Final Grade: 84.86%
```
