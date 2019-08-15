from datetime import datetime

VALID_START_DATE = datetime.strptime("01/01/1901", "%d/%m/%Y")
VALID_END_DATE = datetime.strptime("31/12/2999", "%d/%m/%Y")


class DateValueError(Exception):
    """Raised when the date value is not between 01/01/1901 and 31/12/2999"""
    pass


def get_date(date_str):
    """
    Splits experiment start and end dates from the string
    
    Arguments:
        date_str {str} -- string value with date value
    
    Returns:
        tuple -- return start and end date values
    """
    date_list = date_str.split("-")
    start_date, end_date = map(lambda x: x.strip(), date_list)
    return (start_date, end_date)


def get_elapsed_time(start_date, end_date):
    """
    Calculate elapsed time between two dates with the rules below
    1. if the date is not fully elapsed ex: 07/11/1972 and 08/11/1972 returns 0
    and 01/01/2000 to 03/01/2000 should return 1.
    
    Arguments:
        start_date {str} -- start date of the experiment
        end_date {str} -- end date of the experiment
    
    Raises:
        DateValueError: raises error, if the date value is not between 01/01/1901 and 31/12/2999
    
    Returns:
        int -- returns no of days between two dates
    """
    result = ""
    err_msg = "value is not between 01/01/1901 and 31/12/2999"
    start_date = datetime.strptime(start_date, "%d/%m/%Y")
    end_date = datetime.strptime(end_date, "%d/%m/%Y")

    if not ((start_date >= VALID_START_DATE) and (start_date <= VALID_END_DATE)):
        msg = f"Start date: {start_date} "
        raise DateValueError(msg + err_msg)
    elif not ((end_date >= VALID_START_DATE) and (end_date <= VALID_END_DATE)):
        msg = f"End date: {end_date} "
        raise DateValueError(msg + err_msg)

    diff = end_date - start_date

    if diff.days == 0:
        result = diff.days
    elif diff.days < 0:
        result = abs(diff.days + 1)
    else:
        result = diff.days - 1
    return result


def generator_data(args_obj):
    """
    Read content from file and yeild the elements
    
    Arguments:
        args_obj {object} -- Argument contains file path
    """
    with open(args_obj.file_path) as file_obj:
        for ele in file_obj.readlines():
            start_date, end_date = get_date(ele)
            response = get_elapsed_time(start_date, end_date)
            yield response


def process_data(args_obj):
    """
    Process data based on the input, its either file path which contains test date or date string    
    
    Arguments:
        args_obj {object} -- contains file path or date string
    
    Returns:
        int -- return no of days between experiment start and end date
    """
    try:
        msg = ""
        response_list = []
        if args_obj.file_path != "":
            for ele in generator_data(args_obj):
                print(ele)
        elif args_obj.exp_date != "":
            start_date, end_date = get_date(args_obj.exp_date)
            response = get_elapsed_time(start_date, end_date)
            print(response)
            return response
    except ValueError:
        msg = f"Date format is not correct, start end: {start_date}, end date: {end_date}"
        return msg
    except DateValueError as e:
        return e
