def tryParseInt(value):
    try:
        int(value)
        return True
    except ValueError:
        return False

def tryParseFloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

requiredTickets = 0
priceForBusTicket = 0.0
amoundOfMoneyOffered = 0.0

while requiredTickets < 1:
    requiredTicketsText = input("Enter the number of bus tickets: ")
    isInt = tryParseInt(requiredTicketsText)
    if isInt == True:
        requiredTickets = int(requiredTicketsText)

while priceForBusTicket <= 0:
    priceForBusTicketText = input("Enter the price for single bus ticket: ")
    isFloat = tryParseFloat(priceForBusTicketText)
    if isFloat == True:
        priceForBusTicket = float(priceForBusTicketText)

totalCost = priceForBusTicket * float(requiredTickets)

print('Total cost: £{0:.2f}'.format(totalCost))

while amoundOfMoneyOffered < totalCost:
    while amoundOfMoneyOffered < totalCost:
        amoundOfMoneyOfferedText = input("Enter the amount of money offered: ")
        isFloat = tryParseFloat(amoundOfMoneyOfferedText)
        if isFloat == True:
            amoundOfMoneyOffered = float(amoundOfMoneyOfferedText)
            if amoundOfMoneyOffered < totalCost:
                print("Insufficient Funds!!!")

difference = amoundOfMoneyOffered - totalCost

print('Change from £{0:.2f} is £{1:.2f}'.format(amoundOfMoneyOffered, difference))
