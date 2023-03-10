# Printing the format according to the question
print("########################")
print("MYPY PHONE BOOK")
print("########################")


# Created a function to get the name from user


def get_name():
    first_name = input("Enter the first name\n")
    last_name = input("Enter the last name\n")
    return first_name + " " + last_name


# Making a counter to run the phone book until pressed 5
should_continue = True
# Creating an empty dictionary in which we will store our phone book
new_dict = {}

# Start of the While loop and keeps on looping to ask the user and perform the required action
while should_continue:
    # Giving all the options to the user
    print("1 : Add New Entry")
    print("2 : Delete Entry")
    print("3 : Update Entry")
    print("4 : Lookup Entry")
    print("5 : QUIT")

    # Getting the input from the user based on the menu delivered before
    check = int(input())

    # The block where we add a new entry
    if check == 1:
        print("ADD ENTRY")
        # Calling the function to get the first and last name of the entry
        name = get_name()
        # Getting the phone number to add
        phone_no = int(input("Enter the phone number\n"))
        # Storing the phone number in the dictionary
        new_dict[name] = phone_no
        print(f"Success {new_dict}")

    # The block where we delete an entry
    elif check == 2:
        print("DELETE ENTRY")
        name = get_name()
        # Using the del keyword to delete and entry of the dictionary based on the name
        del new_dict[name]
        print(f"Success {new_dict}")

    # The block where an entry is updated
    elif check == 3:
        print("UPDATE ENTRY")
        # Calling the function to get the name to be updated
        name = get_name()
        # Asking if the user wants to update the name or phone number
        choice = input("Press 1 to update name or press 2 to update phone no: ")
        # Checking if user entered the correct name to avoid key error
        if name not in new_dict:
            print("WRONG INPUT")
        # If correct name is entered then we update name if 1 or phone no if choice is 2
        else:
            if choice == "1":
                new_ph = new_dict[name]
                new_name = get_name()
                # Deleting the old name entry
                del new_dict[name]
                # Creating the new Entry hence updated
                new_dict[new_name] = new_ph
                print(f"Success {new_dict}")
            # The block where we update the phone number
            else:
                # Getting the new phone number from the user
                new_ph = int(input("Enter new phone number: "))
                # Updating the value(phone number) of the name entered by the user
                new_dict[name] = new_ph
                # Printing our dictionary to fail proof check our details
                print(new_dict)

    # The block where we look up and create a new entry if number does not exist
    elif check == 4:
        print("LOOKUP ENTRY")
        # taking the choice from user to check either name of phone number
        name_or_phone = input("Press 1 to check the name and 2 to check the phone number. \n")
        # If user wants to check the phone number we go with '1'
        if name_or_phone == '1':
            name = get_name()
            # checking if the name exists in the dictionary and if not then asking if user wants to save!
            if name not in new_dict:
                print("Your contact name does not exist")
                save = input("Press 1 to save")
                # Saving the new entry which did not exist
                if save == 1:
                    new_phone = int(input("Enter the phone number"))
                    new_dict[name] = new_phone
                    print("saved!")
            # Entry existed already thus showing the results
            else:
                print(f"Your contact info exists {name} : {new_dict[name]}")
        # If user wants to check the name we go with '2'
        elif name_or_phone == '2':
            check_num = int(input("Enter the phone number to check"))
            # Checking if the phone num exists in the dictionary amongst the values
            if check_num in new_dict.values():
                print("Your phone number exists")
                # If the value exists then we figure out at what key does the value exists by for loop checking
                for j in new_dict:
                    # Proofing if the number entered equals the looped key value
                    if check_num == new_dict[j]:
                        # Printing the value that was their under the name it was saved as key value pair
                        print(f"{j}:{new_dict[j]}")
            # If the number does not exist then we ask the user the choice to save it
            else:
                print("Your phone number does not exist. Do you want to save this number as a new contact?")
                save_or_not = input("Press 1 to save")
                # checking if the user wants to save the entered info as new number
                if save_or_not == '1':
                    # Saving the new check_num phone number as a new contact name by using the name function
                    name = get_name()
                    new_dict[name] = check_num

    # The block where the check entered is 5 then making the counter stop
    elif check == 5:
        should_continue = False

    # Default quit if wrong input by user
    else:
        quit()
