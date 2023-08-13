
from .calculate_easter_date import calculate_easter_date
import datetime

def calculate_mardi_gras_date(year):
    # Get the date of Easter for the given year
    easter_year, easter_month, easter_day = calculate_easter_date(year)

    # Calculate the date of Mardi Gras (47 days before Easter Sunday)
    easter_date = datetime.date(easter_year, easter_month, easter_day)
    mardi_gras_date = easter_date - datetime.timedelta(days=47)

    return mardi_gras_date.year, mardi_gras_date.month, mardi_gras_date.day


# Example usage:
# year = 2023
# mardi_gras_year, mardi_gras_month, mardi_gras_day = calculate_mardi_gras_date(year)
# print(f"Mardi Gras in {year} is on {mardi_gras_month}/{mardi_gras_day}/{mardi_gras_year}")
