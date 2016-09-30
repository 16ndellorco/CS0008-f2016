unit = (input("Are you using USC (US Customary Units)? "))   #find the units the user wants to use
if unit in ['yes', 'Yes']:
    distance = float(input("How many miles did you drive? "))   #if they choose USC ask in terms of miles and gallons
    gas = float(input("How many gallons of gas did you use? "))
    kilometers = distance * 1.60934  #must convert to metric in order to find cm/efficiency
    liters = gas*3.78541
    cm = (liters*100)/kilometers  #use what you got from the conversions to determine cm
    if cm > 20:  #use given gas consumption rating ranges
        GCR = "extremely poor"
    elif cm > 15:
        GCR = "poor"
    elif cm > 10:
        GCR = "average"
    elif cm > 8:
        GCR = "good"
    else:
        GCR = "excellent"
    print(format(" ", '24s'), format("USC", '25s'), format("Metric"))
    print("Distance:____: ", format(distance, '12.3f'), "Miles", format(kilometers, '22.3f'), "Km")  #print in the needed format with 3 columns, (ask how to do columns correctly)
    print("Gas:_________: ", format(gas, '12.3f'), "Gallons", format(liters, '20.3f'), "Liters")
    print("Consumption__:", format(distance/gas, '13.3f'), "mpg", format(100*liters/kilometers, '24.3f'), "L/100km")
    print("\nYour Gas Consumption Rating is", GCR)
elif unit in ['no', 'No']:  #if user says no they want to input information in metric system
    distance = float(input("How many kilometers did you drive? "))  #ask in terms of kilometers/liters
    gas = float(input("How many Liters of gas did you use? "))
    miles = distance * .621371  #find miles so you can complete chart at the end
    gallons = gas * .264172
    cm = (gas*100)/distance  #use what the user provided to find the cm/efficiency
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
    print(format(" ", '24s'), format("USC", '27s'), format("Metric"))
    print("Distance _____:", format(miles, '12.3f'), "Miles", format(distance, '24.3f'), "Km", sep=' ')
    print("Gas __________:", format(gallons, '12.3f'), "Gallons", format(gas, '22.3f'), "Liters", sep=' ')
    print("Consumption __:", format(miles / gallons, '12.3f'), "mpg",\
          format(100*(gas/distance), '26.3f'), "L/100km", sep=' ')
    print("\nYour Gas Consumption Rating is", GCR) #give rating based on given data
else:
    print("""Please enter either "Yes" or "No""")  #user must say yes or no to initial question