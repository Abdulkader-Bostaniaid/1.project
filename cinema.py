selection = input("press (1) for cinema , press (2) for theater : ")
student = input("are you a student? (Y/N) :")
fee = 0

if selection == "1" :
     fee = 15

elif selection == "2" :
     fee = 10

#for student

if student == "Y" or student == "y":
    fee = fee / 2     #%50
    print("you have to pay :{}".format(fee))

elif student == "N" or student == "n":
    print("you have to pay :{}".format(fee))