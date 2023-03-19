# Code adapted from

from datetime import date

# get today's date
today = date.today()

# Get day, month and year as individual strings
day = today.strftime("%d")
month = today.strftime("%m")
year = today.strftime("%Y")

heading = "the current date is {}/{}/{}".format(day, month, year)
filename = "MFF_{}_{}_{}".format(year, month, day)

# Heading
print(heading)
print("The filename will be P{.txt".format(filename))

