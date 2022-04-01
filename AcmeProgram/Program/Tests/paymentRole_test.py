import unittest
import sys
sys.path.append('../')

from DataManagment import DataManagment
from Parameterizers import WorkdayParameterizer
from RecordHours import RecordHours
from Employee import Employee
from PaymentRole import PaymentRole 
from Exceptions import WeekDaysException, HourException


class PaymentRoleTestCase(unittest.TestCase):

    '''Employee Payment Amount Test Case'''

    def setUp(self):     
        workdays = DataManagment._read_file_parametrizer('WorkDays.txt')
        WorkdayParameterizer(workdays)  
        self.employee = Employee('MICHAEL')  

    '''
    * Scenario: Weekday
    - Monday 00:01 - 09:00 
    * Expect Result: 225 USD
    '''
    def test_findPrice_weekday_00_09(self):
        records  = [RecordHours(self.employee,'MO','00:01','09:00')]
        payment_role  = PaymentRole(self.employee)        
        payment_role.calculate_Payment(records)
        self.assertEqual(payment_role.payment, 225)

    '''
    * Scenario: Weekday  
    - Monday 09:01 - 18:00 
    * Expect Result: 135 USD
    '''
    def test_findPrice_weekday_09_18(self):
        records  = [RecordHours(self.employee,'MO','09:01','18:00')]
        payment_role  = PaymentRole(self.employee)        
        payment_role.calculate_Payment(records)
        self.assertEqual(payment_role.payment, 135)

    '''
    * Scenario: Weekday 
    - Monday 18:01 - 00:00 
    * Expect Result: 120 USD
    '''
    def test_findPrice_weekday_18_00(self):
        records  = [RecordHours(self.employee,'MO','18:01','00:00')]
        payment_role  = PaymentRole(self.employee)        
        payment_role.calculate_Payment(records)
        self.assertEqual(payment_role.payment, 120)
    
    '''
    * Scenario: Weekend
    - Saturday 00:01 - 09:00 
    * Expect Result: 270 USD
    '''
    def test_findPrice_weekend_00_09(self):
        records  = [RecordHours(self.employee,'SA','00:01','09:00')]
        payment_role  = PaymentRole(self.employee)        
        payment_role.calculate_Payment(records)
        self.assertEqual(payment_role.payment, 270)

    '''
    * Scenario: Weekend  
    - Saturday 09:01 - 18:00 
    * Expect Result: 180 USD
    '''
    def test_findPrice_weekend_09_18(self):
        records  = [RecordHours(self.employee,'SA','09:01','18:00')]
        payment_role  = PaymentRole(self.employee)        
        payment_role.calculate_Payment(records)
        self.assertEqual(payment_role.payment, 180)

    '''
    * Scenario: Weekend 
    - Saturday 18:01 - 00:00 
    * Expect Result: 150 USD
    '''
    def test_findPrice_weekend_18_00(self):
        records  = [RecordHours(self.employee,'SA','18:01','00:00')]
        payment_role  = PaymentRole(self.employee)        
        payment_role.calculate_Payment(records)
        self.assertEqual(payment_role.payment, 150)
    
    '''
    * Scenario: Weekday and Weekend 
    - Saturday -01:01 - 09:00 
    * Expect Result: HourException
    '''
    def test_findPrice_invalid_low(self):         
        with self.assertRaises(HourException):
            records  = [RecordHours(self.employee,'SA','-01:01','09:00')]
            payment_role  = PaymentRole(self.employee) 
            payment_role.calculate_Payment(records)
    
    '''
    * Scenario: Weekday and Weekend 
    - Saturday 18:01 - 25:00 
    * Expect Result: HourException
    '''
    def test_findPrice_invalid_hour_great(self):         
        with self.assertRaises(HourException):
            records  = [RecordHours(self.employee,'SU','18:01','25:00')]
            payment_role  = PaymentRole(self.employee) 
            payment_role.calculate_Payment(records)

    '''
    * Scenario: Weekday
    - Friday 07:00 - 12:00 
    * Expect Result: 95 USD
    '''
    def test_findPrice_friday_07_12(self):         
        records  = [RecordHours(self.employee,'FR','07:00','12:00')]
        payment_role  = PaymentRole(self.employee)        
        payment_role.calculate_Payment(records)
        self.assertEqual(payment_role.payment, 95)
                
    '''
    * Scenario: Weekday
    - Friday 15:00 - 20:00 
    * Expect Result: 85 USD
    '''
    def test_findPrice_friday_15_20(self):         
        records  = [RecordHours(self.employee,'FR','15:00','20:00')]
        payment_role  = PaymentRole(self.employee)        
        payment_role.calculate_Payment(records)
        self.assertEqual(payment_role.payment, 85)

    '''
    * Scenario: Weekday
    - Friday 04:00 - 22:00 
    * Expect Result: 340 USD
    '''
    def test_findPrice_friday_04_22(self):         
        records  = [RecordHours(self.employee,'FR','04:00','22:00')]
        payment_role  = PaymentRole(self.employee)        
        payment_role.calculate_Payment(records)
        self.assertEqual(payment_role.payment, 340)

    '''
    * Scenario: Invalid Day
    * Expect Result: WeekDaysException
    '''
    def test_findPrice_invalid_day(self):         
        with self.assertRaises(WeekDaysException):
            records  = [RecordHours(self.employee,'L','18:01','25:00')]
            payment_role  = PaymentRole(self.employee) 
            payment_role.calculate_Payment(records)