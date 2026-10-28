"""Reusable utility functions for the project."""  
    #This module can be imported and used in other parts of the project to perform common tasks, such as password validation and generation.

from .age_calc_utility import calculate_age

from .calculator_utility import add, subtract, multiply, divide

from .password_utility import check_password_strength, generate_random_password