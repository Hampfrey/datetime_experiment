"""
NAME

This code

This code contains the following functions:
  * funct(var), description
"""
# Imports
import datetime

# Setup
current = datetime.datetime.now()
events = {
    "end of school": datetime.datetime(2024, 3, 6, 15, 30, 0)
    
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
    SUMMARY
    
    Args:
        event (str): 
    
    Return:
        time (idk): 
    """
    if event == "end of school":
        print("\nSchool ends at " + str(events["end of school"]))
        #print(  "  - School will end in " + str(calculate_time_until(events["end of school"])))
    else:
        print("\nInvalid event")

def calculate_time_until(time):
    return_time = time - current.time()
    return return_time

def time_in(location):
    """
    SUMMARY
    
    Args:
        location (str): 
    
    Return:
        time (idk): 
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
    main()