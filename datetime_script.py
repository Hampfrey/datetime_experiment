"""
Datetime

This code

This code contains the following functions:
  * funct(var), description
"""
# Imports
import datetime

# Setup
current = datetime.datetime.now()
events_old = {
    "end of school": datetime.time(15, 30, 0),
    "school": datetime.time(8, 30, 0),
    "world end": datetime.datetime(2012, 12, 12, 12, 12, 12)
}
calendar = {
    "monday": {
        "school": datetime.time(8, 30, 0),
        "period 1": datetime.time(8, 30, 0),
        "period 1 ends": datetime.time(8, 30, 0),
        "period 2": datetime.time(8, 30, 0),
        "period 2 ends": datetime.time(8, 30, 0),
        "lunch": datetime.time(8, 30, 0),
        "lunch ends": datetime.time(8, 30, 0),
        "period 3": datetime.time(8, 30, 0),
        "period 3 ends": datetime.time(8, 30, 0),
        "period 4": datetime.time(8, 30, 0),
        "period 4 ends": datetime.time(15, 30, 0),
        "school ends": datetime.time(15, 30, 0)

    }
}
locations = {
    "london": ""
}

# List
def main():
    """
    Introduce the user and start up the loop
    """
    print("\nWelcome to \"Datetime Calculator\"" +
          "\n  - Type LIST to print a list of all options" +
          "\n  - Enter requests like \"time in london\"" +
          "\n  - Enter EXIT at any time to leave. ")
    
    # While loop
    while(True):
        option = command_input("\nWhat would you like to do?" + 
                               " Type LIST for options : ").lower()
        if option == "list":
            print(events)
            print(locations)
        words = option.split()
        if "time" == words[0]:
            if "until" == words[1]:
                time_until(option[11:])
            elif "in" == words[1]:
                time_in(option[8:])
    
def time_until(event):
    """
    Look through the events dictionary and print the selected deats
    
    Args:
        event (str): The event in question
    """
    if event == "end of school":
        print("\nSchool ends at " + str(events["end of school"]))
        #print(  "  - School will end in " + str(calculate_time_until(events["end of school"])))
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
    if False: 
        # Datetimes
        "woo"
    else:
        # Times
        time = time_or_datetime
        time_dif = str(get_now_time_difference(time))
        if time_dif[0] == "-":
            time_dif = time_dif[8:]
        print(time_dif)

def time_in(location):
    """
    Look through the location dictionary and print its timezone stuff

    Args:
        location (str): The location in question
    """
    print("\nlocation was " + location + " ")

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
                    break
                if bool_input == "n" or bool_input in false_words:
                    return False
                    break
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
    calculate_time_until(events["school"])
    command_input()
    calculate_time_until(events["end of school"])
    command_input()
    main()