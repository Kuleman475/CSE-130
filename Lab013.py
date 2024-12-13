# 1. Name:
#      Taylor Christensen
# 2. Assignment Name:
#      Lab 13: Power
# 3. Assignment Description:
#      find the best average over a certain number in an array
# 4. What was the hardest part? Be as specific as possible.
#      The hardest part for me was figuring out the asserts to put in and how to use them correctly
# 5. How long did it take for you to complete the assignment?
#      2.5 hours

import json

UserInput = input("Pick a List \n 1. Banana.txt \n 2. Small.json \n 3. Large.json \n")
assert UserInput in ["1", "2", "3"], "Input needs to be 1, 2, or 3 :)"
Subset = int(input("Pick a subset number: "))
assert Subset is not int

match UserInput:
    case "1":
        print("incorrect type of file\n Goodbye!")
        exit()
    case "2":
        file = open('Lab13.small.json', 'r')
        ListJson = json.load(file)
    case "3":
        file = open('Lab13.large.json', 'r')
        ListJson = json.load(file)  

List = ListJson["array"]
assert Subset <= len(List), f"for list {UserInput} it needs to be less than or equal to {len(List)}"
Start = 0 
End = Subset
averageList = []
averageStart = []


while End <= len(List):
    Total = 0
    Current = Start
    while Current != End:
        Total +=List[Current]
        Current += 1
    averageList.append(Total / Subset)
    
    Start += 1
    End += 1
maxAverage = max(averageList)
maxStart = averageList.index(maxAverage)
print(List[maxStart: maxStart + Subset])
print(f" the largest average is {max(averageList)}")