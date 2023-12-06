with open("input") as file:
    total = 1
    data = file.readlines()
    raceTimeStrings = [time for time in data[0].split(":")[1].strip().split()]
    raceRecordString = [time for time in data[1].split(":")[1].strip().split()]
    raceTime = ""
    raceRecord = ""
    for timeString in raceTimeStrings:
        raceTime += timeString
    for timeString in raceRecordString:
        raceRecord += timeString
    raceTime = int(raceTime)
    raceRecord = int(raceRecord)

    ways = 0
    for i in range(raceTime):
        if i*(raceTime-i) > raceRecord:
            ways += 1

    print(ways)
