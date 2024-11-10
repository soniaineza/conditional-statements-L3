weight = float(input("enter your weight "))
height = float(input("enter your height "))

BMI =weight/(height/100)**2

if BMI <=18.4:
    print("you are underweight")
elif BMI <=24.9:
    print("you are healthy")
elif BMI <=29.9:
    print("you are overweight")
else:
    print("you are obese")