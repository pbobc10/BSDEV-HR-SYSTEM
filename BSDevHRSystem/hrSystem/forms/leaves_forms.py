
from datetime import timedelta, datetime
from typing import Any
from django.forms import ModelForm,TextInput,DateInput,EmailInput,NumberInput,Select,DateField
from ..models.leaves_models import Leave
from django.core.validators import ValidationError
from ..fiscal_year import FiscalYear
# from datetime import datetime
from ..models.days_off_models import DaysOff
import logging
import datetime


class LeaveForm(ModelForm):
    def clean(self) -> dict[str, Any] | None:
        cleaned_data = super().clean()
        start_date = cleaned_data.get('start_date')
        end_date = cleaned_data.get('end_date')
        reason = cleaned_data.get('reason')
        # calculate first if the start date is in the fiscal year
        if not FiscalYear().is_in_fiscal_year(start_date):
            raise ValidationError(f"Start date must be in the fiscal year {FiscalYear()}")
        # calculate second if the end date is in the fiscal year
        elif not FiscalYear().is_in_fiscal_year(end_date):
            raise ValidationError(f"End date must be in the fiscal year {FiscalYear()}")
        else:
            # check if start date is before end date
            if start_date > end_date:
                raise ValidationError("Start date must be less than end date")
            # check amount of leaves base on reason
            if reason == 'SICK LEAVE':
                if end_date - start_date != timedelta(days=15):
                    raise ValidationError(f"The sick leave entitlement should amount to a total of 15 days but it is { end_date - start_date}.")
            elif reason == 'VACATION':
                if get_total_leave_days(start_date, end_date) != timedelta(days=15):
                    raise ValidationError(f"The vacation leave should be equivalent to a total of 15 days but it is {end_date - start_date}.")
            elif reason == 'MATERNITY':
                if end_date - start_date != timedelta(days=84):
                    raise ValidationError(f"The martnity leave should be equivalent to a total of 84 days but it is {end_date - start_date}.")
            elif reason == 'PATERNITY':
                if end_date - start_date != timedelta(days=5):
                    raise ValidationError(f"The paternity leave should be equivalent to a total of 5  days but it is {end_date - start_date}.")
        
        return cleaned_data

    class Meta:
        model = Leave
        exclude = ('employee',)
        fields = '__all__'
        labels = {
            'comment': '',
        }
        widgets = {
            'employee':Select(attrs={'class':'form-control'}),
            'start_date':DateInput(attrs={'class':'form-control','type': 'date'}),
            'end_date':DateInput(attrs={'class':'form-control','type': 'date'}),
            'reason':Select(attrs={'class':'form-control'}),
            'comment':TextInput(attrs={'class':'form-control','placeholder': 'Enter value here...'}),
            
        }


def get_total_leave_days(start_date,end_date):
    # get total leave days
    days_off = DaysOff.objects.filter(day__range=(start_date,end_date))
    # QuerySet to set
    days_off_set = set()
    for obj in days_off.distinct():
        days_off_set.add(obj)

    # put leave days in a set
    # convert date in leave days to  proleptic Gregorian ordinal of a date.
    # The proleptic Gregorian ordinal represents the number of days since January 1, 1 AD.
    leave_days = set(range(start_date.toordinal(), end_date.toordinal() + 1))
    print(leave_days)
    leave_days = { datetime.date.fromordinal(day) for day in leave_days }
    print(leave_days)
    # remove days off in set
    leave_days -= days_off_set
    # put all sundays in a list
    sundays = list()
    # check if the leave has two consecutive sundays
    for day in leave_days:
        if day.weekday() == 6:
            sundays.append(day)
    # find the min sunday
    min_sunday = min(sundays)
    if (min_sunday + timedelta(days=7)) not in leave_days:
        # track the execution of the function and to troubleshoot any problems that might occur
        logging.error("The leave should have two consecutive sundays.")
        raise ValidationError("The leave should have two consecutive sundays.")
    return len(leave_days)
