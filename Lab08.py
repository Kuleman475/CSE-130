import json

# 1. Name:
#      -Taylor Christensen-
# 2. Assignment Name:
#      Lab 08: Sort
# 3. Assignment Description:
#      -take an unsorted list and sort it-
# 4. What was the hardest part? Be as specific as possible.
#      -the hardest part for me was getting the list to be fully sorted. I could get it partially sorted but then not fully sorted or a couple of items were flip flopped.
#       for example the languages would be C C# python C++ and the rest was similarly organized. I was able to figure out how to get it fixed.-
# 5. How long did it take for you to complete the assignment?
#      -3 Hours


def sortList(data):
    max = len(data["array"])
    assert len(data["array"]) > 0, "List is empty"
    while 1 <= max:
        assert max > 0
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
    assert userInput == 5, "incorrect input please use correct input"

    file = open("Lab08.cities.json", "r")
    data = json.load(file)
    sortList(data)
    print("What is the name of the file? cities.json")


else:

    assert userInput > 5, "incorrect input please use correct input"
