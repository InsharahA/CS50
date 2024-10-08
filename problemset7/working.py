import re
import sys

def main():
    print(convert(input("Hours: ")))

def convert(s):
    time = ""
    match = re.search(r"(\d{1,2})(:)?(\d{2})?\s?(?P<fampm>AM|PM)\s+to\s+(\d{1,2})(:)?(\d{2})?\s?(?P<tampm>AM|PM)", s)
    
    if not match:
        return "Invalid input"

    # Process the start time
    start_hour = int(match.group(1))
    start_minutes = match.group(3) if match.group(3) is not None else "00"
    fampm = match.group("fampm")
    
    # Validate start minutes
    if int(start_minutes) >= 60:
        raise ValueError("Invalid minutes in start time")

    # Convert start time to 24-hour format if needed
    if fampm == "PM" and start_hour != 12:
        start_hour += 12
    elif fampm == "AM" and start_hour == 12:
        start_hour = 0

    time = f"{start_hour:02}:{start_minutes} to "

    # Process the end time
    end_hour = int(match.group(5))
    end_minutes = match.group(7) if match.group(7) is not None else "00"
    tampm = match.group("tampm")
    
    # Validate end minutes
    if int(end_minutes) >= 60:
        raise ValueError("Invalid minutes in end time")

    # Convert end time to 24-hour format if needed
    if tampm == "PM" and end_hour != 12:
        end_hour += 12
    elif tampm == "AM" and end_hour == 12:
        end_hour = 0

    time += f"{end_hour:02}:{end_minutes}"

    return time

if __name__ == "__main__":
    main()
