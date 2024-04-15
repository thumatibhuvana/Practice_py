inp = input("enter your input: ")
with open('text.txt', 'a') as af:
        af.write(inp)
        af.write("\n")
        print(af)


with open('text.txt', 'a') as af:
    student = {"name":"John","age":17,"grade":11.5,"subjects":["Math", "Science", "English"]}
    for key, value in student.items():
        a = f"student {key} : {value}"
        af.write(a)
        af.write("\n")
        print(af)
