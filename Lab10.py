
def is_leap_Year(startYear):
	if (startYear % 4 == 0 and startYear % 100 != 0) or (startYear % 400 == 0):
		return 29
	else:    return 28

totalDays = 0
startDay = 21
startMonth = "October"
startYear = 1999

endDay = 4
endMonth = "March"
endYear = 2004

monthDays = {'January': 31, 'February': is_leap_Year(startYear), 'March': 31, 'April': 30, 'May': 31, 'June': 30, 'July': 31, 'August': 31, 'September': 30, 'October': 31, 'November': 30, 'December': 31}

months = list(monthDays.keys())

totalDays = monthDays[startMonth] - startDay 
y = 0
while startMonth != months[y]:
	y+=1

y+=1
print(months[y])
while months[y] != endMonth or startYear != endYear:
	totalDays += monthDays[months[y]]
	print(totalDays, monthDays[months[y]], months[y], startYear)
	y += 1
	if y == 12:
		y = 0
		startYear += 1
		monthDays['February'] = is_leap_Year(startYear)
totalDays += endDay
print(f"total number of days: {totalDays}")
