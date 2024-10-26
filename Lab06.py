import json
import math

# 1. Name:
#      -Taylor Christensen-
# 2. Assignment Name:
#      Lab 06: Advanced Search
# 3. Assignment Description:
#      -The program is supposed to efficiently search through a list and find the item in the list without looking at each and every item in the list-
# 4. Algorithmic Efficiency
#      -O(log n) because it is only looking at 1 item on the list and seeing if it needs to go up or down on the list -
# 5. What was the hardest part? Be as specific as possible.
#      -The hardest part for me was getting the program to find the item if it was in the big list and it find the item. -
# 6. How long did it take for you to complete the assignment?
#      -3 hours

for i in range(7):
    userInput = int(input("which Json file would you like to open? \n 1. Empty \n 2. Trivial \n 3. Language \n 4. Countries \n 5. Quit \n"))
    print()
    if userInput == 1:
        file = open("Lab06.empty.json", "r")
        print("What is the name of the file? empty.json")

    elif userInput == 2:
        file = open("Lab06.trivial.json", "r")
        print("What is the name of the file? trivial.json")

    elif userInput == 3:
        file = open("Lab06.languages.json", "r")
        print("What is the name of the file? languages.json")

    elif userInput == 4:
        file = open("Lab06.countries.json", "r")
        print("What is the name of the file? countries.json")

    elif userInput == 5:
        exit()

    else:
        print("incorrect input please use correct input")


    data = json.load(file)
    max = len(data["array"])
    min = 0
    middle = 0
    findInFile = input("What name are we looking for? ")
    result = ""

    if max == min:
        result = "item not found"
    while(min != middle or max != middle or min != max):

        middle = (min + max) / 2  

        if ascii(data["array"][int(float(middle))]) == ascii(findInFile):
            result = "what your looking for is in the list"
            min = int(float(middle))
            max = int(float(middle))

        elif math.isclose(min, max, abs_tol= 1):
            result = "item not on the list"
            min = int(float(middle))
            max = int(float(middle))


        elif ascii(data["array"][int(float(middle))]) < ascii(findInFile):
            min = int(float(middle))

        elif ascii(data["array"][int(float(middle))]) > ascii(findInFile):
            max = int(float(middle))

    print(result)
    print()
    i+=1