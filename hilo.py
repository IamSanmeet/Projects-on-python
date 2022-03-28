    """A basic gussing game, wants you to think for a number anf it will try to guess it
    """
low = 1

high =1000
print("Please think of a number between {} and {}".format(low,high))
input("Press ENTER to start")
gusses=1
while True:
    guess=low+(high-low)//2
    
    highlo=input("My guess is {}.Guess higher or lower. Enter h for higher, l for lower and c if the guess was correct. " .format(guess).casefold())
    if highlo=="h":
        low=guess+1
    elif highlo=="l":
        high=guess-1
    elif highlo=="c":
        print("I got right answer in {} gusses".format(gusses))
        break
    else:
        print("Plese enter h,l or c.")
    gusses+=1    