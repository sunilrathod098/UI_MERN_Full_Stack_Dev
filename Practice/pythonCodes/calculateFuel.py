# You are writing a program to calculate fuel efficiency in two formats:
# Liters per 100 kilometers (used in Europe)
# Miles per gallon (used in the US)



liters = float(input("Enter the no of liters to fill the tank\n"))
if liters <= 0:
    print(f"{int(liters)} is a Invalid Input")
else:
    km = float(input("Enter the distance covered\n"))
    if km <= 0:
        print(f"{int(km)} is a Invalid Input")
    else:
        #liter per 100km conversion
        liters_per_100km = (liters / km) * 100
        
        #miles per gallon conversion
        miles = km * 0.6214
        gallon = liters * 0.2642
        miles_per_gallon = miles / gallon
        
        print("Liters/100km")
        print(f"{liters_per_100km:.2f}")
        print("\nMiles/gallons")
        print(f"{miles_per_gallon:.2f}")





# # in functions
# def is_valid_input(value):
#     return value > 0
# def calculate_liter_per_100km(liters, km):
#     return (liters / km) * 100
# def calculate_miles_per_gallon(liters, km):
#     miles = km * 0.6214
#     gallon = liters * 0.2642
#     return miles / gallon

# def main():
#     try:
#         # liter per 100km conversion
#         liters = float(input("Enter the no of liters to fill the tank\n"))
#         if not is_valid_input(liters):
#             print(f"{int(liters)} is a Invalid Input")
#             return
        
#         # miles per gallon conversion
#         km = float(input("Enter the distance covered\n"))
#         if not is_valid_input(km):
#             print(f"{int(km)} is a Invalid Input")
#             return
        
#         liters_per_100km = calculate_liter_per_100km(liters, km)
#         miles_per_gallon = calculate_miles_per_gallon(liters, km)
        
#         print("Liters/100km")
#         print(f"{liters_per_100km:.2f}")
#         print("\nMiles/gallons")
#         print(f"{miles_per_gallon:.2f}")
        
#     except ValueError:
#         print("Invalid input. Please enter a valid input number.")
        
# main()