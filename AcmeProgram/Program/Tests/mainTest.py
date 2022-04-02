import unittest
from parameterizers_test import ParameterizersTestCase
from paymentRole_test import PaymentRoleTestCase

'''
    Testing Cases
'''
suite = unittest.TestSuite()
runner = unittest.TextTestRunner()
runner.run(suite)