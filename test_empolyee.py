import unittest
from IT_employee import ITEmployee

class EmployeeWithoutPositionTests (unittest.TestCase):
    def setUp(self):
        self.emp = ITEmployee("Elena","Pian","QA" )

    def test_names(self):
        self.assertEqual(self.emp.name,"Elena")
        self.assertEqual(self.emp.surname,"Pian")


