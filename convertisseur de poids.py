weight = float(input("ENTER YOUR WEIGHT : "))
unit = input("KILOGRAMS OR POUNDS ? (k or l): ")

if unit == "k4":
    weight = weight * 2.205
    unit = "lbs"
    print(f"YOUR WEIGHT IS : {round(weight, 1)} {unit}")
elif unit == "l":
    weight = weight /2.205
    unit = "kg"
    print(f"YOUR WEIGHT IS : {round(weight, 1)} {unit}")

else:
    print(f"{unit} was not valid")

