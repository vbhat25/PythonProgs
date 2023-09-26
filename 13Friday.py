import datetime

def Friday13(month,year):
    try:
        date = datetime.date(year,month,13)
        if date.weekday() == 4:
            return f"The 13th of {datetime.date(year,month,1).strftime('%B')} {year} is a Friday."
        else:
            return False
    except:
        return False
    
month = int(input("Enter the number of the month: "))
year = int(input("Enter the year: "))

try1 = Friday13(month,year)

if try1:
    print(try1)
else:
    print("Not found in the month of this year")