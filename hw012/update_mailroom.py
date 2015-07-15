donor_list = {
    'Margie DeBella': [100, 95],
    'Liz Rogers': [1000, 5000, 25],
    'Lisa Stokes': [800],
    'Fred Flinstone': [2000, 400, 1500]
}


def start_screen():
    """Opening screen to inform user of program options."""
    opener = "Welcome to Mailroom Madness"
    menu_option = """
    Choose from the following:\n
    T - Send a (T)hank You
    R - Create a (R)eport
    quit - Quit the program\n
    Input:  """

    print(opener)

    path = input(menu_option)
    check_valid_path(path)

    while path:
        path = input("Please enter from the selections below:\n" + menu_option)
        path = check_valid_path(path)


def check_valid_path(path):
    unvalid = True
    try:
        path = path.lower()
        if path == "q" or path == "quit":
            quit()
        elif path == "r":
            generate_report()
        elif path == "t":
            thankyou()
        else:
            return unvalid
    except TypeError:
        return unvalid


def thankyou():
    menu_option = """
    Please enter a name or choose from the following:\n
    list - Print a list of previous donors
    quit - Return to the main menu\n
    Input: """

    print(menu_option)

    donor = input()
    check_thankyou_path(donor)


def check_thankyou_path(donor):

    if donor.lower() == "quit":
        start_screen()
    elif donor.lower() == "list":
        print("See below for a list of donor names")
        print(donor_name_only())
        thankyou()
    try:
        if donor_list[donor]:
            donor_add(donor)
    except KeyError:
        donor_add(donor)


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
    start_screen()


def donor_name_only():
    """Prints list of donor names from dictionary."""
    for key in donor_list:
        print(key)


def donor_add(donor):
    """Add donor to database"""
    if donor not in donor_list:
        donor_list[donor] = []
        donation = donation_add(donor)
        while not isinstance(donation, float) or donation < 0:
            donation = donation_add(donor)

    donor_list[donor].append[donation]
    print_letter(donor, donation)


def donation_add(donor):
    """Adds amount of donation to donor donation list."""
    donation = input("What is the donation amount? ")
    try:
        return float(donation)
    except ValueError:
        print("Invalid! Please enter a number. ")
        return None


def print_letter(donor, donation):
    """Prints email thanking donor for donation."""
    str(donation)

    letter = ("""Dear %s,

    Thank you so much for your kind donation of $%s
    to the Chester County Fund for Women and Girls.

    Without your help, women and girls in Chester County would not
    thrive or live up to their fullest potential.

    We hope you will continue to make this foundation a top
    priority of yours for years to come.

    Best regards,
    Samantha Prince
    Grants Manager""" % (donor, donation))

    with open(donor + ".txt", "w") as f:
        f.write(letter)

    print(letter)
    # start_screen()


if __name__ == '__main__':

    start_screen()
