"""Task 1: Code a function to calculate the average grade.
Task 2: Implement a function to find the highest and lowest grade.
Task 3: Create a feature that categorizes grades into letter grades (A, B, C, etc.)."""


# List of Grades
list_of_grades = [57, 98, 88, 45, 95, 100, 78, 80, 90, 45]


# Task 1
def average_grade(list):
    total = sum(list)
    return total / len(list)


# Task 2
def highest_and_lowest(list):
    highest = max(list)
    lowest = min(list)
    return f' Highest Grade: {highest}\n Lowest Grade: {lowest}'


# Task 3
def grade_category(grade):
    if grade <= 100 and grade >= 90:
        return 'Your Grade is an: A'
    elif grade <= 89 and grade >= 79:
        return 'Your Grade is a: B'
    elif grade <= 78 and grade >= 68:
        return 'Your Grade is a: C'
    elif grade <= 67 and grade >= 60:
        return 'Your Grade is a: D'
    else:
        return 'Your Grade is an: F'
    
print(average_grade(list_of_grades))
print(highest_and_lowest(list_of_grades))
print(grade_category(average_grade(list_of_grades)))