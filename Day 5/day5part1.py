def generateMap(mapStringList): #source start, destination start, length
    mapIntList = []
    for line in mapStringList:
        dest, source, length = tuple(line.split())
        mapIntList.append([int(item) for item in [source, dest, length]])
    return mapIntList
    
def getLocation(source, mapList):
    for line in mapList:
        sourceStart, destStart, length = tuple(line)
        if source >= sourceStart and source < sourceStart + length:
            offset = source - sourceStart
            return destStart + offset
    return source




with open("input") as file:
    low = None
    data = file.readlines()
    seeds = [int(item) for item in data[0].split(":")[1].split()]
    seedToSoilStrings = data[3:13] #0
    soilToFertStrings = data[15:31] #1
    fertToWaterStrings = data[33:48] #2
    waterToLightStrings = data[50:95] #3
    lightToTempStrings = data[97:112] #4
    tempToHumiStrings = data[114:137] #5
    humiToLocStrings = data[139:150] #6
    mapStrings = [seedToSoilStrings, soilToFertStrings, fertToWaterStrings, waterToLightStrings, lightToTempStrings, tempToHumiStrings, humiToLocStrings]
    maps = [generateMap(mapString) for mapString in mapStrings]
    for seed in seeds:
        value = getLocation(seed, maps[0])
        for i in range(1,7):
            value = getLocation(value, maps[i])
        if low is None or value < low:
            low = value
print(low)