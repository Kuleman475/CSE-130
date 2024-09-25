#1. Name:
#      Taylor Christensen
# 2. Assignment Name:
#      Lab 02: Authentication
# 3. Assignment Description:
#      It is essentially a log in where the user puts in a username and password 
#      and if the username and password are in the same spot on the list it should 
#      tell you that you are authenticated.
# 4. What was the hardest part? Be as specific as possible.
#      The hardest part for me was having the python file read the json file.
#      once I was able to figure out how to read it then figuring out how to put 
#      it into a list was also a bit of a challenge.
#      After I was able to figure that out the assignment went pretty smoothly.
# 5. How long did it take for you to complete the assignment?
#      1.5 hours

import json

with open ("Lab02.json") as file:
    data = json.load(file)

username = []
password = []

for i in data['username']:  
    username.append(i)

for j in data ['password']:
    password.append(j)

inputUsername = input("username:  ")
inputPassword = input("password:  ")
count = 0

if inputUsername in username:
    for user in username:
        if inputUsername == user:
            if inputPassword == password[count]:
                print("You are authenticated!")
            else:
                print("You are not authorized to use the system.")
        count += 1
else:
    print("You are not authorized to use the system.")


