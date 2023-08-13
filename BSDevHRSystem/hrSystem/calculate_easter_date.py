def calculate_easter_date(year):
    # Check if the provided year is within the valid range (Gregorian calendar starts from 1583)
    if year < 1583:
        raise ValueError("This algorithm is valid only for years from 1583 onwards.")

    # The following calculations are based on the Computus algorithm to determine the date of Easter

    # Remainder when the year is divided by 19
    year_mod_19 = year % 19

    # Number of centuries (divided by 100)
    centuries = year // 100

    # Remainder when the year is divided by 100
    year_mod_100 = year % 100

    # Number of years in the century that are leap years (divided by 4)
    leap_years_in_century = centuries // 4

    # Remainder when the number of centuries divided by 4
    centuries_mod_4 = centuries % 4

    # Number of leap years in the Metonic cycle
    leap_years_metonic_cycle = (centuries + 8) // 25

    # Difference between the number of centuries and leap years in the Metonic cycle
    difference_metonic_cycle = (centuries - leap_years_metonic_cycle + 1) // 3

    # Number of days since March 21 on which the full moon falls
    days_from_march_21 = (19 * year_mod_19 + centuries - leap_years_in_century - difference_metonic_cycle + 15) % 30

    # Number of years in the century that are leap years (divided by 4)
    leap_years_in_century_mod_4 = year_mod_100 // 4

    # Remainder when the number of years in the century divided by 4
    year_mod_4 = year_mod_100 % 4

    # Number of days from the full moon to the Sunday following it
    days_to_sunday = (32 + 2 * centuries_mod_4 + 2 * leap_years_in_century_mod_4 - days_from_march_21 - year_mod_4) % 7

    # Number of the month (March or April) of Easter Sunday
    easter_month_number = (days_from_march_21 + days_to_sunday - 7 * leap_years_metonic_cycle + 114) // 31

    # Calculate the day of Easter Sunday
    easter_day = ((days_from_march_21 + days_to_sunday - 7 * leap_years_metonic_cycle + 114) % 31) + 1

    # Return the year, month, and day of Easter Sunday as a tuple
    return year, easter_month_number, easter_day

# Test the function
# year = 2023
# year, month, day = calculate_easter_date(year)
# print(f"Easter Sunday in {year}: {month:02d}/{day:02d}")
