import unittest
from parameterizers_test import ParameterizersTestCase
from paymentRole_test import PaymentRoleTestCase


loader = unittest.TestLoader()
suite = unittest.TestSuite()

suite.addTests(loader.loadTestsFromModule(ParameterizersTestCase))
suite.addTests(loader.loadTestsFromModule(PaymentRoleTestCase))

runner = unittest.TextTestRunner()
runner.run(suite)