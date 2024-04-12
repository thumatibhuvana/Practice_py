from list_operations import filter_numbers

lst = [1,2,3,4,5,6]
l = filter_numbers(lst, threshold = 6)
print(l)


from calculator import action

result = action(4,2, "add")
print(result)


from grade_calculator import grade_of_a_student

import sys
print("Welcome to grade calculator")
name = input("enter your name: ")
marks = [90,90,70,80,90,90]
grade=grade_of_a_student(marks)
print(name + " your grade is: " + grade)

