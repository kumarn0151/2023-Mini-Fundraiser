# functions go here

# Checks user has entered yes / no to a question
def yes_no(question):
    while True:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"

        elif response == "no" or response == "n":
            return "no"

        else:
            print("Please enter yes or no")


# checks users enter am integer to a given question
def num_check(question):
    while True:

        try:
            response = int(input(question))
            return response

        except ValueError:
            print("Please enter an integer.")


# main routine starts here

# set maximum number of below
MAX_TICKETS = 3
ticket_sold = 0
# Ask user if they want see the instructions

want_instructions = yes_no("Do you want to read the instructions?")

if want_instructions == "yes":
    print("instructions go here")

print()

# loop to sell tickets

while ticket_sold < MAX_TICKETS:
    name = input("Please enter your name or 'xxx' to quit: ")

    if name == 'xxx':
        break

    age = num_check("Age: ")

    if 12 <= age <= 120:
        pass
    elif age < 12:
        print("sorry you are too young for this movie")
        continue
    else:
        print("?? That looks like a typo, please try again.")
        continue

    ticket_sold += 1

# output number of tickets sold
if ticket_sold == MAX_TICKETS:
    print("Congratulations you have sold all the tickets")

else:
    print("You have sold {} ticket/s. There is {} ticket/s "
          "remaining".format(ticket_sold, MAX_TICKETS - ticket_sold))
