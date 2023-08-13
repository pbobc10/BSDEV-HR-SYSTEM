import datetime

class FiscalYear:
    def __init__(self):
        self.calculate_fiscal_year()

    def calculate_fiscal_year(self):
        current_date = datetime.date.today()
        if current_date.month >= 10:  # If the current month is October or later, the fiscal year starts in the current year
            self.start_year = current_date.year
        else:  # Otherwise, the fiscal year starts in the previous year
            self.start_year = current_date.year - 1

        self.fiscal_year_start = datetime.date(self.start_year, 10, 1)
        self.fiscal_year_end = datetime.date(self.start_year + 1, 9, 30)

    def is_in_fiscal_year(self, date_to_check):
        return self.fiscal_year_start <= date_to_check <= self.fiscal_year_end
    
    def __str__(self) -> str:
        return f"{self.start_year}-{self.start_year+1}"

# Example usage:
# fiscal_year = FiscalYear()

# date_to_check = datetime.date(2023, 7, 22)  # Replace with datetime.date.today() to use the current date

# if fiscal_year.is_in_fiscal_year(date_to_check):
#     print(f"The date {date_to_check} is within the fiscal year {fiscal_year.start_year}-{fiscal_year.start_year+1}.")
# else:
#     print(f"The date {date_to_check} is outside the fiscal year {fiscal_year.start_year}-{fiscal_year.start_year+1}.")
