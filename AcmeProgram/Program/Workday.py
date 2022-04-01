from Validator import Validator

class Workday:
    """
    A class used to represent an Workday

    ...

    Attributes
    ----------
    day : Weekdays
        the day of the week
    init_time : datetime.datetime
        initial date
    final_time : datetime.datetime
        final time
    price : float
        price
    
    """
    def __init__(self,day, init_time, final_time, price):
        """
        Parameters
        ----------
        day : Weekdays
            the day of the week (Enum value)
        init_time : datetime.datetime
            initial date
        final_time : datetime.datetime
            final time
        price : float
            price
        """
        self._day = Validator._validate_day(day)
        self._init_time = Validator._validate_hour(init_time)
        self._final_time = Validator._validate_final_time(init_time,final_time)
        self._price = Validator._validate_price(price)
    
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
    def price(self): 
        return self._price 
        
    @price.setter 
    def price(self, value): 
        self._price = Validator._validate_price(value)

    def __eq__(self, other):
        if isinstance(other, Workday):
            return self.day == other.day and self.init_time == other.init_time and self.final_time == other.final_time
        return False  
      
    def __str__(self):
        return f'WorkDay: {self.day} {self.init_time} {self.final_time} {self.price}'