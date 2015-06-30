def start_screen():
    """Opening screen to inform user of program options."""
    print("Welcome to Mailroom Madness\n")
    print("Choose from the following:\n")
    print("T - Send a (T)hank You")
    print("R - Create a (R)eport")
    print("quit - Quit the program\n")
    path = input("What would you like to do first?  ")
    if (path.upper() == 'T'):
        thank_you()
    elif (path.upper() == 'R'):
        generate_report()
    elif (path.lower == 'q' or path.lower() == 'quit'):
        quit()
    else:
        print("Input not valid, please choose again.")
        start_screen()


donor_list = {
    'Margie DeBella': [100, 95],
    'Liz Rogers': [1000, 5000, 25],
    'Lisa Stokes': [800],
    'Fred Flinstone': [2000, 400, 1500]
}


def thank_you():
    donor = input("Please enter a name or choose from the following: \n"
                  "list - Print a list of previous donors\n"
                  "quit - Return to the main menu :  ")
    if (donor.lower() == 'r' or donor.lower() == 'return'):
        start_screen()
    elif (donor.lower() == 'l' or donor.lower() == 'list'):
        print("See below for a list of donors: ")
        print(donor_list)
    elif (donor in donor_list):
        donation_add()
    else:
        donor_list.extend([donor])
        donation_add()
        print_letter()


def donation_add():
    """Adds amount of donation to donor donation list."""
    amount = input("Please enter a donation amount or 'quit': ")
    if (amount.lower() == 'quit' or amount.lower == 'q'):
        start_screen()
    elif (amount.isnumeric() == True):
        # Check how to get amount to the correct donor
        donor_list.append([amount])
    else:
        print("Please enter a number for the donation amount.")
        donation_add()


def print_letter():
    """Prints email thanking donor for donation."""
    print("Dear %s,\n\n"
          "Thank you so much for your kind donation of $%s \n"
          "to the Chester County Fund for Women and Girls.\n"
          "Without your help, women and girls in Chester County would not\n"
          "thrive or live up to their fullest potential.\n\n"
          "We hope you will continue to make this foundation a top\n"
          "priority of yours for years to come.\n\n"
          "Best regards,\n"
          "Samantha Prince\n"
          "Grants Manager")


def generate_report():
    print("Name \t\t|Total \t|# | Average\n" + ("_" * 40))
    for key in donor_list:
        donor_name = key
        total_donated = sum(donor_list[key])
        num_donate = len(donor_list[key])
        avg = total_donated / num_donate
        print('%s \t|$%d \t|%d | $%d' %
              (donor_name, total_donated, num_donate, avg))


start_screen()
