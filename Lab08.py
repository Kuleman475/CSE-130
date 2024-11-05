import json

userInput = int(input("which Json file would you like to open? \n 1. Empty \n 2. Trivial \n 3. Language \n 4. States \n 5. Cities \n 6. Quit \n"))
print()
if userInput == 1:
    file = open("Lab08.empty.json", "r")
    data = json.load(file)
    max = len(data["array"])
    for i in range(max):
        print(data["array"][i])
    print("What is the name of the file? empty.json")

elif userInput == 2:
    file = open("Lab08.trivial.json", "r")
    data = json.load(file)
    max = len(data["array"])
    for i in range(max):
        print(data["array"][i])
    
    print("What is the name of the file? trivial.json")

elif userInput == 3:
    file = open("Lab08.languages.json", "r")
    data = json.load(file)
    max = len(data["array"])
    # SWITCH THINGS IN THE ARRAY JSON
    data["array"][6], data["array"][0] = data["array"][0], data["array"][6]
    for i in range(max):
        print(data["array"][i])
    print("What is the name of the file? languages.json")

elif userInput == 4:
    file = open("Lab08.states.json", "r")
    data = json.load(file)
    max = len(data["array"])
    for i in range(max):
        print(data["array"][i])
    print("What is the name of the file? states.json")

elif userInput == 5:
    file = open("Lab08.cities.json", "r")
    data = json.load(file)
    max = len(data["array"])
    for i in range(max):
        print(data["array"][i])
    print("What is the name of the file? cities.json")


else:
    print("incorrect input please use correct input")
