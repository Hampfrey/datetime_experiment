"""
Datetime

This code does things with datetime

This code contains the following functions:
  * main(), introduces the program and starts the loop
  * time_until(str), looks through the event dictionary and prints details
  * get_now_time_difference(time), gets the difference between local time and
    the given
  * cast_str_into_datetime(str), turns a datetime in string format into a 
    datetime
  * calculate_time_until(time or datetime), calculates the time until/differnce 
    of the inputed
  * time_in(), TO BE IMPLEMENTED
  * capitalize(str), capitalizes the first character of a string
  * command_input(str = "", process = 1), call for an input while 
    allowing EXIT whenever
"""
# Imports
import datetime

# Setup
current = datetime.datetime.now()
weekday = datetime.date.weekday(current)

# School day
calendar = (
    {
        # Monday
        "school": datetime.time(8, 30, 0),
        "period 1": datetime.time(8, 30, 0),
        "period 1 ends": datetime.time(10, 2, 0),
        "period 2": datetime.time(10, 8, 0),
        "period 2 ends": datetime.time(11, 40, 0),
        "lunch": datetime.time(11, 40, 0),
        "lunch ends": datetime.time(12, 14, 0),
        "period 3": datetime.time(12, 20, 0),
        "period 3 ends": datetime.time(13, 52, 0),
        "period 4": datetime.time(13, 58, 0),
        "period 4 ends": datetime.time(15, 30, 0),
        "school ends": datetime.time(15, 30, 0)
    },
    {
        # Tuesday
        "school": datetime.time(8, 30, 0),
        "period 1": datetime.time(8, 30, 0),
        "period 1 ends": datetime.time(9, 54, 0),
        "period 2": datetime.time(10, 0, 0),
        "period 2 ends": datetime.time(11, 24, 0),
        "advisory": datetime.time(11, 30, 0),
        "advisory ends": datetime.time(12, 00, 0),
        "lunch": datetime.time(12, 00, 0),
        "lunch ends": datetime.time(12, 30, 0),
        "period 3": datetime.time(12, 36, 0),
        "period 3 ends": datetime.time(14, 0, 0),
        "period 4": datetime.time(14, 6, 0),
        "period 4 ends": datetime.time(15, 30, 0),
        "school ends": datetime.time(15, 30, 0)
    },
    {
        # Wednesday
        "school": datetime.time(9, 0, 0),
        "period 1": datetime.time(9, 0, 0),
        "period 1 ends": datetime.time(10, 26, 0),
        "period 2": datetime.time(10, 32, 0),
        "period 2 ends": datetime.time(11, 58, 0),
        "lunch": datetime.time(11, 58, 0),
        "lunch ends": datetime.time(12, 28, 0),
        "period 3": datetime.time(12, 34, 0),
        "period 3 ends": datetime.time(13, 59, 0),
        "period 4": datetime.time(14, 5, 0),
        "period 4 ends": datetime.time(15, 30, 0),
        "school ends": datetime.time(15, 30, 0)
    },
    {
        # Thursday
        "school": datetime.time(8, 30, 0),
        "period 1": datetime.time(8, 30, 0),
        "period 1 ends": datetime.time(9, 49, 0),
        "period 2": datetime.time(9, 55, 0),
        "period 2 ends": datetime.time(11, 14, 0),
        "access": datetime.time(11, 20, 0),
        "access ends": datetime.time(12, 5, 0),
        "lunch": datetime.time(12, 5, 0),
        "lunch ends": datetime.time(12, 40, 0),
        "period 3": datetime.time(12, 46, 0),
        "period 3 ends": datetime.time(14, 5, 0),
        "period 4": datetime.time(14, 11, 0),
        "period 4 ends": datetime.time(15, 30, 0),
        "school ends": datetime.time(15, 30, 0)
    },
    {
        # Friday
        "school": datetime.time(8, 30, 0),
        "period 1": datetime.time(8, 30, 0),
        "period 1 ends": datetime.time(9, 49, 0),
        "period 2": datetime.time(9, 55, 0),
        "period 2 ends": datetime.time(11, 14, 0),
        "jag time": datetime.time(11, 20, 0),
        "jag time ends": datetime.time(12, 5, 0),
        "lunch": datetime.time(12, 5, 0),
        "lunch ends": datetime.time(12, 40, 0),
        "period 3": datetime.time(12, 46, 0),
        "period 3 ends": datetime.time(14, 5, 0),
        "period 4": datetime.time(14, 11, 0),
        "period 4 ends": datetime.time(15, 30, 0),
        "school ends": datetime.time(15, 30, 0)
    },
    {
        # Saturday
    },
    {
        # Sunday
    },
    {
        # Unassigned
        "4:97": datetime.time(17, 37, 0),
        "noon": datetime.time(12, 0, 0),
        "world end p2": datetime.datetime(2024, 12, 12, 12, 12, 12),
        "world end": datetime.datetime(2012, 12, 12, 12, 12, 12),
        "tf2 heavy update": datetime.datetime(9999, 6, 5, 12, 13, 9),
        "half-life release": datetime.datetime(1998, 11, 19, 0, 0, 0)
    }
    
)
locations = {
    "london": "datetime.datetime.now(timezone.utc)",
    "tokyo": "",
    "bejing": "",
    "munich": "",
    "moon": "",
    "south pole": ""
}

