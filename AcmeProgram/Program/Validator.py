
from Exceptions import WeekDaysException, HourException, PriceException, FormatException
from Weekdays import WeekDays
from datetime import datetime
import re

class Validator:

    '''Validator if day is a week day'''

    @staticmethod
    def _validate_day(day): 
        """Valid if one day is correct

        The method based on the Weekdays enum validates if a day is correct or not.

        Parameters
        ----------
        day : str
            Day that is required to evaluate.
        Raises
        ------
        WeekDaysException
            If that day is not found among the days of the enum.
        """ 

        day =  day.upper() 
        if day in list(WeekDays._member_names_):   
            return day
        else:
            raise WeekDaysException(f'{day} It is not a day of the week!')

    @staticmethod   
    def _validate_hour_num(hour_num):              
        """Validate if an hour is correct

        Based on an integer, it is validated if it is between 0 and 24.  

        Parameters
        ----------
        hour_num : int
            Hour required to evaluate.
        Raises
        ------
        HourException
            If the time entered is not between 0 and 24.
        """ 
        hour_num = int(hour_num)
        if(hour_num>=0 and hour_num<=23):
             return hour_num
        else:
             raise HourException(f'The hour {hour_num} is not valid!')
         
    @staticmethod   
    def _validate_hour(hour): 
        """Validate if the time format is correct.

        The method validates if the entered string is a correct time.  

        Parameters
        ----------
        hour : str
            str that is required to evaluate and convert to time.
        Raises
        ------
        HourException
            If the entered hour does not exist.
        """              
        try:
            hour = datetime.strptime(hour,'%H:%M')
        except:
            raise HourException(f'The {hour} does not exist!')
        return hour

    @staticmethod
    def _validate_price(price): 
        """Valid if the price is not negative.

        The method validates if an entered price is not negative. 

        Parameters
        ----------
        price : int
            Integer that is required to evaluate.
        Raises
        ------
        PriceException
            If the entered price is negative.
        """     
        price = int(price)
        if(price >=0):
             return price
        else:
             raise PriceException(f'The negative prices does not exist!')
         
    @staticmethod
    def _validate_final_hour(hour):
        """Valid if the end hour is 0.

        The method validate if an hour is 0 and change it to 24.

        Parameters
        ----------
        hour : int
            Hour you want to change to 24.
        """   
        hour = int(hour)
        if(hour==0):
             return 24
        else:
             return hour

    @staticmethod
    def _validate_final_time(init_time,final_time):
        """Valid if the end date is less than the start date.

        The method validates if the date range is correct.

        Parameters
        ----------
        init_time : datetime.datetime
            initial date
        init_time : datetime.datetim
            final date
        Raises
        ------
        HourException
            If the end date is less than the start date.
        """ 
             
        final_tim = Validator._validate_hour(final_time)
        init_hour = Validator._validate_hour(init_time).hour
        final_hour = final_tim.hour
        
        if(init_hour < Validator._validate_final_hour(final_hour)):
             return final_tim
        else:
             raise HourException(f'The date: {init_time} is less than the date: {final_time}')

    @staticmethod
    def _validate_format_file(line):  
        """Validate the format of a line is correct.

        The method validates if the line complies with the format of the parameterizer file.

        Parameters
        ----------
        line : str
            Line that needs to be evaluated.
        Raises
        ------
        FormatException
            If the line does not comply with the format.
        """
        r = re.compile(r'[a-zA-Z]*=([a-zA-Z]{2}[0-9]{2}:[0-9]{2}-[0-9]{2}:[0-9]{2},?)+')       
        if r.match(line) is not None:
            return line
        else:
            raise FormatException(f'{line} should be [Employee]=[Day][Hour:Min]:[Hour:Min]') 

    @staticmethod
    def _validate_format_parametrizer(line):  
        """Validate the format of a line is correct.

        The method validates if the line complies with the format of the employee record file.

        Parameters
        ----------
        line : str
            Line that needs to be evaluated.
        Raises
        ------
        FormatException
            If the line does not comply with the format.
        """
        r = re.compile(r'[a-zA-Z]{2}-[0-9]{2}:[0-9]{2}-[0-9]{2}:[0-9]{2}-[0-9]*')     
        if r.match(line) is not None:
            return line
        else:
            raise FormatException(f'[Day]-[Hour:Min]-[Hour:Min]-[Price]') 