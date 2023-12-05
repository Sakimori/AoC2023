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

def getBoundaries(start, end, mapList):
    boundaries = [(start, end)]
    oldBoundaries = []
    convertedBoundaries = []
    while oldBoundaries != boundaries:
        oldBoundaries = boundaries
        boundaries = []
        for boundaryStart, boundaryEnd in oldBoundaries:
            split = False
            for line in mapList:              
                sourceStart, destStart, length = tuple(line)
                if sourceStart > boundaryStart and sourceStart < boundaryEnd :
                    boundaries += [(boundaryStart, sourceStart-1),(sourceStart,boundaryEnd)]
                    split = True
                    break
                elif sourceStart+length > boundaryStart and sourceStart+length < boundaryEnd:
                    boundaries += [(boundaryStart,sourceStart+length-1),(sourceStart+length,boundaryEnd)]
                    split = True
                    break
            if not split:
                boundaries += [(boundaryStart, boundaryEnd)]
    for boundaryStart, boundaryEnd in boundaries:
        convertedBoundaries.append((getLocation(boundaryStart, mapList),getLocation(boundaryEnd,mapList)))
    return convertedBoundaries
            



with open("input") as file:
    low = None
    ranges = []
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
    for index in range(int(len(seeds)/2)):
        locationRange = [(seeds[index*2], seeds[index*2]+seeds[index*2+1])]
        for mapIndex in range(0,7):
            splitRange = []
            for start, end in locationRange:
                splitRange += getBoundaries(start, end, maps[mapIndex])
            locationRange = splitRange.copy()
        ranges.append(locationRange)
    for locationRange in ranges:
        subLow = None
        for start, end in locationRange:
            if subLow is None or start < subLow:
                subLow = start
        if low is None or subLow < low:
            low = subLow
print(low)