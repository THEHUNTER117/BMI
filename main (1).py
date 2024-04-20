z=str(input("Please enter the unit of your heighT Which you will be entering later (meters=m,centimeters=cm,feet=f): "))
if (z=="f"):
    p=float(input("Please enter feet: "))
    q=float(input("Please enter inches: "))
    y=float(input("Please enter your wieght(in kg)(only numerical value): "))
    c=y/(((p*12)+q)/39)**2
    print("Your bmi is: ",c)
    if (c<18.5):
        print("You are under wieght! :(")
    elif (c<25):
        print("You are healthy :)")
    elif (c<30):
        print("You are over wieght! :(")
    elif (c>30):
        print("You are obese! :(((")
elif (z=="m"):
    x=float(input("Please enter your height(only numerical value): "))
    y=float(input("Please enter your wieght(in kg)(only numerical value): "))
    a=y/x**2
    print("Your bmi is: ",a)
    if (a<18.5):
        print("You are under wieght! :(")
    elif (a<25):
        print("You are healthy :)")
    elif (a<30):
        print("You are over wieght! :(")
    elif (a>30):
        print("You are obese! :(((")
elif (z=="cm"):
    x=float(input("Please enter your height(only numerical value): "))
    y=float(input("Please enter your wieght(in kg)(only numerical value): "))
    b=y/(x/100)**2
    print("Your bmi is: ",b)
    if (b<18.5):
        print("You are under wieght! :(")
    elif (b<25):
        print("You are healthy :)")
    elif (b<30):
        print("You are over wieght! :(")
    elif (b>30):
        print("You are obese! :(((")
else:
    print("You have to enter the unit. Now press run button and restart")


    
