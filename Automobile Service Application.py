
selection = input("Please make a selection \n1-Oil Change\n2-Tire Rotation\n3-Car Wash: ")

print(selection)

if selection == "1":
    print("You have selected Oil Change")
    service_amount = 35
elif selection == "2":
    print("You have selected Tire Rotation")
    service_amount = 19
elif selection == "3":
    print("You have selected Car Wash")
    service_amount = 7
else:
    print("You have entered an invalid selection")

vehicle_year = input("Please enter year of vehicle: ")

age = 2023 - int(vehicle_year)

print(age)
  
if age < 1:
    surcharge = 0
    print("Vehicle surcharge is $0")
elif age >= 1 and age < 5:
    surcharge = 5
    print("Vehicle surcharge is $5")
elif age >= 5 and age < 10:
    surcharge = 10
    print("Vehicle surcharge is $10")
elif age > 10:
    surcharge = 20
    print("Vehicle surcharge is $20")

total_due = service_amount + surcharge
print()
print("Service Amount is: $" + str(service_amount))
print("Age of vehicle is: " + str(age))
print("Surchage Fee is: $" + str(surcharge))
print("Total Due is: $" + str(total_due))











                       






















