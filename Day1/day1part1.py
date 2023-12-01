with open("input") as file:
    total = 0
    for line in file.readlines():
        first = None
        last = None
        for char in line:
            if char.isnumeric():
                if first is None:
                    first = char
                else:
                    last = char
        if last is not None:
            total += int(f"{first}{last}")
        else:
            total += int(f"{first}{first}")
    print(total)