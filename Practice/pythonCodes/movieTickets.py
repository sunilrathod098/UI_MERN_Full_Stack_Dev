def calculate_ticket_cost():
    try:
        tickets = int(input("Enter the no of tickets: "))
        if tickets < 5 or tickets > 40:
            print("Minimum 5 and maximum 40 tickets")
            return
        
        refreshment = input("Do you want refreshments? (yes/no): ").strip().lower()
        coupon = input("Do you have any coupons? (yes/no): ").strip().lower()
        circle = input("Enter a circle (k/q): ").strip().lower()
        
        if circle not in ['k', 'q']:
            print("Invalid input")
            return
        
        if circle == 'k':
            price_per_ticket = 75
        else:
            price_per_ticket = 150
            
        total = tickets * price_per_ticket
        
        #apply 10% discount if more then 20 tickets
        if tickets > 20:
            total *= 0.9
            
        #apply 2% discount if coupon is available
        if coupon == "yes":
            total *= 0.98
            
        #add refreshment cost
        if refreshment == "yes":
            total += 50 * tickets
            
        print(f"Total cost: {total:.2f}")
        
    except ValueError:
        print("Invalid input. Please enter a number for tickets.")
        
calculate_ticket_cost()