import calendar
year = int(input("Enter year: "))
month_num = int(input("Enter month number (1-12): "))
date = int(input("Enter date: "))
if month_num >= 1 and month_num <= 12:
    print()
    print(calendar.month(year, month_num))
    if year%4==0:
        print("This is leap year")
    else:
        print("This is not a leap year")    
    if 1 <= date <= calendar.monthrange(year, month_num)[1]:
        # Find the weekday
        day_number = calendar.weekday(year, month_num, date)
        days = [
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
            "Sunday"
        ]
        print("The date is:", date, "-", month_num, "-", year)
        print("The day is:", days[day_number])
        
    else:
        print("Invalid date") 
       
        
else:
    print("Invalid")
    









 



































































































































































































































