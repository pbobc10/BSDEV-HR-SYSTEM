import unittest
from django.test import TestCase

# Create your tests here.
import datetime
from unittest import TestCase, mock
from  forms.leaves_forms import get_total_leave_days
from models.leaves_models import Leave

class TestGetTotalLeaveDays(TestCase):
    def setUp(self):
        self.start_date = datetime.date(2022, 1, 1)
        self.end_date = datetime.date(2022, 1, 15)

    def test_no_days_off(self):
        self.assertEqual(get_total_leave_days(self.start_date, self.end_date), 14)

    def test_with_days_off(self):
        with mock.patch('my_module.DaysOff.objects.filter') as mock_filter:
            mock_filter.return_value = [datetime.date(2022, 1, 3), datetime.date(2022, 1, 10)]
            self.assertEqual(get_total_leave_days(self.start_date, self.end_date), 12)

    def test_leave_days_less_than_15(self):
        self.start_date = datetime.date(2022, 1, 1)
        self.end_date = datetime.date(2022, 1, 5)
        self.assertEqual(get_total_leave_days(self.start_date, self.end_date), 4)

    def test_weekend_days_off(self):
        self.start_date = datetime.date(2022, 1, 1)
        self.end_date = datetime.date(2022, 1, 15)
        with mock.patch('my_module.DaysOff.objects.filter') as mock_filter:
            mock_filter.return_value = [datetime.date(2022, 1, 8), datetime.date(2022, 1, 9)]
            self.assertEqual(get_total_leave_days(self.start_date, self.end_date), 12)

    def test_start_date_equal_to_end_date(self):
        self.start_date = datetime.date(2022, 1, 1)
        self.end_date = datetime.date(2022, 1, 1)
        self.assertEqual(get_total_leave_days(self.start_date, self.end_date), 0)

    def test_no_leave_days(self):
        self.start_date = datetime.date(2022, 1, 1)
        self.end_date = datetime.date(2021, 12, 31)
        self.assertEqual(get_total_leave_days(self.start_date, self.end_date), 0)

if __name__ == '__main__':
    unittest.main()
