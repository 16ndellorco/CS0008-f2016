
# printKV: prints and formats key and values based on data type
def printKV(key, value, klen = 0):
    # print simple strings without value
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
    lineCount = 0    # track total distance and line count
    totalDistance = 0

    for l in lines: # loop through each line in the file
        # remove new line character
        l = l.rstrip('\n')
        # split name and distance
        info = l.split(',')
        # only process lines where a name and distance are found
        if len(info) == 2:
            # set distance variable from value in file
            distance = float(info[1])
            if isinstance(distance, float):  # make sure distance is a float
                totalDistance += distance
            lineCount += 1  # increment line count, increases by 1 at at time
    return (lineCount, totalDistance)  # return two values, line count and total distance

def summary(totalLineCount, totalDistance):
    printKV('Totals', None)
    printKV('Total # of lines', totalLineCount,  8)
    printKV('Total distance run', totalDistance, 6)
# main function this is the first entry into the program
def main():

    FinalLineCount = 0
    FinalDistance  = 0

    while True:     # loop to keep asking for files to read
        # gets the file name to be read
        fileName = input('File to be read: ')

        if fileName.lower() == 'quit':   # if user enters quit, display totals
            # display of totals
            summary(FinalLineCount, FinalDistance)
            break  #terminates current function

        # validate input by making sure length is > 0 and it is a string variable otherwise display invalid input
        if not len(fileName) == 0 and not isinstance(fileName, str):
            print('Invalid input.')
            continue
        else:
            # open file by using open function
            with open(fileName, 'r') as fileHandle:
                # get line count and total distance
                values = processFile(fileHandle)

                # print line count and distance
                printKV('Partial Total # of lines',values[0])
                printKV('Partial distance run',values[1], 4)

                # add totals to grand total
                FinalLineCount += values[0]
                FinalDistance  += values[1]
                print(end='\n') # add a new line at the end
            # file is automatically closed when using the keyword

if __name__ == "__main__":
    main()    # call the main function