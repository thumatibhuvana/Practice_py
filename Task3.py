L1 = [1,5,7,9,10,40,36,23]
print("max value: " + str(max(L1)))
print("min value: " + str(min(L1)))
print("sum: " + str(sum(L1)))
L2 = []
for n in L1:
    if n%2==0:
        L2.append(n)
print(L2)

max=0
for n in L1:
    if n>max:
        max=n
print(max)

L1 = [1,5,7,9,10,40,36,23]
min=L1[0]
for n in L1:
    if n<min:
        min=n
print(min)

i=0
for n in L1:
   i = i+n
print(i)

L2 = [1,'a','b','c',2,3]
L3 = []
L4 = []
for n in L2:
    if type(n) == str:
        L3.append(n)
        # print("L3: ", L3)
    else:
        L4.append(n)
        # print("L4: ", L4)
print("L3: ", L3)
print("L4: ", L4)


