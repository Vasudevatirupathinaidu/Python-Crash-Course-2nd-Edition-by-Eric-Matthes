
import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    """Tests for the module employee"""

    def setUp(self):
        """Make an employee to use in tests."""
        self.employee1 = Employee('vasu', 'bonu', 10000)

    def test_give_default_raise(self):
        """Test that a default raise works correctly."""
        salary = self.employee1.give_raise()
        self.assertEqual(salary, 15000)

    def test_give_custom_raise(self):
        """Test that a custom raise works correctly."""
        salary = self.employee1.give_raise(3000)
        self.assertEqual(salary, 13000)

if __name__ == '__main__':
    unittest.main()
