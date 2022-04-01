"""
Class exceptions

"""
class WeekDaysException(Exception):
    
    def __init__(self, message):
        super().__init__(message)

class HourException(Exception):
    
    def __init__(self, message):
        super().__init__(message)

class PriceException(Exception):
    
    def __init__(self, message):
        super().__init__(message)

class FormatException(Exception):
    
    def __init__(self, message):
        super().__init__(message)
        