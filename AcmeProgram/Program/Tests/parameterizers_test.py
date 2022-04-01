import unittest
import sys
sys.path.append('../')

from DataManagment import DataManagment
from Parameterizers import WorkdayParameterizer
from Exceptions import WeekDaysException,HourException


class ParameterizersTestCase(unittest.TestCase):

   '''WeekDays and WeekEnds Prices Test Cases'''

   def setUp(self):     
      workdays = DataManagment._read_file_parametrizer('WorkDays.txt')
      WorkdayParameterizer(workdays)   
       
   '''
   * Scenario: Weekday 00:01 - 09:00
      -  hour: 2
   * Expect Result: 25 USD
   '''
   def test_findPrice_weekday_2(self):   
      price = WorkdayParameterizer().findPrice('TU',2)
      self.assertEqual(price, 25)

   '''
   * Scenario: Weekday 09:01 - 18:00
      -  hour: 12
   * Expect Result: 15 USD
   '''
   def test_findPrice_weekday_12(self):   
      price = WorkdayParameterizer().findPrice('WE',12)
      self.assertEqual(price, 15)

   '''
   * Scenario: Weekday 18:01 - 00:00
      -  hour: 21
   * Expect Result: 20 USD
   '''
   def test_findPrice_weekday_21(self):   
      price = WorkdayParameterizer().findPrice('TH',21)
      self.assertEqual(price, 20)

   '''
   * Scenario: Weekend 00:01 - 09:00
      -  hour: 2
   * Expect Result: 30 USD
   '''
   def test_findPrice_weekend_2(self):   
      price = WorkdayParameterizer().findPrice('SU',2)
      self.assertEqual(price, 30)

   '''
   * Scenario: Weekend 09:01 - 18:00
      -  hour: 12
   * Expect Result: 20 USD
   '''
   def test_findPrice_weekend_12(self):   
      price = WorkdayParameterizer().findPrice('SA',12)
      self.assertEqual(price, 20)

   '''
   * Scenario: Weekend 18:01 - 00:00
      -  hour: 21
   * Expect Result: 25 USD
   '''
   def test_findPrice_weekend_21(self):   
      price = WorkdayParameterizer().findPrice('Su',21)
      self.assertEqual(price, 25)

   '''
   * Scenario: Invalid Hour
      -  hour: -19
   * Expect Result: HourException
   '''
   def test_findPrice_negative(self):      
      with self.assertRaises(HourException):
            price = WorkdayParameterizer().findPrice('SU',-19)

   '''
   * Scenario: Invalid Hour
      -  hour: 27
   * Expect Result: HourException
   '''
   def test_findPrice_great(self):      
      with self.assertRaises(HourException):
            price = WorkdayParameterizer().findPrice('FR',27)

   '''
   * Scenario: Invalid Day
      -  Day: 'N'
   * Expect Result: HourException
   '''
   def test_findPrice_day(self):      
      with self.assertRaises(WeekDaysException):
            price = WorkdayParameterizer().findPrice('N',2)