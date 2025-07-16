month = int(input("Enter month number (1-12): "))
if month == 12 or month == 1 or month == 2:
    print("Season: Winter")
elif month == 3 or month == 4 or month == 5:
    print("Season: Spring")
elif month == 6 or month == 7 or month == 8:
    print("Season: Summer")
elif month == 9 or month == 10 or month == 11:
    print("Season: Winter")
else:
    print("Invalid month number. Please enter a number between 1 and 12.")