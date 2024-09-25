from datetime import datetime

name = input("What is your name? ")
print(f"Hello {name}")
currentYear = datetime.now().year
birthYear = int(input("What year were you born? "))
yourAge = currentYear - birthYear
print(f"your age is {yourAge}")