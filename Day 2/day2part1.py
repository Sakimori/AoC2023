with open("input") as file:
    total = 0
    count = 1 #one-indexed
    for line in file.readlines():
        thisGame = {"red":0, "green":0, "blue":0}
        line = line.split(":")[1]
        pulls = line.split(";")
        for pull in pulls:
            colors = pull.split(",")
            for colorNumString in colors:
                icount, color = tuple(colorNumString.strip().split(" "))
                if thisGame[color] < int(icount):
                    thisGame[color] = int(icount)
        if thisGame["red"] > 12 or thisGame["green"] > 13 or thisGame["blue"] > 14:
            pass
        else:
            total += count
        count += 1
print(total)