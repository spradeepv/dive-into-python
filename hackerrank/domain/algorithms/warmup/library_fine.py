def calculate_fine(actual_date, expected_date):
    """
    Problem Statement

        The Head Librarian at a library wants you to make a program that
        calculates the fine for returning the book after the return date. You
        are given the actual and the expected return dates. Calculate the fine
        as follows:

        If the book is returned on or before the expected return date, no fine
        will be charged, in other words fine is 0.

        If the book is returned in the same month as the expected return date,
        Fine = 15 Hackos × Number of late days

        If the book is not returned in the same month but in the same year as
        the expected return date, Fine = 500 Hackos × Number of late months

        If the book is not returned in the same year, the fine is fixed at
        10000 Hackos.

    Input Format
        You are given the actual and the expected return dates in D M Y format
        respectively. There are two lines of input. The first line contains the
        D M Y values for the actual return date and the next line contains the
        D M Y values for the expected return date.

    Constraints
        1?D?31
        1?M?12
        1?Y?3000
        Output Format

    Output a single value equal to the fine.

    Sample Input
        9 6 2015
        6 6 2015

    Sample Output
        45
    :param actual_date: Actual return date as string
    :param expected_date: Expected return date as string
    :return: Fine as integer
    """
    actual = map(int, actual_date.split(" "))
    expected = map(int, expected_date.split(" "))
    actual_day, actual_month, actual_year = actual[0], actual[1], actual[2]
    expected_day, expected_month, expected_year = (expected[0], expected[1],
                                                   expected[2])
    if actual_year > expected_year:
        return 10000
    elif actual_year == expected_year and actual_month > expected_month:
        diff_months = actual_month - expected_month
        return 500 * diff_months
    elif (actual_year == expected_year and actual_month == expected_month
          and actual_day > expected_day):
        diff_days = actual_day - expected_day
        return 15 * diff_days
    else:
        return 0

actual_date = raw_input()
expected_date = raw_input()
print(calculate_fine(actual_date, expected_date))

