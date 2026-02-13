# Wap to check driving license eligibility 

age = int(input("Enter your age here:"))
citizen = input("Are you Indian? (y/n):")


if age>=18 and citizen.lower()=="y":

    print("Yes , you are eligible")

else:

    print("No , you are not eligible")
