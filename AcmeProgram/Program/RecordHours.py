from Parameterizers import  WorkdayParameterizer
from Validator import Validator

class RecordHours:
    """
    A class used to represent an Employees records

    ...

    Attributes
    ----------
    employee : Employee
        employee type object 
    day : datetime.datetime
        the day of the weekday
    init_time : str
        initial day
    final_time : int
        final day  
    payment : int
        Hour value based on the hour parameterizer.

    Methods
    -------
    getAmountPayment(self)
        Get hour value based on the hour parameterizer.
    """
    
    def __init__(self,employee,day, init_time, final_time):
        """
        Parameters
        ----------
        employee : Employee
            employee type object 
        day : datetime.datetime
            the day of the weekday
        init_time : str
            initial day
        final_time : int
            final day  
        payment : int
            Hour value based on the hour parameterizer.
        """
        self._employee = employee
        self._day = Validator._validate_day(day)
        self._init_time = Validator._validate_hour(init_time)
        self._final_time = Validator._validate_final_time(init_time,final_time)
        self._payment = self.getAmountPayment()
    
    @property
    def employee(self): 
        return self._employee 
         
    @employee.setter 
    def employee(self, value): 
        self._employee = value

    @property
    def day(self): 
        return self._day 
         
    @day.setter 
    def day(self, value): 
        self._day = Validator._validate_day(value) 
   
    @property
    def init_time(self): 
        return self._init_time 
         
    @init_time.setter 
    def init_time(self, value):    
        self._init_time = Validator._validate_hour(value) 
            
    @property
    def final_time(self): 
        return self._final_time 
         
    @final_time.setter 
    def final_time(self, value):
        self._final_time = Validator._validate_hour(value)

    @property
    def payment(self): 
        return self._payment
   
    def getHourWorked(self):
        return self._final_time - self._init_time

    def getAmountPayment(self):
        """Gets hour value based on the hour parameterizer.

        Returns
        -------
        totalPrice:
            Price of the hour based on the parameterizer.
        """    
        totalPrice = 0  
        for hour in range(self.init_time.hour,Validator._validate_final_hour(self._final_time.hour)):                 
            if(WorkdayParameterizer().workdays!=None):
                totalPrice += WorkdayParameterizer().findPrice(self.day,hour)         
        return totalPrice

    def __eq__(self, other):
            if isinstance(other, RecordHours):
                return self.employee == other.employee and self.day == other.day and self.init_time == other.init_time and self.final_time == other.final_time  and self.payment == other.payment
            return False 

    def __str__(self):
            return f'RecordHours: {self.employee} {self.init_time} {self.final_time} {self.payment}'