phone = 1234
mapping = {1: "one", 2: "two", 3: "three", 4: "four"}
for num in str(phone):    #converting phone to string becoz we can iterate only strings, lists,... but not integers, float,& boolean.
    print(mapping[int(num)])

msg = input("enter your message: ")
words = msg.split(' ')
print(words)
out = ""
emojis = {":)": "😊", ":(": "😡😭💔", "$": "💲"}
for word in words:
    if word in emojis:
        out = out+emojis[word]+" "
    else:
        out = out+word+" "
print(out)

L = [-10, 5, 20, -1, 53, 60, 61]
out = 0
for n in L:
    out = out + n
out = out/len(L)
print(out)

cost = {'apple': 2, 'banana': 3, 'berry': 5, 'avocado': 10}
my_purchase = ['apple', 'apple', 'banana', 'berry', 'berry', 'avocado', 'avocado', 'berry', 'coconut']
price = 0
for item in my_purchase:
    if item in cost:
        price = price + cost[item]
    else:
        print(f"cost not found for: {item}")
print("Total purchase of mine: " +str(price))
print(f"Total purchase of mine: {price}")

x = 'Hello BHUVANA, How Are YoU?'
count = 0
for letter in x:
    if letter.isupper():
        count = count + 1
print(count)

L1 =[10, 5, 1, 3, 2, 8]
even_count = 0
odd_count = 0
for n in L1:
    if n%2 == 0:
        even_count = even_count + 1
    if n%2 != 0:
        odd_count = odd_count +1
print(f'count of even: {even_count}')
print(f'count of odd: {odd_count}')


# Emoji conversion pgm using Functions
msg = input("enter your message: ")
words = msg.split(' ')
print(words)
out = ""
emojis = {":)": "😊", ":(": "😡😭💔", "$": "💲"}
for word in words:
    if word in emojis:
        out = out+emojis[word]+" "
    else:
        out = out+word+" "
print(out)

def message(msg):
    words = msg.split(' ')
    print(words)
    out = ""
    emojis = {":)": "😊", ":(": "😡😭💔", "$": "💲"}
    for word in words:
        if word in emojis:
            out = out + emojis[word] + " "
        else:
            out = out + word + " "
    return out

m = input("enter your message: ")
result = message(m)
print(result)






