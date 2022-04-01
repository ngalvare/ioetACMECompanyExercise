from RecordHours import RecordHours

class PaymentRole:
    """
    A class used to represent a Payment Role

    ...

    Attributes
    ----------
    employee : Employee
        employee type object 
    payment : int
        Total value of the employee's payroll.

    Methods
    -------
    calculate_Payment(self,records)
        Get the total amount of the employee's payment.
    """
   
    def __init__(self, employee):
        self._employee = employee
        self._payment = 0

    @property
    def employee(self): 
        return self._employee 
     
    @employee.setter 
    def employee(self, employee): 
        self._employee = employee
    
    @property
    def payment(self): 
        return self._payment
       
    @payment.setter 
    def payment(self, payment): 
        self._payment= payment

    def calculate_Payment(self,records):
        """Get the total amount of the employee's payment.

        The method calculates based on all the employee's records
        how much is its value to pay and assigns it to the payment
        field of the object.

        Parameters
        ----------
        records : List
            List of all employee time stamps.
        """
        
        payment = 0
        for record in records:
            if isinstance(record, RecordHours):
                if(self.employee == record.employee):
                    payment += record.payment  
                          
        self.payment = payment
         
    def __eq__(self, other):
            if isinstance(other, PaymentRole):
                return self.employee == other.employee and self.payment == other.payment
            return False 

    def __str__(self):
        return f'The amount to pay {self.employee.name} is: {self.payment}'