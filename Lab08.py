import json


def sortList(data):
    max = len(data["array"])
    assert (max > 0, "List is empty")
    while 1 <= max:
        assert max <= 0
        for t in range(max):
            select = t
            for j in range(max):
                if ascii(data["array"][j]) > ascii(data["array"][select]):
                    select = j
            data["array"][select], data["array"][t] = data["array"][t], data["array"][select]
        max -= 1

    for i in range(len(data["array"])):
        print(data["array"][i])


userInput = int(input("which Json file would you like to open? \n 1. Empty \n 2. Trivial \n 3. Language \n 4. States \n 5. Cities \n 6. Quit \n"))
print()
if userInput == 1:
    file = open("Lab08.empty.json", "r")
    data = json.load(file)
    sortList(data)  
    print("What is the name of the file? empty.json")

elif userInput == 2:
    file = open("Lab08.trivial.json", "r")
    data = json.load(file) 
    sortList(data)  
    print("What is the name of the file? trivial.json")

elif userInput == 3:
    file = open("Lab08.languages.json", "r")
    data = json.load(file)
    sortList(data)
    print("What is the name of the file? languages.json")

elif userInput == 4:
    file = open("Lab08.states.json", "r")
    data = json.load(file)
    sortList(data)
    print("What is the name of the file? states.json")

elif userInput == 5:
    file = open("Lab08.cities.json", "r")
    data = json.load(file)
    sortList(data)
    print("What is the name of the file? cities.json")


else:
    assert (userInput > 5, "incorrect input please use correct input")

