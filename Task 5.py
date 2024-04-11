'''def hello_function(greeting):
    return greeting


print(hello_function('Hello'))


def hello_function(greeting):
    return greeting,"Mrs.Hanu."


print(hello_function('Hello'))



def hello_function(greeting):
    return "{} Mrs.Hanu."


print(hello_function('Hi'))


def hello_function(greeting):
    return "{} Mrs.Hanu.".format(greeting)


print(hello_function('Hi'))


def hello_function(greeting):
    pass  #If i dont want any exception then we need to place pass so that it will return none


print(hello_function('Hello'))


def details(*name, **age):
    return "{},{}".format(name, age)


print(details('Bhuvan', 20, name="Hanu", age=25))'''


def action(x,y,z):
    if z == "add":
        z = x+y
    elif z == "sub":
        z = x-y
    elif z == "mul":
        z = x*y
    elif z == "div":
        z = x/y
    return z


result = action(4,2, "div")
print(result)


def s(l):
    result = 0
    for n in l:
        result = result+int(n)
    return result

l = [1,2,10,4,5]
result = s(l)
print(result)


def decision(n):
    if n%2 == 0:
        z = "even"
    else:
        z = "odd"
    return z


z = decision(16)
print(z)



def grade_of_a_student(marks):
    total = 0
    for n in marks:
        total = total + n
    print("your total = " + str(total) + "/" + str(600))

    perc = (total/600)*100
    print(perc)
    if 90 <= perc <= 100:
        grade = "A"
    elif 80 <= perc < 90:
        grade = "B"
    elif 70 <= perc < 80:
        grade = "C"
    elif perc >= 60 and perc < 70:
        grade = "D"
    elif perc >= 50 and perc < 60:
        grade = "E"
    else:
        grade = "Fail"
    return grade

import sys
print("Welcome to grade calculator")
name = input("enter your name: ")
marks = [50,60,70,80,90,90]
grade=grade_of_a_student(marks)
print(name + " your grade is: " + grade)


