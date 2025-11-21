import sys
if len(sys.argv) == 4:
    distance = float(sys.argv[1])
    fuel_used = float(sys.argv[2])
    mileage = float(sys.argv[3])

   
else:
    distance = 200
    fuel_used = 20
    mileage =15
efficiency = distance / fuel_used
print("Distance Travelled:", distance, "km")
print("Fuel Used:", fuel_used, "liters")
print("Mileage:", mileage, "km/l")
print("Fuel Efficiency:", round(efficiency, 2), "km/l")
