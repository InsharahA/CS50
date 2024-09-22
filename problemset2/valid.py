def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    # Check length of the plate (2 to 6 characters)
    if len(s) < 2 or len(s) > 6:
        return False

    # Check if the first two characters are letters
    if not (s[0].isalpha() and s[1].isalpha()):
        return False

    # Loop through the characters to enforce rules
    number_started = False
    for i in range(2, len(s)):
        if s[i].isdigit():
            # Once a number is found, it must stay digits until the end
            if not number_started:
                # Check if the first digit is '0'
                if s[i] == '0':
                    return False
                number_started = True
        elif s[i].isalpha():
            # If a letter appears after numbers, it's invalid
            if number_started:
                return False
        else:
            # Invalid characters (punctuation, spaces, etc.)
            return False

    return True

main()
