def grade_of_a_student(marks):
        total = 0
        for n in marks:
            try:
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
            except Exception as e:
                print("Invalid value")
        return grade


import sys
print("Welcome to grade calculator")
name = input("enter your name: ")
marks = [50,'Hi',70,80,90,90]
grade=grade_of_a_student(marks)
print(name + " your grade is: " + grade)





print("Welcome to Bhuvana Bank")
print("Please proceed with below options to continue")
print("1. open checking account")
print("2. open savings account")
account = input(" select 1 or 2 : ")
print(int(account))
account = int(account)
charges_per_account = {1: 0.01, 2: 0.02}
if account == 1:
    try:
        print("opening checking account")
        a = int(input("please enter amount to deposit: "))
        print(a)
        b = input("select continue or exit: ")
        while b == "continue":
            a1 = int(input("please enter amount to deposit: "))
            b = input("select continue or exit: ")
            a=a+a1
            print(a)
        deposited_amount = a
        charges = deposited_amount * charges_per_account[account]
        final_amount = deposited_amount - charges
        print(str(final_amount) + " is deposited into your checking account")
    except Exception as e:
        print("Invalid Error")    #Just prints "Invalid Error" and stops becoz written try & except for outer logic
else:
    try:
        print("opening savings account")
        c = int(input("please enter amount to deposit: "))
        print(c)
        d = input("select continue or exit: ")
        while d == "continue":
            try:
                c1 = int(input("please enter amount to deposit: "))
                d = input("select continue or exit: ")
                c = c + c1
            except Exception as e:
                print("Invalid Value")     #prints "Invalid Error" and continues becoz written try & except for inner particular logic
            print(c)
        deposited_amount1 = c
        charges = deposited_amount1 * charges_per_account[account]
        final_amount1 = deposited_amount1 - charges
        print(str(final_amount1) + " is deposited into your savings account")
    except Exception as e:
        print("Invalid Error")