# List
def main():
    """
    Introduce the user and start up the loop
    """
    print("\nWelcome to \"Datetime Calculator\"" +
          "\n  - Type LIST to print a list of all options" +
          "\n  - Current options are \"time until ____\" and" +
          "\n    \"time in ____\"" +
          "\n  - Enter EXIT at any time to leave ")
    
    # While loop
    while(True):
        option = command_input("\nWhat would you like to do?" + 
                               " Type LIST for options : ").lower()
        if option == "list":
            print("\nTIME UNTIL, Weekday Events")
            for key, value in calendar[weekday].items():
                print("    " + key, ":", value)
            print("TIME UNTIL, Global Events")
            for key, value in calendar[7].items():
                print("    " + key, ":", value)
            print("TIME IN, Locations")
            for key, value in locations.items():
                print("    " + key, ":", value)
        if option != "":
            words = option.split()
            if "time" == words[0]:
                if "until" == words[1]:
                    time_until(option[11:])
                elif "since" == words[1]:
                    time_until(option[11:], True)
                elif "in" == words[1]:
                    time_in(option[8:])
    
def time_until(event):
    """
    Look through the events dictionary and print the selected deats
    
    Args:
        event (str): The event in question
    """
    if event in calendar[weekday]:

        # Weekday based events
        print()
        print(capitalize(event + " happens at " + 
                        str(calendar[weekday][event])))
        timedelta = str(calculate_time_until(calendar[weekday][event]))
        timedelta = timedelta.split(":")
        print("Which is in " + timedelta[0] + " hours, " + timedelta[1] + 
                " minutes, and " + timedelta[2] + " seconds")
    elif event in calendar[7]:

        # Unassigned events
        print()
        if type(calendar[7][event]) == type(current):

            # Datetimes
            print(capitalize(event + " happens on " + 
                    str(calendar[7][event])))
            timedelta = str(calculate_time_until(calendar[7][event]))
            timedelta = timedelta.split(", ")
            time = timedelta[1].split(":")
            print("Which is in " + timedelta[0] + ", " + time[0] + 
                    " hours, " + time[1] + " minutes, and " + time[2] + 
                    " seconds")
        else:

            # Times
            print(capitalize(event + " happens at " + 
                    str(calendar[7][event])))
            timedelta = str(calculate_time_until(calendar[7][event]))
            timedelta = timedelta.split(":")
            print("Which is in " + timedelta[0] + " hours, " + timedelta[1] 
                    + " minutes, and " + timedelta[2] + " seconds")
    else:
        print("\nInvalid event")

def get_now_time_difference(time):
    """
    This function subtracts a time from now
    
    Args:
        time (time): The time to check
    
    Return:
        time_dif (timedelta): The time difference
    """
    current = datetime.datetime.now()
    time_str = str(time)
    current_str = str(current)
    current_date_str = current_str[:11]
    time_dif = cast_str_into_datetime(current_date_str + time_str) - current
    return(time_dif)

def cast_str_into_datetime(string):
    """
    This function subtracts a time from now
    
    Args:
        string (str): A datetime converted into a string in standard format
    
    Return:
        (datetime): The string now in datetime format
    """
    # this is horrific
    datetime_str = ""
    for x in string:
        if x != "-" and x != ":":
            datetime_str += x
        else:
            datetime_str += " "
    datetime_split = datetime_str.split()
    year = int(datetime_split[0])
    month = int(datetime_split[1])
    day = int(datetime_split[2])
    hour = int(datetime_split[3])
    minute = int(datetime_split[4])
    second = int(datetime_split[5])
    return datetime.datetime(year, month, day, hour, minute, second)

def calculate_time_until(time_or_datetime):
    """
    This function finds the time until an event
    
    Args:
        time_or_datetime (time or datetime): The time of an event or an event's 
        datetime
    
    Return:
        time_dif (str): The time until it, accounting for day difference
    """
    if type(time_or_datetime) == type(current): 
        # Datetimes
        timedate = time_or_datetime
        return timedate - current
    else:
        # Times
        time = time_or_datetime
        time_dif = str(get_now_time_difference(time))
        if time_dif[0] == "-":
            time_dif = time_dif[8:]
        return time_dif

def time_in(location):
    """
    Look through the location dictionary and print its timezone stuff

    Args:
        location (str): The location in question
    """
    print("\nlocation was " + location + " ")

def capitalize(string):
    """
    This function capitalizes the first letter of a string
    
    Args:
        string (str): The string
    
    Return:
        (str): The string with a capital first letter
    """
    return string[0].upper() + string[1:]
    

def command_input(prompt = "", process = 0):
    """
    A simple function that allows the user to input values while having access 
    to EXIT. If a bool_mode is enabled it will look for certain keywords and 
    process them as True or False
    
    Process values
        0, string mode, return the input
        1, bool mode, force the user to choose True or False
        2, bool mode passthrough, ask the user if they'd like to do something,
           if they don't input anything return False
        
    Args:
        prompt (str = ""): The prompt for asking the user with
        process (int = 0): Determines the process mode
    
    Return:
        return_input (str): The user input after having checked for exit
        (bool): If bool mode is on
        return_bool (bool): If bool mode passthrough is on
    """
    # Bool mode check words
    true_words = ["yes", "correct", "true"]
    false_words =["no", "incorrect", "false"]
    
    if process == 0:
        # String mode
        return_input = input(prompt)
        if return_input.lower() == "exit":
            print("\nExiting... ")
            exit()
        else:
            return return_input
    elif process == 1:
        # Bool mode
        while(True):
            bool_input = input(prompt).lower()
            if bool_input == "exit":
                print("\nExiting... ")
                exit()
            else:
                if bool_input == "y" or bool_input in true_words:
                    return True
                if bool_input == "n" or bool_input in false_words:
                    return False
                input("\nFailed bool_mode input, please use Y or N ")
    elif process == 2:
        # Bool mode passthrough
        bool_input = input(prompt).lower()
        if bool_input == "exit":
            print("\nExiting... ")
            exit()
        else:
            return_bool = False
            if bool_input == "y" or bool_input in true_words:
                return_bool = True
            return return_bool
        
if __name__ == '__main__':
    main()