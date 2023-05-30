def custom_date_imputer(input_date: str):
    """
    Custom imputer of date formats
    Example:
    "18 Sep 2018" -> "18 Sep 2018" (no change)
    "Apr 2020" -> "1 Apr 2020" (first day of month imputed if not available by default)

    :param input_date: date in string representation, format "18 Sep 2018" or "Sep 2018"
    :return: date in string representation with day in month imputed if not available by default, format "18 Sep 2018"
    """

    day_and_month_and_year_present = False
    only_month_and_year_present = False

    # custom date parser
    words = input_date.split()
    numbers = [word for word in words if word.isdigit()]
    digits = [len(number) for number in numbers]
    digit_storage = dict(zip(numbers, digits))
    month = [word for word in words if not word.isdigit()][0]

    # check if day is provided in input date
    if len(numbers) == 2:
        day_and_month_and_year_present = True
    elif len(numbers) == 1:
        only_month_and_year_present = True

    # day is available
    if day_and_month_and_year_present:
        return input_date
    # day is not available
    elif only_month_and_year_present:
        for number, digits in digit_storage.items():
            if digits == 4:
                year = number
        day = '1' # if day is not provided, first day in the month is imputed
        output_date = day + ' ' + month + ' ' + year
        return output_date
    # different format than expected
    else:
        return input_date