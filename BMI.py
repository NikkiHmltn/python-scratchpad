height = float(input("Enter your height in meters:\n"))
weight = float(input("Enter your weight in kg:\n"))

BMI = round(weight / height, 2)

if BMI < 18.5: 
    print(f"Your BMI is {BMI} and you are underweight")
elif BMI > 18.5 and BMI < 25: 
    print(f"Your BMI is {BMI} and you are a normal weight")
elif BMI > 25 and BMI < 30: 
    print(f"Your BMI is {BMI} and you are overweight")
elif BMI > 30 and BMI < 35:
    print(f"Your BMI is {BMI} and you are obese")
else:
    print(f"Your BMI is {BMI} and you are clinically obese")