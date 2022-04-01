
class Employee:
    """
    A class used to represent an Employee

    ...

    Attributes
    ----------
    name : str
        the name of the employee
    """
    def __init__(self,name):
        """
        Parameters
        ----------
        name : str
            The name of the employee
        """
        self._name = name

    @property
    def name(self): 
        return self._name 
        
    @name.setter 
    def name(self, value): 
        self._workdays = value 

    def __hash__(self):
        return hash((self.name))

    def __eq__(self, other):
        if isinstance(other, Employee):
            return self.name == other.name
        return False 

    def __str__(self):
        return f'{self._name}'
        