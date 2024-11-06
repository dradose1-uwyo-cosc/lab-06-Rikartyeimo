# Your Name Here : Rikart Yeimo
# UWYO COSC 1010
# Submission Date: 11/5/2024
# Lab Section: Homework 3
# Sources, people worked with, help given to: Brian Montiel
# your
# comments
# here
def leap_year (year):
    if year % 4 == 0 :
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
def january_first_day(year):
    y = year - 1
    day = (36 + y + (y // 4) - (y // 100) + (y // 400)) % 7
    return  day
def valid_date(month, day, year):
    if month < 1 or month > 12:
        return False
    if day < 1:
        return False
    if month in [4, 6, 9, 11] and day > 30:
        return False
    if month in [1, 3, 5, 7, 8, 10, 12] and day > 31:
        return False
    if month == 2:
        if leap_year(year) and day > 29:
            return False
        elif not leap_year(year) and day > 28:
            return False
    return True

def day_of_week(month, day, year):
    if not day_of_week(month, day, year):
        return "Invalid Date"
    days_in_month = [31, 28 + leap_year(year), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day_of_week = ["Sunday", "Monday", "Tuesday","Wednesday","Thursday","Friday","Saturday"] 

    january_first = january_first_day(year)
    total_days = sum(days_in_month[:month - 1]) + day - 1
    day_of_week = (january_first + total_days) % 7
    return day_of_week[day_of_week]   
def main():
    input_date = input ("Enter date (MM/DD/YYY):")
    try:
        month, day, year = map(int, input_date.split('/'))
        result = day_of_week(month, day, year)
        print(f"{input_date} {result}")
    except ValueError:
        print("Invalid Date")
if __name__ == "__main__":
    main()

