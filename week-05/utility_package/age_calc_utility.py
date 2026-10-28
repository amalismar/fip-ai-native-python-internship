"""Function for calculating age"""

from datetime import date

def calculate_age(birth_year, birth_month, birth_day):
    """Calculate age based on birth date

    Args:
        birth_year (int): Year of birth
        birth_month (int): Month of birth
        birth_day (int): Day of birth
    
    Returns:
        int: Age in years
    
    Raises:
        ValueError: If the birth date is in the future
    """

    birth_date = date(birth_year, birth_month, birth_day)

    today = date.today()

    if birth_date > today:
        raise ValueError("Birth date cannot be in the future.")

    age = today.year - birth_date.year

    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age -= 1

    return age