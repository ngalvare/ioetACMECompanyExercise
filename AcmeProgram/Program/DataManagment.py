from email import message
from Validator import Validator
from RecordHours import RecordHours
from Workday import Workday
from Employee import Employee 
from Exceptions import WeekDaysException, HourException, PriceException, FormatException
import sys 


class DataManagment:

    """
    A class used to managment data

    ...

    Methods
    -------
    _read_file_records(filename)
        Read the register of employees data.
    
    _read_file_parametrizer(filename)
        Read the data for the Workday parameterizer.
    """

    @staticmethod
    def _read_file_records(filename):  
        """Read the register of employees data.

        Parameters
        ----------
        filename : file name
        """
        try:               
            dataEmployees = {}
            inputs = []
            with open(filename) as f:

                lines = f.readlines()
                
                for line in lines:
                    inputs.append(line)
                    data = Validator._validate_format_file(line.strip()).split('=')
                    name = data[0]
                    employee = Employee(name)
                    
                    records = []
                    work_days = data[1].split(',')
                    for work_day in work_days:
                        day = work_day[:2]
                        times = work_day[2:].split('-')
                        init_time = times[0]
                        final_time = times[1]
                        record = RecordHours(employee, day, init_time, final_time)
                        if(record!=None):
                            records.append(record)
                    
                    dataEmployees[employee] = records
                
            return dataEmployees,inputs

        except WeekDaysException as e :
            print(f'Register Exception: {e} ')
         
        except HourException as h:
            print(f'Register Exception: {h} ')
        
        except FormatException as f:
            print(f'Register Exception: {f}. ')

            
    @staticmethod
    def _read_file_parametrizer(filename):  
        """Read the data for the Workday parameterizer.

        Parameters
        ----------
        filename : file name
        """
        try:
            
            workdays = []
            with open(filename) as f:
                lines = f.readlines()
                
                for line in lines:
                    data = Validator._validate_format_parametrizer(line).split('-')
                    name = data[0]
                    init_time = data[1]
                    final_time = data[2]
                    price = int(data[3])
                    workday =  Workday(name, init_time, final_time, price)
                    workdays.append(workday)

            return workdays

        except PriceException as p:
           sys.exit(f'Parametrizer Exception: {p}')   

        except FormatException as f:
            sys.exit(f'Parametrizer Exception: {f}') 

        except WeekDaysException as e :
            sys.exit(f'Parametrizer Exception: {e}') 
         
        except HourException as h:
            sys.exit(f'Parametrizer Exception: {h}')      