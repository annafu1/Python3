print("Choose a number between 0-10")
userInput = input("Guess here:")
userInput = int(userInput)
print(userInput)
from random import randrange
randomNum = randrange(1, 10)
print(randomNum)
if userInput > randomNum: 
    print("Guess was too high")
elif userInput < randomNum:
    print("Guess was too low")
else:
    print("Correct")  