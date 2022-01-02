# The greeting program.
# Make a program that has your name and the current day of the week stored as separate variables and then prints a message like this:
#      “Good day <name>! <day> is a perfect day to learn some python.”
# Note that <name> and <day> are predefined variables in source code.
# An additional bonus will be to use different string formatting methods for constructing result string.

import datetime
my_name = "Viktor"
date_t = str(datetime.date.today())
year = int(date_t[0:4])
month = int(date_t[5:7])  #А якщо місяць або дата одноциферні?
date = int(date_t[8:10])
week_day = datetime.date(year, month, date).strftime("%A")
print(week_day)
print("Good day {0}! {1} is a perfect day to learn some python.".format(my_name, week_day))