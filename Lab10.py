
def is_leap_Year(startYear):
	if (startYear % 4 == 0 and startYear % 100 != 0) or (startYear % 400 == 0):
		return 29
	else:    return 28

totalDays = 0
startDay = 22
startMonth = "May"
startYear = 2020
endDay = 25
endMonth = "December"
endYear = 2024

monthDays = {'January': 31, 'February': is_leap_Year(startYear), 'March': 31, 'April': 30, 'May': 31, 'June': 30, 'July': 31, 'August': 31, 'September': 30, 'October': 31, 'November': 30, 'December': 31}

list(monthDays)


x = monthDays.keys()
totalDays = startDay - monthDays[startMonth]
while (startYear != endYear & startMonth != endMonth & startDay != endDay):
	totalDays += list(monthDays[startMonth])[x]
	x += 1
	if x > 12:
		x = 1
print(f"total number of days: {totalDays}")
