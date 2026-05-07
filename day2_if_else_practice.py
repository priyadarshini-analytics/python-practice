# Q.1 Largest of three numbers

a = 5
b = 9
c = 2
if a > b and a > c:
    print("a is greater")
elif b > c and b > a:
    print("b is greater")
else:
    print("c is greater")

# Q.2 Leap year checker
year = int(input("Enter a year: "))
if year % 4 == 0 or year % 400 == 0 and year % 100 != 0:
     print("leap year")
else:
    print("not a leap year")


# Q.3 Electricity bill
unit = int(input("Enter your unit: "))
if unit < 100:
    bill = unit * 5
elif unit < 200:
    bill = unit * 7
else:
    bill = unit * 10
print("final bill:",bill)


# Q4 password strength checker
password = input("Enetr your password:")
if len(password) < 6:
    print("weak")
elif "@" in password or "#" in password:
    print("strong")
else:
    print("medium")


# Q5 triagle checker
a = int(input("Enter your first side:"))
b = int(input("Enter your second side:"))
c = int(input("Enter your third side:"))
if a == b and b == c:
    print("Equilateral")
elif a == b or b == c or a == c:
    print("ispsceles")
else:
    print("scalene")


# Q6 ATM Machine logic
amount = int(input("Enetr your widrawal amount:"))
balance = 10000
if amount > balance:
    print("insufficient balance")
elif amount % 100 != 0:
    print("invalid amount")
else:
    print("transaction successful")

# Q.7 Discount calculator
amount = int(input("Enter your shopping amount"))
if amount > 5000:
    discount = 5000 * 20 / 100
    final_amount = discount - amount
elif amount > 3000:
     discount = 3000 * 10 / 100
     final_amount = discount - amount 
else:
    print("no discount")
    final_amout = amount
print("Your final amount is:",final_amount)


# Q.8 Login system
user_name = input("Enter your username:")
password = input("Enter your pasword:")
if user_name == "admin" and password == "python123":
    print("Login successful")
elif user_name != "admin" :
     print("wrong username")
else:
    print("wrong password")

