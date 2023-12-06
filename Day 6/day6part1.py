with open("input") as file:
    total = 1
    data = file.readlines()
    raceTimes = [int(time) for time in data[0].split(":")[1].strip().split()]
    raceRecords = [int(time) for time in data[1].split(":")[1].strip().split()]
    races = list(zip(raceTimes, raceRecords))
    for time, record in races:
        ways = 0
        for i in range(time):
            if i*(time-i) > record:
                ways += 1
        total *= ways
    print(total)
