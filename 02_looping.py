# main routine starts here

# set maxium number of below
MAX_TICKETS = 3

# loop to sell tickets
ticket_sold = 0
while ticket_sold < MAX_TICKETS:
    name = input("Please enter your name or 'xxx' to quit: ")

    if name == 'xxx':
        break

    ticket_sold += 1

# output number of tickets sold
if ticket_sold == MAX_TICKETS:
    print("Congratulations you have sold all the tickets")

else:
    print("You have sold {} ticket/s. There is {} ticket/s remaining".format(ticket_sold, MAX_TICKETS - ticket_sold))
