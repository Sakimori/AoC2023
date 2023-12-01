numStringList = [("one","1"), ("two","2"), ("three","3"), ("four","4"), ("five","5"), ("six","6"), ("seven","7"), ("eight","8"), ("nine","9")]
total = 0
with open("input") as file:
    for line in file.readlines():
        #digit, index
        first = (None, None)
        last = (None, None)
        #find proper digits
        for charIndex in range(len(line)):
            if line[charIndex].isnumeric():
                if first[0] is None:
                    first = (line[charIndex], charIndex)
                else:
                    last = (line[charIndex], charIndex)
        #find string digits
        for numStringWord, numStringValue in numStringList:
            stringIndex = line.find(numStringWord)
            rStringIndex = line.rfind(numStringWord)
            if stringIndex != -1:
                if stringIndex <= first[1]:
                    if last[1] is None:
                        last = (first[0], first[1])
                    first = (numStringValue, stringIndex)
                if last[1] is None or rStringIndex > last[1]:
                    last = (numStringValue, rStringIndex)
        if last[0] is not None:
            total += int(f"{first[0]}{last[0]}")
        else:
            total += int(f"{first[0]}{first[0]}")
    print(total)