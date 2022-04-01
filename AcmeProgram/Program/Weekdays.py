from enum import Enum, unique

"""
    Enum to standardize the days of the week
    according to their first two acronyms 
""" 

@unique
class WeekDays(Enum):
    MO = 1
    TU = 2
    WE = 3
    TH = 4
    FR = 5
    SA = 6
    SU = 7