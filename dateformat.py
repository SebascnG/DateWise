from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
import pandas as pd


def identify_date_format(date):
    formats = [
        "%Y-%m-%d",
        "%m-%d-%Y",
        "%Y/%m/%d",
        "%d-%m-%Y",
        "%Y.%m.%d",
        "%m/%d/%Y",
        "%d/%m/%Y",
        "%Y %m %d",
        "%m %d %Y",
        "%d %m %Y",
        "%Y:%m:%d",
        "%m:%d:%Y",
        "%d:%m:%Y",
        "%Y %m %d %H:%M:%S",
        "%Y %m %d %H:%M",
        "%Y %m %d %H",
        "%Y %m %d %I:%M:%S %p",
        "%Y %m %d %I:%M %p",
        "%Y %m %d %I %p",
        "%d/%m/%Y %H:%M:%S",
        "%d/%m/%Y %H:%M",
        "%d/%m/%Y %H",
        "%d/%m/%Y %I:%M:%S %p",
        "%d/%m/%Y %I:%M %p",
        "%d/%m/%Y %I %p",
        "%Y-%m-%dT%H:%M:%S",
        "%Y-%m-%dT%H:%M",
        "%Y-%m-%dT%H",
        "%Y-%m-%dT%H:%M:%S.%f",
        "%Y-%m-%dT%H:%M:%S %Z",
        "%Y-%m-%dT%H:%M %Z",
        "%Y-%m-%dT%H %Z"
    ]

    for fmt in formats:
        try:
            datetime.strptime(date, fmt)
            return fmt
        except ValueError:
            pass
    return "Unknown"


def date_comparison(date1=None, date2=None, operation=None):

    if date1 and date2 and operation:

        date1_comparison = datetime.strptime(date1, identify_date_format(date=date1)) 

        date2_comparison = datetime.strptime(date2, identify_date_format(date=date2)) 

        if operation == "==":

            return date1_comparison == date2_comparison
        
        elif operation == "<":

            return date1_comparison < date2_comparison
        
        elif operation == "<=":

            return date1_comparison <= date2_comparison
        
        elif operation == ">":

            return date1_comparison > date2_comparison
        
        elif operation == ">=":

            return date1_comparison >= date2_comparison


def week_start(date:any):

    if isinstance(date, str):

        fmt = identify_date_format(date)

        weekday = datetime.strptime(date, fmt).weekday()

        week_start = (datetime.strptime(date, fmt) - timedelta(days=weekday)).strftime(fmt)

        return week_start
    

def week_end(date:any, weekend:bool):
    
    if isinstance(date, str):

        fmt = identify_date_format(date)

        weekday = datetime.strptime(date, fmt).weekday()

        if weekend == False:

            if weekday < 4:   

                week_end = (datetime.strptime(date, fmt) + timedelta(days=4 - weekday)).strftime(fmt)
                return(f'Business Week ends: {week_end}')

            else:

                return('Businees Week has already ended.')

        elif weekend == True:

            if weekday < 6:   

                week_end = (datetime.strptime(date, fmt) + timedelta(days=6 - weekday)).strftime(fmt)
                return(f'Full Week ends: {week_end}')

            else:

                return('Today is the end of the week.')


def date_operations(date:any, operation:str, format:str, range:int, weekend:bool):

    if date and operation and range:

        if isinstance(date, str):

            fmt = identify_date_format(date)

            weekday = datetime.strptime(date, fmt).weekday()

            date = datetime.strptime(date, fmt)

            if format == 'day':

                if weekend == False:

                    if operation == '+' : 

                        weekday = date.weekday()

                        while range: 

                            if range and weekday <= 3 or weekday >= 6:

                                date += timedelta(days=1)
                                weekday = date.weekday()
                                range -= 1
                            
                            else:
                                
                                date += timedelta(days=1)
                                weekday = date.weekday()

                        return(f'Added date without weekend: {date.strftime(fmt)}')
                        
                    elif operation == '-':

                        weekday = date.weekday()

                        while range: 

                            if range and weekday <= 5 and weekday >= 1:

                                date -= timedelta(days=1)
                                weekday = date.weekday()
                                range -= 1
                            
                            else:
                                
                                date -= timedelta(days=1)
                                weekday = date.weekday()


                        return(f'Subtracted date without weekend: {date.strftime(fmt)}')

                elif weekend == True:

                    if operation == '+' : 

                        while range: 

                            date += timedelta(days=1)
                            range -= 1

                        return(f'Added date with weekend: {date.strftime(fmt)}')
                        
                    elif operation == '-':

                        while range:

                            date -= timedelta(days=1)
                            range -= 1
                            
                        return(f'Subtracted date without weekend: {date.strftime(fmt)}')
            
            elif format == 'month':

                year = int(date.year)
                month = int(date.month)
                day = int(date.day)

                if operation == '+':

                    month += range

                    while month > 12:

                        month -= 12
                        year += 1

                    date = datetime(year=year, month=month, day=day)

                    return(f'Added date: {date.strftime(fmt)}') 
                
                elif operation == '-':

                    month -= range

                    while month <= 0:

                        month += 12
                        year -= 1
                        

                    date = datetime(year=year, month=month, day=day)

                    return(f'Subtracted date: {date.strftime(fmt)}')
                
            elif format == 'year':

                year = int(date.year)
                month = int(date.month)
                day = int(date.day)

                if operation == '+':

                    year += range
                    
                    date = datetime(year=year, month=month, day=day)

                    return(f'Added date: {date.strftime(fmt)}')
                
                elif operation == '-':

                    year -= range
                    
                    date = datetime(year=year, month=month, day=day)

                    return(f'Subtracted date: {date.strftime(fmt)}')                    

                
