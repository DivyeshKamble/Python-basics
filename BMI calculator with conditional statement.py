#Calculate the BMI of user and use if else statement
#BMI = kg/m**2
w = float(input("Enter your weight in kg : "))
h = float(input("Enter the height in meters : "))
BMI = (w/(h**2))
print(BMI)

if BMI < 18.5:
    print("You are underweight. You need to gain weight.")
elif BMI >= 18.5 and BMI < 25:
    print("You are in the normal weight range. Keep it up!")
elif BMI >= 25:
    print("You are overweight. You need to lose weight.")
else:
    print("You are overweight or obese. You need to lose weight.")