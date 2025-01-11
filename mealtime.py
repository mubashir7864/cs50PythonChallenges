
from datetime import datetime,time

def main():
    # Take user input for the time (e.g., "2:30 PM")
    userInput = input("Please enter the time (e.g., 2:30 PM): ")
    convertTime(userInput)

def convertTime(inp):
    # Format the time string. Assuming user input is in 12-hour format (e.g., "2:30 PM")
    time_format = "%I:%M %p"
    
    try:
        # Convert the time string to a datetime object
        conTime = datetime.strptime(inp, time_format)

        timeOnly = conTime.time()

        breakfast_start = time(7, 0)  # 7:00 AM
        breakfast_end = time(8, 0)    # 8:00 AM

        if  breakfast_start <= timeOnly <= breakfast_end:
            print("Its BreakFast Time")
        
        # Print the converted time
        print(f"Converted time: {conTime.time()}")  # Only print time part
    except ValueError:
        print("Invalid time format. Please enter the time in the format: HH:MM AM/PM")

    

main()