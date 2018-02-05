# A basic choose your own adventure game to review funcion defintions, loops, breaks ect.
#This is the space tutorial.

import random
import time
from textwrap import dedent


def displayIntro():
     print(dedent( """
        A putrid odor fills your nostrils. You are running through some sort of underground tunnel. You are completely devoid of memory.
        But, you are filled with a sense of urgency and you know you must run. Your feet pound against the gravel. Your head is pounding along with it.
        Do you remember how you got here? Do you even want to? There is no time left now! Quick make a decision. East or West.
    """))

def choosePath():
    path = ""
    while path != "1"and path != "2":  #input validation if both equal to underground and surfae then its true
        print("I couldn't quite catch that. Please enter 1 or 2:")
        path = input(" Which will you choose? (1 or 2): ")
        print()

    return path

def checkPath(chosenPath):
      print("You head  underground")
      time.sleep(5)
      print("It's cold.")
      time.sleep(8)
      print("So very cold")
      time.sleep(3)
      print("You wonder..")
      time.sleep(3)
      print("Where is everyone else?")
      print()

      correctPath = (1)

      if chosenPath == str(correctPath):
         print("You will get your answer soon enough.")
         print("That voice..")
         time.sleep(8)
         print("You don't recognize it. But it fills you with..")
         time.sleep(2)
         print("T")
         time.sleep(2)
         print("R")
         time.sleep(2)
         print("E")
         time.sleep(2)
         print("P")
         time.sleep(2)
         print("I")
         time.sleep(2)
         print("D")
         time.sleep(2)
         print("A")
         time.sleep(2)
         print("T")
         time.sleep(2)
         print("I")
         time.sleep(2)
         print("O")
         time.sleep(2)
         print("N")
      else:
         print(" You feel rush of electricity through your body.")
         print("Then nothing.")




replay = "yes"
while replay == "yes" or replay == "y":
     displayIntro()
     choice =choosePath()
     checkPath(choice) # choice is equal to "1" or "2"
     replay = input("Would you want to play again? (yes or y?): ") 
