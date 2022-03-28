from random import randint, random
from creditcard_part1 import last_digit, decimal_right_shift

def verify(number13):
    digits = len (number13)
    
"""
Generate is using random and it is creating a 7 digit number
"""     
def generate():
      number6 = randint(1000000,9999999)
      return str(number6) 
"""
The luhn algorithim is taking in input and joinning it with the random numbers genrated by the random function   
"""
def luhn(ccnum):
    if(len(ccnum) != 13):
        return False
    newCCNum = ""
    sum = 0
    for i in range(len(ccnum)):
        if i % 2 == 0:
            duplicate = int(ccnum[i]) * 2
            if((duplicate) > 9):
                strDuplicate = str(duplicate)
                digit1 = strDuplicate[0]
                digit2 = strDuplicate[1]
                sumOfDigits = int(digit1) + int(digit2)
                newCCNum = newCCNum + str(sumOfDigits)
            else:
                newCCNum = newCCNum + str(duplicate) 
        else:
            newCCNum = newCCNum + ccnum[i]
    for i in range(len(newCCNum)):
        sum = sum + int(newCCNum[i])
    if sum % 10 == 0:
        return True
    
    else:
        return False


# Possible return values
#
# "<num> is not all digits"
#
# "<num> is not six digits"
# "Three valid numbers:"
# "\t<num1>"
# "\t<num2>"
# "\t<num3>"
def main():
    base = input("Enter a 6 digit number:\n")
    if not base.isnumeric(): 
        print ("Number must be all digits" )
    total = base + generate()
    count = 0 
    while count < 3: 
        if luhn(total) == True:
            print(total)
            count = count + 1  
        total = base + generate()

        
  
if __name__ == "__main__":
    main()