def start_screen():
    """Opening screen to inform user of program options."""
    print("Welcome to Mailroom Madness\n")
    print("Choose from the following:\n")
    print("T - Send a (T)hank You")
    print("R - Create a (R)eport")
    print("quit - Quit the program\n")
    path = input("What would you like to do first? ")
    if (path.upper() == 'T'):
        thank_you()
    elif (path.upper() == 'R'):
        generate_report()
    elif (path.lower == 'q' or path.lower() == 'quit'):
        quit()


def thank_you():
    donor = input("Please enter a donor name or choose from the following: \n"
                  "list - Print a list of previous donors\n"
                  "quit - Return to the main menu")
    if (donor.lower() == 'q' or donor.lower() == 'quit'):
        quit()
    elif (donor.lower() == 'l' or donor.lower() == 'list'):
        print("See below for a list of donors:")
        print(donor_name_list)
    elif (donor in donor_name_list):



def print_letter():
    """Prints email thanking donor for donation."""
    print("Dear %n,\n\n"
          "Thank you so much for your kind donation of $%d"
          "to the Foundation for Fruit.  We couldn't deliver "
          "our delicious friut to our friends in Finland without"
          "all of your help.\n\n"
          "We hope you will continue to make this foundation a top"
          "priority of yours for years to come.\n\n"
          "Best regards,\n"
          "Samantha Prince\n"
          "Founder")
