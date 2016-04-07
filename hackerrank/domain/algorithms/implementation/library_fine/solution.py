def calculate_fine(actual_date, expected_date):
    actual = map(int, actual_date.split(" "))
    expected = map(int, expected_date.split(" "))
    actual_day, actual_month, actual_year = actual[0], actual[1], actual[2]
    expected_day, expected_month, expected_year = expected[0], expected[1], expected[2]
    if actual_year > expected_year:
        return 10000
    elif actual_year == expected_year and actual_month > expected_month:
        diff_months = actual_month - expected_month
        return 500 * diff_months
    elif actual_year == expected_year and actual_month == expected_month and actual_day > expected_day:
        diff_days = actual_day - expected_day
        return 15 * diff_days
    else:
        return 0

actual_date = raw_input()
expected_date = raw_input()
print(calculate_fine(actual_date, expected_date))

