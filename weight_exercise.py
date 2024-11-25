weight = input("Weight: ")
measurement = input("(K)g or (L)bs: ")
conversion = 2.20462
if measurement.lower() == "l":
    kg = float(weight) / conversion
    print("Weight in Kg: " + str(kg))
elif measurement.lower() == "k":
    lb = float(weight) * conversion
    print("Weight in Lb: " + str(lb))
else:
    print("Invalid input please type K or L.")