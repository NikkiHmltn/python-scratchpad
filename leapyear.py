# on every year that is evenly division by 4
    # except every eyar that is evenly divisible by 100
        # unless the year is also evenly divisible by 400 

year = int(input("What year do you want to check?\n"))

if year % 4 == 0:
    # leap year
    if year % 100 == 0 and year % 400 == 0: 
        print("Its a leap year!")
    elif year % 100 == 0:
        print("It's not a leap year.")
else: 
    print("Sorry, not a leap year.")