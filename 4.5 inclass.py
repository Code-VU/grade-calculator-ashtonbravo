def getTickets():
    getSingleTicket()
    print("---")
    getSingleTicket()
    print("---")
    getSingleTicket()

def getSingleTicket():
    speedLimit = 60
    bigTicketOffSet = 20
    speed = int(input("How fast were they going?: "))
    birthday = input("Is it their birthday (y/n): ")
    if(birthday.upper()=="Y"):
        speedLimit += 5
    if(speed>speedLimit+bigTicketOffSet):
        print("big ticket")
    elif(speed>speedLimit):
        print("small ticket")
    else:
        print("No Ticket")
getTickets()