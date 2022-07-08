wall = int(input("enter the square feet of wall space to be painted : "))

costPerGallon = int(input("enter price of the paint per gallon : "))

noGallon = (wall * 1)/115
hoursRequired = (wall * 8)/115
costPaint = noGallon * costPerGallon 
charges = hoursRequired * hoursRequired
totalCost = int(costPaint) + int(charges) 

print("The number of gallons of paint required is :" + str(noGallon))
print("The hours of labor required is :" + str(hoursRequired))
print("The cost of the paint is :" + str(costPaint))
print("The labor charges  is :" + str(charges))
print("The total cost of the paint job is :" + str(totalCost))
