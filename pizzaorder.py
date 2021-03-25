print("Welcome to Python Pizza!")
size = input("What size pizza do you want? S, M, or L\n")
add_pepperoni = input("Do you want pepperoni? Y or N\n")
extra_cheese = input("Do you want extra cheese? Y or N\n")
bill = 0

#small pizza: 15
#med pizza: 20
#large pizza: 25

# pepperoni for small: 2
# peperoni for med/large: 3

#extra cheese for any pizza: 1

if size == 'S':
    bill += 15
    if add_pepperoni == 'Y':
        bill += 2
        if extra_cheese == 'Y':
            bill += 1
            print(f"Your total is: {bill}")
        else: 
            print(f"Your total is: {bill}")
    else:
        if extra_cheese == 'Y':
            bill += 1
            print(f"Your total is: {bill}")
        else: 
            print(f"Your total is: {bill}")
        
elif size == 'M':
    bill += 20
    if add_pepperoni == 'Y':
        bill += 3
        if extra_cheese == 'Y':
            bill += 1
            print(f"Your total is: {bill}")
        else: 
            print(f"Your total is: {bill}")
    else:
        if extra_cheese == 'Y':
            bill += 1
            print(f"Your total is: {bill}")
        else: 
            print(f"Your total is: {bill}")
else: 
    bill += 25
    if add_pepperoni == 'Y':
        bill += 3
        if extra_cheese == 'Y':
            bill += 1
            print(f"Your total is: {bill}")
        else: 
            print(f"Your total is: {bill}")
    else:
        if extra_cheese == 'Y':
            bill += 1
            print(f"Your total is: {bill}")
        else: 
            print(f"Your total is: {bill}")
    