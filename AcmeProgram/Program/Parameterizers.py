from Validator import Validator


class Singleton(type):
    """
    A class used to represent a singleton design pattern

    ...

    Attributes
    ----------
    insance : str
        Instance of the object itself
    Methods
    -------
    __call__(cls, *args, **kwargs)
        managment instance of the object itself
    """
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]
    
class WorkdayParameterizer(metaclass = Singleton):
   """
   A class used to represent a workday parametrizer

   ...

   Attributes
   ----------
   workdays : List
      List of workdays
   Methods
   -------
   findPrice(self, dayE, hour)
      get the price of hour based on the hour parameterizer.
   """
   def __init__(self, workdays):
      """
        Parameters
        ----------
        workdays : List
         List of workdays
        """
      self.workdays = workdays
 
   def findPrice(self, dayE, hour): 
      """Get the price of an hour based on the hour parameterizer.

        The method receives the day the employee worked and the hour of work.

        Parameters
        ----------
        dayE : Weekdays
            The day the employee works.
        hour : datetime.datetime
            The time I need to evaluate to get price.

        return
        ------
        The standardized price of the range of hours to which the sent hour belongs
        """
      hour =  Validator._validate_hour_num(hour)  
      dayE = Validator._validate_day(dayE)
      if(self.workdays!=None):
         for workDay in self.workdays:  
            if(workDay.day == dayE):
               if(hour >= workDay.init_time.hour and  hour < Validator._validate_final_hour(workDay.final_time.hour)): 
                  return workDay.price