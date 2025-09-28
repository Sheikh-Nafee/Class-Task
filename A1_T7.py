# Print info message "Calculate fuel consumption"
print("Calculate fuel consumption")

#Ask "Enter travel distance(kilometers): " and the value to feed variable
Feed = input("Enter travel distance(kilometers): ")

#Convert the Feed into integer and assign it to Distance variable
Distance = int(Feed)

#Ask "Enter fuel usage(litres): "
Feed = input("Enter fuel usage(litres): ")

#Convert the Feed into an integer and assign it to the FuelUsage variable 
FuelUsage = int(Feed)

#Calculate the Consumption for 100 km
Consumption = (FuelUsage/Distance)*100

#Convert the Consumption back to an integer
Consumption = int(Consumption) 

#Print "Fuel consumption is {Consumption} l per 100 km"
print(f"Fuel consumption is {Consumption} l per 100 km" )