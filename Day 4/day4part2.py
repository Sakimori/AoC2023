with open("input") as file:
    total = 0
    cards = [(line.split(":")[1].split("|")[0].strip(),line.split(":")[1].split("|")[1].strip(),1) for line in file.readlines()] #winners, owned, copies
    for index in range(len(cards)):
        winnerString, ownedString, copies = cards[index]
        winners = [int(num) for num in winnerString.split()]
        owned = [int(num) for num in ownedString.split()]
        count = 1
        for winner in winners:
            if winner in owned:
                count += 1
        for i in range(1,count):
            try:
                cards[index+i] = (cards[index+i][0], cards[index+i][1], cards[index+i][2]+copies)
            except IndexError:
                pass
    for card in cards:
        total += card[2]
print(total)