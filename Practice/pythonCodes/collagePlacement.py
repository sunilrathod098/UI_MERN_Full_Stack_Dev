cse = int(input("Enter the number of placements in CSE: "))
ece = int(input("Enter the number of placements in ECE: "))
mech = int(input("Enter the number of placements in MECH: "))

if cse < 0 or ece < 0 or mech < 0:
    print("Input is Invalid")
elif cse == ece == mech:
    print("None of the department has got the highest placement")
else:
    max_value = max(cse, ece, mech)
    print("Highest placement")
    if cse == max_value:
        print("CSE")
    if ece == max_value:
        print("ECE")
    if mech == max_value:
        print("MECH")
