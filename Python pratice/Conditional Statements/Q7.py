# Wap to withdraw amount from the account in atm

a = int(input("Enter amount to be withdraw: "))
b = 10000 # Balance leliya itna

if a<=b:
    print("Withdrawal Successful")
    print("Remaining Balance:",b-a)
else:
    print("Insufficient Balance")
