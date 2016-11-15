# printKV: prints and formats key and values based on data type
def printKV(key, value, klen = 0):
    # prints simple strings without value
    if value == None:
        print(key)
    # check for different data types
    if isinstance(value, str):
        print('{:<{}}: {:>20}'.format(key, len(key) + klen, value))
    elif isinstance(value, float):
        print('{:<{}}: {:>10.3f}'.format(key, len(key) + klen, value))
    elif isinstance(value, int):
        print('{:<{}}: {:>10}'.format(key, len(key) + klen, value))
# processFile: process a file and reads and loops through all lines of file handled
def processFile(fh):
    # read all lines and store them in a variable
    lines = fh.readlines()
    # track how many lines there're in the file
    linecount = 0
    # track total distance
    totaldistance = 0
    # loop through each line in the file
    for l in lines:
        # remove new line character
        l = l.rstrip('\n')
        # split name and distance
        info = l.split(',')
        # only process lines where a name and
        # distance are found
        if len(info) == 2:
            # set distance variable from value in file
            distance = float(info[1])
            # make sure distance is a float
            if isinstance(distance, float):
                totaldistance += distance
            # increment line count, increases by 1 at a time
            linecount += 1
    # returns two values, line count and total distance
    return (linecount, totaldistance)
def summary(totallinecount, totaldistance):
    printKV('Totals', None)
    printKV('Total # of lines', totallinecount,  8)
    printKV('Total distance run', totaldistance, 6)
# main function this is the first entry into the program
def main():
    finallinecount = 0
    finaldistance  = 0
    # loop to keep asking for files to read
    while True:
        # gets the file name to be read
        fileName = input('File to be read: ')
        # if user enters quit, display totals
        if fileName.lower() == 'quit':
            # display of totals
            summary(finallinecount, finaldistance)
            break
# validate input by making sure length is > 0 and it is a string variable otherwise display invalid input
        if not len(fileName) == 0 and not isinstance(fileName, str):
            print('Invalid input.')
            continue
        else:
            # open file by using the open function
            with open(fileName, 'r') as fileHandle:
                # find the total line count and total distance
                values = processFile(fileHandle)
                # prints the line count and distance
                printKV('Partial Total # of lines',values[0])
                printKV('Partial distance run',values[1], 4)
                # add totals to grand total
                finallinecount += values[0]
                finaldistance  += values[1]
            # file is automatically closed when using the keyword
            print(end='\n')
if __name__ == "__main__":
    # call the main function
    main()