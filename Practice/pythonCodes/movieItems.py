total_pizzas_count = int(input("Enter the no of pizzas bought: "))
total_puffs_count = int(input("Enter the no of puffs bought: "))
total_cooldrinks_count = int(input("Enter the no of cool drinks bought: "))

total_bill =  total_pizzas_count * 100 + total_puffs_count * 20 + total_cooldrinks_count * 10

print("Bill Details")

print("No of pizzas:{}".format(total_pizzas_count))
print("No of puffs:{}".format(total_puffs_count))
print("No of cooldrinks:{}".format(total_cooldrinks_count))
print("total Price={}".format(total_bill))

print("ENJOY THE SHOW!!!")