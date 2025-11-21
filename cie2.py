import sys

# Give values inside the code
sys.argv = ["fuel.py", "300", "20", "15"]   # distance, fuel used, mileage

if len(sys.argv) == 4:
    distance = float(sys.argv[1])
    fuel_used = float(sys.argv[2])
    mileage = float(sys.argv[3])

    if fuel_used != 0:
        efficiency = distance / fuel_used
        print("Distance Travelled:", distance, "km")
        print("Fuel Used:", fuel_used, "liters")
        print("Mileage:", mileage, "km/l")
        print("Fuel Efficiency:", round(efficiency, 2), "km/l")
    else:
        print("Fuel used cannot be zero!")
else:
    print("Usage: python fuel.py <distance> <fuel_used> <mileage>")
