import random
import sys
# def GuesingGame(randomnum):
#     userinput = int(input("Guess a number"))
#     if randomnum != userinput:
#         while userinput != randomnum:
#             userinput = int(input("Guess a number"))
#         print(" hey you found the random number")
#     elif userinput == 'exit':
#         sys.exit(" ah you are exiting")


# randomnum = random.randint(1,2)
# GuesingGame(randomnum)

# ---------------------------------------------------------

randomnum = random.randint(1,9)
userinput = 0
# while randomnum != userinput:
#     userinput = input("Enter the random number")
#     if userinput == 'exit':
#         print ("Exting ....")
#         break
# else:
#     print("Hey you found the random number")


while randomnum != userinput:
    userinput = int(input(" Enter the random number"))
else:
    print(" Hey you found the random number !!!!Whoooola!!!!!!")







