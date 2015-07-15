def start_screen():
    """Opening screen to inform user of program options."""
    print("Welcome to Mailroom Madness\n")
    print("Choose from the following:\n")
    print("T - Send a (T)hank You")
    print("R - Create a (R)eport")
    print("quit - Quit the program\n")


donor_list = {
    'Margie DeBella': [100, 95],
    'Liz Rogers': [1000, 5000, 25],
    'Lisa Stokes': [800],
    'Fred Flinstone': [2000, 400, 1500]
}


def generate_report():
    """Generates a report for user with key information
       still doesn't print sorted"""
    print("Name \t\t|Total \t|# | Average\n" + ("_" * 40))
    sorted_list = sorted(donor_list, key=lambda donor: sum(donor_list[donor]),
                         reverse=True)
    for key in sorted_list:
        donor_name = key
        total_donated = sum(donor_list[key])
        num_donate = len(donor_list[key])
        avg = total_donated / num_donate
        print('%s \t|$%d \t|%d | $%d' %
              (donor_name, total_donated, num_donate, avg))
    return False


def donor_name_only():
    """Prints list of donor names from dictionary."""
    for key in donor_list:
        print(key)


def donor_add(donor, amount):
    """Add donor to database"""
    donor_list[donor] = [amount]


def donation_add(donor, amount):
    """Adds amount of donation to donor donation list."""
    donor_list[donor].append(amount)


def print_letter(donor, amount):
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
          "Grants Manager" % (donor, amount))


if __name__ == '__main__':

    start_screen()
    path = input("What would you like to do first?  ")

    if (path.upper() == 'R'):
        generate_report()

    elif (path.upper() == 'T'):
        donor = input("Please enter a name or choose from the following: \n"
                      "list - Print a list of previous donors\n"
                      "quit - Return to the main menu :  ")
        amount = int(input("Please enter a donation amount or 'quit': "))
        if (donor.lower() == 'q' or donor.lower() == 'quit'):
            start_screen()

        elif (donor.lower() == 'l' or donor.lower() == 'list'):
            print("See below for a list of donors: ")
            print(donor_name_only())

        else:
            name_in_list = False
            for key in donor_list:
                if donor == key:
                    name_in_list = True
                    break
                else:
                    name_in_list = False

        if (name_in_list is True):
            donation_add(donor, amount)
            print_letter(donor, amount)
        else:
            donor_add(donor, amount)
            donation_add(donor, amount)
            print_letter(donor, amount)

    elif (path.lower == 'q' or path.lower() == 'quit'):
        quit()
