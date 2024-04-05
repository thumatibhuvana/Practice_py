import sys
print("Welcome to grade calculator")
name = input("enter your name: ")
tel_marks = int(input("enter telugu marks: "))
hin_marks = int(input("enter hindi marks: "))
eng_marks = int(input("enter english marks: "))
math_marks = int(input("enter maths marks: "))
sci_marks = int(input("enter science marks: "))
soc_marks = int(input("enter social marks: "))
if tel_marks < 0 or tel_marks > 100 :
    print("Invalid values")
    sys.exit()
if hin_marks < 0 or hin_marks > 100 :
    print("Invalid values")
    sys.exit()
if eng_marks < 0 or eng_marks > 100 :
    print("Invalid values")
    sys.exit()
if math_marks < 0 or math_marks > 100 :
    print("Invalid values")
    sys.exit()
if sci_marks < 0 or sci_marks > 100 :
    print("Invalid values")
    sys.exit()
if soc_marks < 0 or soc_marks > 100 :
    print("Invalid values")
    sys.exit()

total = tel_marks + hin_marks + eng_marks + math_marks + sci_marks + soc_marks

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

print(name + " your grade is: " + grade)

