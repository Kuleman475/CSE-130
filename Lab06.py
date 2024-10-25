import json

userInput = int(input("which Json file would you like to open? \n 1. Countries \n 2. Empty \n 3. Language \n 4. Trivial \n 5. Quit \n"))

if userInput == 1:
    file = open("lab06.countries.json", "r")
elif userInput == 2:
    file = open("lab06.empty.json", "r")
elif userInput == 3:
    file = open("lab06.languages.json", "r")
elif userInput == 4:
    file = open("lab06.trivial.json", "r")
elif userInput == 5:
    exit()
else:
    print("incorrect input please use correct input")


data = json.load(file)
max = len(data["array"])
min = 0


while(min != max):

    middle = (min + max) / 2  
    if ascii(data["array"][middle]) == ascii("Python"):
        print("what your looking for is in the list")
    elif ascii(data["array"][middle]) < ascii("Python"):
        min = middle + 1
    else:
        max = middle - 1


#         unction binarySearch(list, target):
# start = 0
# end = length(list) - 1
# while start <= end:
# mid = (start + end) // 2
# if list[mid] == target:
# return mid
# else if list[mid] < target:
# start = mid + 1
# else:
# end = mid - 1
# return -1 # target not in list
# COMPARE AND CONTRAST
# ▪ Provide an analysis as to the pros and cons of the two solutions?

