from datetime import date , time ,datetime
# calling the today
# function of date class
today = date. today()
now = datetime.now()
print("Today's date is", today)
print("\nCurrent Date and time is ", now)
#Printing dates components
print("\n date components",today.year,today.month,today.day)
