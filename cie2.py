# Fuel Efficiency Calculator

# Provide input values directly in the code
distance = 400.0   # in kilometers
fuel_used = 20.0   # in liters

# Check if valid inputs are provided
if distance > 0 and fuel_used > 0:
    # Calculate mileage (fuel efficiency)
    mileage = distance / fuel_used

    # Print the fuel efficiency report
    print("------ Fuel Efficiency Report ------")
    print("Distance Travelled :", distance, "km")
    print("Fuel Used          :", fuel_used, "liters")
    print("Fuel Efficiency    :", round(mileage, 2), "km per liter")
else:
    # If invalid values are provided
    print("Error: Invalid input values!")
    print("Distance and fuel used must be greater than zero.")
