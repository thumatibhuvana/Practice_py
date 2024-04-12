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

