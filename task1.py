import datetime
my_name = "Viktor"
date_t = str(datetime.date.today())
year = int(date_t[0:4])
month = int(date_t[5:7])  #А якщо місяць або дата одноциферні?
date = int(date_t[8:10])
week_day = datetime.date(year, month, date).strftime("%A")
print(week_day)
print("Good day {0}! {1} is a perfect day to learn some python.".format(my_name, week_day))