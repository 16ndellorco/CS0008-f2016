unit = (input("Are you using USC (US Customary Units)? "))
if unit in ['yes', 'Yes']:
    distance = float(input("How many miles did you drive? "))
    gas = float(input("How many gallons of gas did you use? "))
    kilometers = distance * 1.60934
    liters = gas*3.78541
    cm = (liters*100)/kilometers
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
    print("Distance:____: ", format(distance, '.3f'), "Miles", format(kilometers, '.3f'), "Km", sep=' ')
    print("Gas:_________: ", format(gas, '.3f'), "Gallons", format(liters, '.3f'), "Liters", sep=' ')
    print("Consumption__:", format(distance/gas, '.3f'), " mpg", format(100*liters/kilometers, '.3f'), "L/100km", sep=' ')
    print("Your Gas Consumption Rating is", GCR)
elif unit in ['no', 'No']:
    distance = float(input("How many kilometers did you drive? "))
    gas = float(input("How many Liters of gas did you use? "))
    miles = distance * .621371
    gallons = gas * .264172
    cm = gas * (distance*100)
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
    print("Distance _____:", format(miles, '.3f'), "Miles", format(distance, '.3f'), "Km", sep=' ')
    print("Gas __________:", format(gallons, '.3f'), "Gallons", format(gas, '.3f'), "Liters", sep=' ')
    print("Consumption __:", format(miles / gallons, '.3f'), "mpg",
          format(100*(gas/distance), '.3f'), "L/100km", sep=' ')
    print("Your Gas Consumption Rating is", GCR)
else:
    print("""Please enter either "Yes" or "No""")