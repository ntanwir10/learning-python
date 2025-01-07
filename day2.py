# commision calculator in python

name = input("Enter your name: ")
sales = int(input("Enter your sales: "))

commission =round(sales * 13 / 100, 2) 

print(f"hello {name}, your commission is ${commission}")