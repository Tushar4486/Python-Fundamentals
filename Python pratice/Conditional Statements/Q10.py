# Wap for college admission

marks = int(input("Enter your 12 Percentage here:"))

quota = input("Are you having any sports quota?(y/n):")

if marks>=70 and quota.lower()=="y":

    print("You can take admission")

else:

    print("Sorry, you are not eligible for admission")