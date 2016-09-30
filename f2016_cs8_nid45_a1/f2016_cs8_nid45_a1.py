unit = (input("Are you using USC (US Customary Units)? "))   #find the units the user wants to use
if unit in ['yes', 'Yes']:
    distance = float(input("How many miles did you drive? "))   #if they choose USC ask in terms of miles and gallons
    gas = float(input("How many gallons of gas did you use? "))
    kilometers = distance * 1.60934  #must convert to metric in order to find cm/efficiency
    liters = gas*3.78541
    cm = (liters*100)/kilometers  #use what you got from the conversions to determine cm
    if cm > 20:  #use given gas consumption rating ranges
        GCR = "Extremely Poor"
    elif cm > 15:
        GCR = "Poor"
    elif cm > 10:
        GCR = "Average"
    elif cm > 8:
        GCR = "Good"
    else:
        GCR = "Excellent"
    print(format("\n ", '32s'), format("USC", '22s'), format("Metric"))
    print("Distance:______________:", format(distance, '10.3f'), "Miles", format(kilometers, '19.3f'), "Km")  #print in the needed format with 3 columns, (ask how to do columns correctly)
    print("Gas:___________________:", format(gas, '10.3f'), "Gallons", format(liters, '17.3f'), "Liters")
    print("Consumption____________:", format(distance/gas, '10.3f'), "mpg", format(100*liters/kilometers, '21.3f'), "L/100km")
    print("\nGas Consumption Rating : ", GCR)
elif unit in ['no', 'No']:  #if user says no they want to input information in metric system
    distance = float(input("How many kilometers did you drive? "))  #ask in terms of kilometers/liters
    gas = float(input("How many Liters of gas did you use? "))
    miles = distance * .621371  #find miles so you can complete chart at the end
    gallons = gas * .264172
    cm = (gas*100)/distance  #use what the user provided to find the cm/efficiency
    if cm > 20:
        GCR = "Extremely Poor"
    elif cm > 15:
        GCR = "Poor"
    elif cm > 10:
        GCR = "Average"
    elif cm > 8:
        GCR = "Good"
    else:
        GCR = "Excellent"
    print(format("\n ", '31s'), format("USC", '23s'), format("Metric"))
    print("Distance ______________:", format(miles, '9.3f'), "Miles", format(distance, '20.3f'), "Km", sep=' ')
    print("Gas ___________________:", format(gallons, '9.3f'), "Gallons", format(gas, '18.3f'), "Liters", sep=' ')
    print("Consumption ___________:", format(miles / gallons, '9.3f'), "mpg",\
          format(100*(gas/distance), '22.3f'), "L/100km", sep=' ')
    print("\nGas Consumption Rating :", GCR) #give rating based on given data
else:
    print("""Please enter either "Yes" or "No""")  #user must say yes or no to initial question