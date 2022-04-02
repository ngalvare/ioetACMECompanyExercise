from DataManagment import DataManagment
from PaymentRole import PaymentRole 
from Parameterizers import WorkdayParameterizer

"""Demo Acme Company

This script allows the company to calculate the total pay for employees company,
 based on the hours they worked and the times during which they worked.

This program needs the Workdays price of value range per hour and employee records
"""

workdays = DataManagment._read_file_parametrizer('../Fields/WorkDays.txt')
database = WorkdayParameterizer(workdays)

data_employees,inputs = DataManagment._read_file_records('../Fields/Examples.txt')

i,y = 0,0
for employee in data_employees:
      payment =  PaymentRole(employee) 
      payment.calculate_Payment(data_employees[employee])
      i +=1
      print(f'Case {i}:\n\n{employee}\n\nINPUT:\n{inputs[y]}\n\nOUTPUT:\n{payment} USD\n')
      y +=1