import json
import math

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
middle = 0

while(min != middle or max != middle):
    middle = (min + max) / 2  
    if ascii(data["array"][int(float(middle))]) == ascii("United States of America"):
        print("what your looking for is in the list")
        min = int(float(middle))
        max = int(float(middle))
    # elif math.isclose(min, max, abs_tol= 1):
    #     print("item not on the list")
    #     min = int(float(middle))
    #     max = int(float(middle))
    elif ascii(data["array"][int(float(middle))]) < ascii("United States of America"):
        min = int(float(middle)) + 1
        print("Greater half")
    elif ascii(data["array"][int(float(middle))]) > ascii("United States of America"):
        max = int(float(middle)) - 1
        print("lesser half")
    else:
        print("item not available")
        min = int(float(middle))
        max = int(float(middle))

# function binarySearch(list, target):
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

