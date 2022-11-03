# no importing libraries allowed for this project

# function for converting from military time
def mil_con(hour: int):
    """Converts an hour as military time into its standard format along with its meridiem"""
    if hour == 0:
        return 12, 'AM'
    elif hour == 12:
        return 12, 'PM'
    if 1 <= hour < 12:
        return hour, 'AM'
    elif 12 < hour < 24:
        return hour - 12, 'PM'
    else:
        return 9999, "Error"


def add_time(start: str, duration: str, starting_day=''):
    """Takes a time, adds a specific amount of hours and minutes, and returns the time it would be after.
    If at least a day has passed, return the amount of days passed. If a starting day is specified, it also returns the
    day it would be.

    :param start: the starting time, in standard format
    :param duration: how much time to pass in HH:MM format
    :param starting_day: (optional) what day it is during the 'start' variable
    """
    # convert start variable into int variables. HH = starting hour, MM = starting minute
    colon_idx = start.index(':')
    space_idx = start.index(' ')
    HH = int(start[:colon_idx])
    MM = int(start[colon_idx+1:space_idx])
    # isolate meridiem (AM, PM)
    start_meridiem = start[space_idx+1:]
    # convert duration variable into into int variables. hh = duration hour, mm = duration minute
    colon_idx = duration.index(':')
    hh = int(duration[:colon_idx])
    mm = int(duration[colon_idx+1:])

    # convert starting time to military time for easier calculation
    if start_meridiem == 'AM' and HH == 12:
        HH = 0
    elif start_meridiem == 'PM' and HH != 12:
        HH += 12

    # variables to store the final time, in order to convert it to be a standard time
    end_hour = HH + hh
    end_minute = MM + mm
    # convert minutes >= 60 into the appropriate hours
    if end_minute >= 60:
        plus_hour = end_minute // 60
        end_hour += plus_hour
        end_minute -= (plus_hour * 60)

    # at this point we can figure out how many days have passed
    # initiate variable to store how many days passed once the duration time has passed
    days_passed = 0
    # these variables store how much time is needed in order to enter the next day
    hours_needed = 0
    minutes_needed = 60 - MM
    if minutes_needed == 60:
        minutes_needed = 0
        hours_needed = 24 - HH
    else:
        hours_needed = 24 - HH - 1
    # if there is enough time within 'duration' for a day to be passed, we add 1 to days_passed
    if hh > hours_needed or (hh == hours_needed and mm >= minutes_needed):
        days_passed += 1
        # create new variables to find out how much more days have passed which is: duration - the time we calc'd
        mm_left = mm - minutes_needed
        hh_left = hh - hours_needed
        if mm_left < 0:
            mm_left += 60
            hh_left -= 1
        days_passed += hh_left//24

    days_later = ''
    if days_passed == 1:
        days_later = ' (next day)'
    elif days_passed > 1:
        days_later = f' ({days_passed} days later)'
    else:
        days_later = ''

    # convert time to standard time
    if end_hour > 24:
        end_hour = end_hour % 24
    end_hour, end_meridiem = mil_con(end_hour)
    if end_minute < 10:
        end_minute = str(end_minute)
        end_minute = f'0{end_minute}'
    else:
        end_minute = str(end_minute)

    next_day = ''
    if starting_day != '':
        # initiate a days list to iterate through later in order to find which day was landed on
        days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
        # lower starting_day so it can match with days list
        starting_day = starting_day.lower()
        day_idx = days.index(starting_day)
        next_day = f', {days[(day_idx + days_passed) % 7].title()}'

    return f'{str(end_hour)}:{end_minute} {end_meridiem}{next_day}{days_later}'
