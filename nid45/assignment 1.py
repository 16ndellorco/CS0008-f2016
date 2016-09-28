unit = (input("Are you using USC? "))
if unit in ['yes', 'Yes']:
    distance = int(input("How many miles did you drive? "))
    gas = int(input("How many gallons of gas did you use? "))
    kilometers = distance * 1.60934
    liters = gas*3.78541
    cm = (liters/100)*kilometers
    if cm > 20:
        GCR = "extremely poor"
    elif cm > 15:
        GCR = "poor"
    elif cm > 10:
        GCR = "average"
    elif cm > 8:
        GCR = "good"
    else:
        GCR = "excellent"
    print("Distance: ", format(distance, '.3f'), "Miles", format(kilometers, '.3f'), "Km", sep=' ')
    print("Gas: ", format(gas, '.3f'), "Gallons", format(liters, '.3f'), "Liters", sep=' ')
    print("Consumption: ", format(distance/gas, '.3f'), "mpg", format(kilometers/liters, '.3f'), "L/100km", sep='')
    print("Your Gas Consumption Rating is", GCR)
elif unit in ['no', 'No']:
    distance = int(input("How many kilometers did you drive? "))
    gas = int(input("How many Liters of gas did you use? "))
    miles = distance * .621371
    gallons = gas * .264172
    cm = (gas / 100) * distance
    if cm > 20:
        GCR = "extremely poor"
    elif cm > 15:
        GCR = "poor"
    elif cm > 10:
        GCR = "average"
    elif cm > 8:
        GCR = "good"
    else:
        GCR = "excellent"
    print("Distance: ", format(miles, '.3f'), "Miles", format(distance, '.3f'), "Km", sep=' ')
    print("Gas: ", format(gallons, '.3f'), "Gallons", format(gas, '.3f'), "Liters", sep=' ')
    print("Consumption: ", format(miles / gallons, '.3f'), "mpg", format(distance / gas, '.3f'), "L/100km", sep='')
    print("Your Gas Consumption Rating is", GCR)
else:
    print("""Please enter either "Yes" or "No""")