def range_calculation(start:any, end:any, weekend:bool, frequency:str) -> list:

    """
    Working only with string right now, pandas and datetime conditions need to be implemented

    parameters:

    >>>> start: begining of the date range 
    >>>> end: begining of the date range 
    >>>> weekend: 
    >>>> frequency: <day, month, year>
    """

    if start and end: 

        start_type = type(start)
        end_type = type(start)

        if start_type and end_type == str: 

            if date_comparison(end, start, '>'):
                max_date = start
                min_date = end
            else:
                max_date = end
                min_date = start

            max_format = identify_date_format(start)
            max_date = datetime.strptime(start, max_format)

            min_format = identify_date_format(end)
            min_date = datetime.strptime(end, min_format)

            days_between = []

            if weekend:

                while max_date != min_date + timedelta(days=1):

                    max_date -= timedelta(days=1)
                    days_between.append(max_date.strftime(max_format))
                
                output = f'Days between two dates are: {days_between}'

            else:

                while max_date != min_date + timedelta(days=1):

                    max_date -= timedelta(days=1)
                    if max_date.weekday() < 5:
                        days_between.append(max_date.strftime(max_format))
                    else:
                        pass

                output =  f'Business days between two dates are: {days_between}'

            if frequency == 'day':

                return f'Difference between two dates is {output} day(s).'
            
            elif frequency == 'week':

                week_difference = len(days_between) / 7

                if type(week_difference) != int:

                    weeks = int(week_difference)
                    days = len(days_between) % 7

                return f"Difference between two dates is {weeks} week(s) and {days} days. If you want to see specific dates, switch to format='day'"

            elif frequency == 'month':

                month_difference = len(days_between) / 30

                if type(month_difference) != int:

                    months = int(month_difference)
                    days = len(days_between) % 30

                return f"Difference between two dates is {months} month(s) and {days} days. If you want to see specific dates, switch to format='day'"
            
            elif frequency == 'quarter':

                quarter_difference = len(days_between) / 90

                if type(quarter_difference) != int:

                    quarters = int(quarter_difference)
                    days = len(days_between) % 90

                return f"Difference between two dates is {quarters} quarter(s) and {days} days. If you want to see specific dates, switch to format='day'"
            
            elif frequency == 'year':

                year_difference = len(days_between) / 365

                if type(year_difference) != int:

                    years = int(year_difference)
                    days = len(days_between) % 365

                return f"Difference between two dates is {years} year(s) and {days} days. If you want to see specific dates, switch to format='day'"

    else:

        print('Missing mandatory variable.')

    return f'Days between two dates are: {days_between}'


def date_convert(date:any, desired_type:str, format:str):
    
    date_type = str(type(date)).split("'")[1]

    desired_result = date_type + '-' + desired_type

    conversions = {
        'str-pandas'                 : pd.to_datetime(date) if isinstance(date, str) else None, 
        'str-datetime'               : datetime.strptime(date, format) if isinstance(date, str) else None,
        'pandas-str'                 : date.strftime(format) if isinstance(date, pd._libs.tslibs.timestamps.Timestamp) else None,
        'pandas-datetime'            : date.to_pydate(date) if isinstance(date, pd._libs.tslibs.timestamps.Timestamp) else None,
        'datetime.datetime-str'      : date.strftime(format) if isinstance(date, datetime) else None,
        'datetime.datetime-pandas'   : pd.Timestamp(date).strftime(format) if isinstance(date, datetime) else None
    }

    if date_type == desired_type:
        return 'Your date is in desired format'
    else:
        return conversions[desired_result]






car = date_operations('2024-03-13', '+', 'day', 3, False)
print(car)

