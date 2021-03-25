print("Welcome to the Love Calculator!")
name1 = input("What is your name?\n")
name2 = input("What is their name?\n")
t = 0 
r = 0
u = 0
e = 0
l = 0
o = 0
v = 0 
E = 0

first = name1.lower()
second = name2.lower()

t += first.count('t') + second.count('t')
r += first.count('r') + second.count('r')
u += first.count('u') + second.count('u')
e += first.count('e') + second.count('e')

first_num = t + r + u + e

l += first.count('l') + second.count('l')
o += first.count('o') + second.count('o')
v += first.count('v') + second.count('v')
E += first.count('e') + second.count('e')

second_num = l + o + v + E

print(f"Your compatibility is {first_num}{second_num}%")

