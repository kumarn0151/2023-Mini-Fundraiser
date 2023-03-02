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


# main routine starts here
yes_no_list = ["yes", "no"]
payment_list = ["cash", "credit"]

want_instructions = string_checker("Do you want to see the instructions",
                                   1, yes_no_list)
print(f"You chose {want_instructions}")

payment_method = string_checker("How do you want to pay?", 2,
                                payment_list)

print(f"You are paying with {payment_method}")
