def last_digit(num):
    """Computes the last digit of the num

    Args:
        num (int): A positive integer

    Returns:
        (int) : The last digit of num (123 -> 3)
    """
    
    last_digit = num % 10 
    return int(last_digit)
# Right shifts num by one digit
#  123 -> 12
def decimal_right_shift(num):
    right_shift = num /10
    return int(right_shift)

# Sum digit of the input -- assume there
# are exactly three digits
def sum_digits(num):
    #prints out last digit
    thirdDigit = last_digit(num)
    #prints out first two digits
    twoDigit = decimal_right_shift(num)
    #prints out second digit
    secondDigit = last_digit(twoDigit)
    #prints out first digit
    firstDigit = decimal_right_shift(twoDigit)
    sum = thirdDigit + secondDigit + firstDigit
    print(sum)
# Ask the user for input and print a message
# Three possible messages:
#    "Number must be all digits"
#    "Number must be three digits"
#    "The sum of the digits of <num> is <result>"
def main():
    num = input("Please enter a 3-digit positive number:\n\t")
    if not num.isnumeric(): 
        print ("Number must be all digits" )
    elif len(num) != 3 :
        print ("Number must be three digits")
    else:
        return sum_digits(int(num))
if __name__ == "__main__":
    main()
