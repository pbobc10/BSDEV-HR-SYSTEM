from datetime import date
class FiscalYear:
    def __init__(self,year):
        self.year = year
        self.start_date = date(year,10,1)
        self.end_date = date(year + 1,9,30)
    False
    
    def is_giving_day_in_fiscal_year(self,giving_day):
        if giving_day >= self.start_date and giving_day <= self.end_date:
            return True
        else:
            return False