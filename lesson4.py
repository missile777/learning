# 'dictionary' data structure
import unittest


def employee_costs_per_day(d: dict):
    return d


class TestListMethod(unittest.TestCase):
    def test_employee_costs_per_day(self):
        payroll = {'employee1': 12, 'employee2': 12, 'employee3': 13}
        self.assertEqual(employee_costs_per_day(payroll), 37)


payroll = {'employee1': 12, 'employee2': 12, 'employee3': 13}
print(payroll)
print(payroll.keys())
print(payroll.values())

print(employee_costs_per_day(payroll))
unittest.main()
