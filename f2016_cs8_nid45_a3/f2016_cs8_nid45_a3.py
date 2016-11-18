
# printKV: prints and formats key and values based on data type
def printKV(key, value, klen = 0):
    # print simple strings without value
    if value == None:
        print(key)

    # check for different data types
    if isinstance(value, str):
        print('{:<{}}: {}'.format(key, len(key) + klen, value))
    elif isinstance(value, float):
        print('{:<{}}: {:0.5f}'.format(key, len(key) + klen, value))
    elif isinstance(value, int):
        print('{:<{}}: {}'.format(key, len(key) + klen, value))

def get_stats(info):
    # dictionary to store stats
    stats = {}

    # store files read
    stats['FileCount'] = len(info.keys())

    count_lines = 0
    total_distance = 0

    # store max distance run and
    # participant in a set
    max_distance_run = ('', float(0))

    # store min distance run and
    # participant in a set
    min_distance_run = ('', float(1000))

    # to count participants with multiple records
    participants = {}

    for key in info.keys():
        # get number of values for each key
        count_lines += len(info[key])
        # sum total distance
        for item in info[key]:
            item = item.split(',')
            distance = float(item[1])
            total_distance += distance

            # add participants to a dictionary to count for multiple
            # records the distance they ran
            if item[0].strip() not in participants.keys():
                participants[item[0].strip()] = (1, distance)
            else:
                participants[item[0].strip()] = (participants[item[0].strip()][0] + 1, participants[item[0].strip()][1] + distance)
            # store the max distance run and participant name
            if distance > max_distance_run[1]:
                max_distance_run = (item[0], distance)
            # store the min distance and participant name
            if distance < min_distance_run[1]:
                min_distance_run = (item[0], distance)

    # count participants with more than one record
    multiple_records_participant = 0
    for participant in participants.keys():
        if participants[participant][0] > 1:
            multiple_records_participant += 1

    # store info in dictionary keys
    stats['TotalLines'] = count_lines
    stats['TotalDistanceRun'] = total_distance
    stats['MaxDistanceRun'] = max_distance_run
    stats['MinDistanceRun'] = min_distance_run
    stats['ParticipantCount'] = count_lines
    stats['Multiplecounts'] = multiple_records_participant

    # create output file
    with open('f2016_cs8_nid45_a3.data.output.csv', 'w') as filehandle:
        for key in participants.keys():
            filehandle.write('{},{},{:0.2f}\n'.format(key, participants[key][0], participants[key][1]))

    # now return stats
    return stats

# main function
def main():
    # gets the file name to be read
    masterfile = 'f2016_cs8_a3.data.txt'
    # store each file info in a dictionary
    fileinfo = {}
    # use to store each file values
    values = []
    # open file by using with open
    with open(masterfile, 'r') as fileHandle:
        # read all lines from master file
        lines = fileHandle.readlines()
        # loop through each line
        for line in lines:
            # remove new line character
            line = line.replace('\n','')
            # set a dictionary key from the master file lines
            # and set its values to an empty list
            fileinfo[line] = []

    # loop through each key which is the file in master list
    for key in fileinfo.keys():
        # open the file
        with open(key, 'r') as fileHandle:
            # read all lines
            lines = fileHandle.readlines()
            # counter use to skip header
            counter = 0
            for line in lines:
                if counter > 0:
                    # remove new line character
                    line = line.replace('\n','')
                    # add each line to dictionary values
                    fileinfo[key].append(line)
                counter += 1

    # at this point we have all the information
    # in memory, so we have to get the results
    info = get_stats(fileinfo)

    # get line count and total distance
    printKV('Number of Input files read', info['FileCount'], 10)
    printKV('Total number of lines read', info['TotalLines'],10)
    printKV('\nTotal distance run', info['TotalDistanceRun'],18)
    printKV('\nMax distance run', info['MaxDistanceRun'][1],20)
    printKV('by participant', info['MaxDistanceRun'][0],22)
    printKV('\nMin distance run', info['MinDistanceRun'][1],20)
    printKV('by participant', info['MinDistanceRun'][0],22)
    printKV('\nTotal number of participants', info['ParticipantCount'],8)
    printKV('Number of participants\nwith multiple records', info['Multiplecounts'],15)

    # add a new line at the end
    print(end='\n')

if __name__ == "__main__":
    # call the main function
    main()
