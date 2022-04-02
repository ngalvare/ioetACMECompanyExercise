# About The Project

### Goals
------------
The goal of this exercise is to calculate the total that the company has to pay an employee, according to the hours they worked and the times during which they worked. The prices of the hour ranges are define in the following table: 

```
Monday - Friday

00:01 - 09:00 25 USD
09:01 - 18:00 15 USD
18:01 - 00:00 20 USD

Saturday and Sunday
00:01 - 09:00 30 USD
09:01 - 18:00 20 USD
18:01 - 00:00 25 USD

```

The system recives the hours worked by an employee.This input should follow this format: 

```
RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00
```

The output is the total amount to pay the employee.

![image](https://user-images.githubusercontent.com/24533393/161355300-3fe652c5-c95a-4500-8121-18a77a2b3e7b.png)

### Getting Started
------------

##### Built With
  * [Python 3.9.12](https://www.python.org/downloads/release/python-3912/)
  * [unittest](https://docs.python.org/es/3.9/library/unittest.html)
  
##### Usage program
  * Clone the repository
  * Go inside the `Program` directory of the project 
  * Execute the command `python demo.py` 
  
    * The system will read a file with the prices for each hour range and load them in the parametrizer. Additionally,it will read the file with hours worked by the          employees and will show the salary of those employees. 

    * Hour range prices file       
        ![image](https://user-images.githubusercontent.com/24533393/161351631-07094c9c-9b28-4ea0-88d0-777055f7f36e.png)

    * Employees Records file
        ![image](https://user-images.githubusercontent.com/24533393/161351686-4000b44e-7050-44f5-942c-19cff9f6b6ae.png)

    * The amount(USD) to pay each employee as an output.
        ![image](https://user-images.githubusercontent.com/24533393/161355466-d28ce43a-ff72-4671-8c40-95250e7913b8.png)
  
##### Testing
  * Go inside the `Test` directory of the project 
  * Execute the command  `python -m unittest -v mainTest.py` to see detailed information.
    ![image](https://user-images.githubusercontent.com/24533393/161351890-e20ad91e-8ed7-4349-937f-9add304bd0a9.png)


### Methodology y Architecture
------------

##### Methodology
 *	Object Oriented Programming was used as a basis for the system
 *	The objects represent the next elements in the system:
    *  Employee
    *	 Hours record of each employee
    *	 Payment role
    *	 Working day
 *	The hour range is defined by the company, therefore an hour parameterizer was built to receive the hours with the price of each range. The parameterizer was  created using a singleton pattern design. The reason for this is that only one instance of the object will be used throughout the execution of the system.
 *	A Validator class was built to verify the correct format of primordial data like:
    *	Day
    *	Start date
    *	Finish date
    *	Price
 *	All the possible exceptions are defined and managed inside the Exceptions file.

##### Architecture

![UML Software](https://user-images.githubusercontent.com/24533393/161349835-9de4cfd9-da55-4640-8e9f-9408547db76d.png)


 ### Project Organization
------------

    ├── README.md          <- The top-level README for developers using this project.
    ├── AcmeProgram        
        ├── Fields
            └── WorkDays   <- File with the hour ranges and the prices
            └── Examples   <- File with the employee records
        ├── Program        
              ├── Test     <- Testing directory
                └── mainTest.py             <- Main test
                └── parameterizers_test.py  <- Test for the parameterizer
                └── paymentRole_test.py     <- Test for the payment calculation     
            └── DataManagment.py            <- Class for file reading
            └── demo.py<- main del sistema  <- Main execution file
            └── Employee.py                 <- Employee class
            └── Exceptions.py               <- Exception file with exceptions classes
            └── Parameterizers.py           <- Parameterizer Class
            └── PaymentRole.py              <- PaymentRol class
            └── RecordHours.py              <- Record Hour class
            └── Validator.py                <- Validor file
            └── Weekdays.py                 <- Weekdays Enum
            └── Workday.py                  <- WorkDay class
-------
