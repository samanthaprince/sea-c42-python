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
    else:
        print("Input not valid, please choose again.")
        start_screen()


donor_name_list = ['Margie DeBella', 'Liz Rogers', 'Lisa Stokes']

donor_donation_list = [[100, 95], [1000, 5000, 25000], [800]]


def thank_you():
    donor = input("Please enter a donor name or choose from the following: \n"
                  "list - Print a list of previous donors\n"
                  "return - Return to the main menu")
    if (donor.lower() == 'r' or donor.lower() == 'return'):
        start_screen()
    elif (donor.lower() == 'l' or donor.lower() == 'list'):
        print("See below for a list of donors:")
        print(donor_name_list)
    elif (donor in donor_name_list):
        donation_add()
    else:
        donor_name_list.extend([donor])
        donation_add()


def donation_add():
    amount = input("Please enter a donation amount or 'quit': ")
    if (amount.lower() == 'quit' or amount.lower == 'q'):
        start_screen()
    elif (amount.isnumeric() == True):
        donor_donation_list.append(['amount'])
    else:
        print("Please enter a number for the donation amount.")
        donation_add()


def print_letter():
    """Prints email thanking donor for donation."""
    print("Dear %n,\n\n"
          "Thank you so much for your kind donation of $%d "
          "to the Chester County Fund for Women and Girls."
          "Without your help, women and girls in Chester County would not"
          "thrive or live up to their fullest potential.\n\n"
          "We hope you will continue to make this foundation a top"
          "priority of yours for years to come.\n\n"
          "Best regards,\n"
          "Samantha Prince\n"
          "Grants Manager")
