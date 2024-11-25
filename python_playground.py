olympic_barbell = 45
units = input("Enter the unit of measurment for the plates (L for lbs or K for kgs): ")
plate_weight = input("Enter weight of plates: ")
plate_number = input("Enter the number of plates per side of barbell: ")
conversion = 2.20462

#take inputs above and calculate raw weight in listed unit of measurement
total_plate_weight = (int(plate_weight) * int(plate_number)) * 2

#Outputs total weight including the barbell
total_weight = total_plate_weight + olympic_barbell
print(total_weight)

#Take results and output total weight in both kgs and lbs
if units.lower() == "l":
    kg = total_weight / conversion
    print("The total weight is: " + str(total_weight) + "lbs")
    print("or")
    print(str(kg) + "kgs")
elif units.lower() == "k":
    lb = total_weight * conversion
    print("The total weight is: " + str(total_weight) + "kgs")
    print("or")
    print(str(lb) + "lbs")
else:
    print("Invalid unit entered. Please type L or K")

    

