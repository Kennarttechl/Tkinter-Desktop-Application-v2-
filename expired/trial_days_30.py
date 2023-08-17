
from datetime import datetime, timedelta 
"""This is are built-in module, which are part of python standard library
# timedelta is used to keep track of the time duration for the trial period.
"""

def check_trial_status() -> bool:
    current_date = datetime.now().date() # This provide us with the right date or month
    trial_start_date = datetime(2023, 8, 2).date() #Setting a defualt date as starting date
    trial_end_date = trial_start_date + timedelta(days=30) # This keep track of the date till 30d
    if trial_end_date.month != trial_start_date.month:
        trial_end_date = trial_end_date.replace(day=1)
        """
        # It compares the current_date with the trial_end_date and returns True if the current date is greater (i.e., after) the trial end date, indicating that the trial period has expired.
        
        This conditional statement checks if the month of the trial_end_date is different from the month of the trial_start_date. If the trial period spans across two different months (e.g., if the start date is June 1 and the end date is July 1), it sets the day of the trial_end_date to 1. This ensures that the trial end date remains within the same month as the start date.
        """
    return current_date < trial_start_date or current_date > trial_end_date


