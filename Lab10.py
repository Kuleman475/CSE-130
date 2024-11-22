# 1. Name:
#      -Taylor Christensen-
# 2. Assignment Name:
#      Lab 10: Number of Days
# 3. Assignment Description:
#      -count how many days are between two dates-
# 4. What was the hardest part? Be as specific as possible.
#      -the hardest part was figuring out how to count between december and january of the next year when they are close together dates.-
# 5. How long did it take for you to complete the assignment?
#      -3.5 hours


def is_leap_Year(startYear):
	if (startYear % 4 == 0 and startYear % 100 != 0) or (startYear % 400 == 0):
		return 29
	else:    return 28

totalDays = 0

startDay = 22
startMonth = 5
startYear = 1996

endDay = 21
endMonth = 11
endYear = 2024



# monthDays = {'January': 31, 'February': is_leap_Year(startYear), 'March': 31, 'April': 30, 'May': 31, 'June': 30, 'July': 31, 'August': 31, 'September': 30, 'October': 31, 'November': 30, 'December': 31}
monthDays = {1: 31, 2: is_leap_Year(startYear), 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
months = list(monthDays.keys())


y = 0
if startMonth == endMonth and endYear == startYear:
	totalDays = endDay - startDay
elif not isinstance(endYear, int):
	print("Please put a number")
elif startMonth < 1 or endMonth < 1 or startMonth > 12 or endMonth > 12:
	print("please put a correct month")
	totalDays = -5
elif startDay < 1 or endDay < 1 or startDay > monthDays[startMonth] or endDay > monthDays[endMonth]:
	print("please put a correct day")
	totalDays= -5
elif endYear < startYear:
	print("please put start date before end date")
	totalDays = -5
else:
	totalDays = monthDays[startMonth] - startDay 
	while startMonth != months[y]:
		y+=1

	y+=1
	if y == 12:
		y = 0
		startYear+=1
	while months[y] != endMonth or startYear != endYear:
		totalDays += monthDays[months[y]]
		# print(totalDays, monthDays[months[y]], months[y], startYear)
		y += 1
		if y == 12:
			y = 0
			startYear += 1
			monthDays['February'] = is_leap_Year(startYear)
	totalDays += endDay
if totalDays < 0:
	totalDays = "Error"
print(f"total number of days: {totalDays}")
