# find and calculating the wheels of the vehicle

#1
vehicle = int(input("Enter the total no.of vehicle: "))
wheels = int(input("Enter the total number of wheels: "))
if wheels % 2 != 0 or wheels < 2 or wheels >4*vehicle or wheels < 2*vehicle:
    print("Invalid input")
else:
    f_w = (wheels-2*vehicle) // 2
    t_w = vehicle - f_w
    print(f"Tw: {t_w} Fw: {f_w}")