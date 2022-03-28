import random
highest = 10
ans= random.randint(1,highest)
ask=int(input("Enter a nnumber between 1-10: "))
if ask < ans:
    print ("Guess higher") 
if ask>ans:
    print("Guess lower")
if ans==ask:
    print("Your guess is correct")
    