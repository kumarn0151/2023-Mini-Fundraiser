import pandas


# functions go here

def not_blank(question):
    while True:
        response = input(question)

        if response != "":
            return response

        else:
            print("This can't be blank, please enter a response")
            print()


# checks users enter am integer to a given question
def num_check(question):
    while True:

        try:
            response = int(input(question))
            return response

        except ValueError:
            print("Please enter an integer.")


# Calculate the ticket price based on the age
def calc_ticket_price(var_age):
    # ticket is $7:50 for users under 16
    if var_age < 16:
        price = 7.5

    # ticket is $10.50 for users between 16 and 64
    elif var_age < 65:
        price = 10.5

    # ticket price is $6:50 for seniors (65+)
    else:
        price = 6.5

    return price


# check that users enter a valid response (eg: yes / no)
# cash / credit based on list of options
def string_checker(question, num_letters, valid_response):
    if num_letters == 1:
        short_version = 1
    else:
        short_version = 2

    while True:
        response = input(question).lower()

        for item in valid_response:
            if response == item[:short_version] or response == item:
                return item

        print(f"Please enter {valid_response[0]} or {valid_response[1]}")


# currency formatting function
def currency(x):
    return "${:.2f}".format(x)


# main routine starts here

# set maximum number of below
MAX_TICKETS = 50
ticket_sold = 0

yes_no_list = ["yes", "no"]
payment_list = ["cash", "credit"]

# List to hold ticket details
all_names = []
all_ticket_cost = []
all_surcharge = []

mini_movie_dict = {
    "Name": all_names,
    "Ticket Price": all_ticket_cost,
    "Surcharge": all_surcharge
}

# Ask user if they want see the instructions

want_instructions = string_checker("Do you want to read the"
                                   " instructions (y/n):",
                                   1, yes_no_list)

if want_instructions == "yes":
    print("instructions go here")

print()

# loop to sell tickets

while ticket_sold < MAX_TICKETS:
    name = not_blank("Please enter your name or 'xxx' to quit: ")

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

    # calculate ticket cost
    ticket_cost = calc_ticket_price(age)
    print("Age: {}, Ticket Price: ${:.2f}".format(age, ticket_cost))

    # get payment method
    payment_method = string_checker("choose a payment method "
                                    "(cash /credit)",
                                    2, payment_list)
    if payment_method == "cash":
        surcharge = 0
    else:
        # calculate 5% surcharge if users are paying by credit card
        surcharge = ticket_cost * 0.05

    print(f'You chose {payment_method}')

    # add ticket name, cost and surcharge to lists
    all_names.append(name)
    all_ticket_cost.append(ticket_cost)
    all_surcharge.append(surcharge)

# create data frame from dictionary to organise information
mini_movie_frame = pandas.DataFrame(mini_movie_dict)
mini_movie_frame = mini_movie_frame.set_index('Name')

# Calculate the total ticket cost (ticket + surcharge)
mini_movie_frame['Total'] = mini_movie_frame['Surcharge'] \
                            + mini_movie_frame['Ticket Price']

# calculate the profit for each ticket
mini_movie_frame['Profit'] = mini_movie_frame['Ticket Price'] - 5

# calculate ticket and profit totals
total = mini_movie_frame['Total'].sum()
profit = mini_movie_frame['Profit'].sum()

# Currency Formatting (uses currency function)
add_dollars = ['Ticket Price', 'Surcharge', 'Total', 'Profit']
for var_item in add_dollars:
    mini_movie_frame[var_item] = mini_movie_frame[var_item].apply(currency)

print("---- Ticket Data ----")
print()

# output table with ticket data
print(mini_movie_frame)

print()
print("----- Ticket Cost / Profit -----")

# output total ticket sales and profit
print("Total Ticket Sales: ${:.2f}".format(total))
print("Total Price : ${:.2f}".format(profit))

# output number of tickets sold
if ticket_sold == MAX_TICKETS:
    print("Congratulations you have sold all the tickets")
else:
    print("You have sold {} ticket/s. There is {} ticket/s "
          "remaining".format(ticket_sold, MAX_TICKETS - ticket_sold))
