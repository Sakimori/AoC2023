with open("input") as file:
    total = 0
    cards = [(line.split(":")[1].split("|")[0].strip(),line.split(":")[1].split("|")[1].strip()) for line in file.readlines()]
    for winnerString, ownedString in cards:
        winners = [int(num) for num in winnerString.split()]
        owned = [int(num) for num in ownedString.split()]
        count = -1
        for winner in winners:
            if winner in owned:
                count += 1
        total += 2**count if count >= 0 else 0
print(total)