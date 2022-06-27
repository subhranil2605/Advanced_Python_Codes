import unittest
from unittest.mock import patch
from employee import Employee


class TestEmployee(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # connecting to the database or other similar things done here
        # print('setupClass')
        pass
        

    @classmethod
    def tearDownClass(cls):
        # print('tearDownClass')
        pass
        

    def setUp(self):
        self.emp_1 = Employee("Subhranil", "Sarkar", 50000)
        self.emp_2 = Employee("Pritam", "Sarkar", 70000)
        

    def tearDown(self):
        pass
        

    def test_email(self):
        self.assertEqual(self.emp_1.email, 'Subhranil.Sarkar@gmail.com')
        self.assertEqual(self.emp_2.email, 'Pritam.Sarkar@gmail.com')

        self.emp_1.first = "Pijush"
        self.emp_2.first = "Ashik"
        self.emp_2.last = "Mamun"
        
        self.assertEqual(self.emp_1.email, 'Pijush.Sarkar@gmail.com')
        self.assertEqual(self.emp_2.email, 'Ashik.Mamun@gmail.com')
        

    def test_fullname(self):
        self.assertEqual(self.emp_1.fullname, 'Subhranil Sarkar')
        self.assertEqual(self.emp_2.fullname, 'Pritam Sarkar')

        self.emp_1.first = "Pijush"
        self.emp_2.first = "Ashik"
        self.emp_2.last = "Mamun"
        
        self.assertEqual(self.emp_1.fullname, 'Pijush Sarkar')
        self.assertEqual(self.emp_2.fullname, 'Ashik Mamun')


    def test_amt(self):
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, 52500)
        self.assertEqual(self.emp_2.pay, 73500)
        

    def test_monthly_schedule(self):
        with patch('employee.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = "success"
            schedule = self.emp_1.monthly_schedule('May')
            mocked_get.assert_called_with('http://company.com/Sarkar/May')
            self.assertEqual(schedule, 'success')

            mocked_get.return_value.ok = False
            schedule = self.emp_2.monthly_schedule('June')
            mocked_get.assert_called_with('http://company.com/Sarkar/June')
            self.assertEqual(schedule, 'Bad Response!')


if __name__ == "__main__":
    unittest.main()
