print("Welcome to Bhuvana Bank")
print("Please proceed with below options to continue")
print("1. open checking account")
print("2. open savings account")
account = input(" select 1 or 2 : ")
print(int(account))
account = int(account)
charges_per_account = {1: 0.01, 2: 0.02}
if account == 1:
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
else:
    print("opening savings account")
    c = int(input("please enter amount to deposit: "))
    print(c)
    d = input("select continue or exit: ")
    while d == "continue":
        c1 = int(input("please enter amount to deposit: "))
        d = input("select continue or exit: ")
        c = c + c1
        print(c)
    deposited_amount1 = c
    charges = deposited_amount1 * charges_per_account[account]
    final_amount1 = deposited_amount1 - charges
    print(str(final_amount1) + " is deposited into your savings account")

