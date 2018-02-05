print("""The train ride home is long, but at this hour is peaceful. You have just return from a year in Fort Benning for basic training.You are tired, but proud of yourself. You are not the same person who left.
    The sound of wailing babies has ceased and the noisy people on their phones are no more.
    Besides you and an older couple. The train is quite bare . You are about to doze off to sleep when "Club" by Dej Loaf breaks the silence of the train.
    The couple looks over at you in disapproval.What do you do?
    """)
 



door = input("> ")

if door == "1":
    print("There's a giant bear here eating a cheese cake.")
    print("What do you do?")
    print("1. Take the cake.")
    print("2. Scream at the bear.")

    bear = input("> ")

    if bear == "1":
        print("The bear eats your face off. Good job!")
    if bear == "2":
        print("The bear eats your legs off. Good job!")
    else:
        print(f"Well, doing {bear} is probably better.")
        print("Bear runs away.")

elif door == "2":
    print("You stare at the endless abyss at Hades retina.")
    print("1. Blueberries.")
    print("2. Yellow jacket clothespins.")
    print("3. Understanding revolvers yelling melodies.")

    insanity = input("> ")

    if insanity == "1" or insanity == "2":
        print("Your body survives powered by a mind of jello.")
        print("Good job!")
    else:
        print("The insanity rots your eyes into a pool of muck.")
        print("Good job!")

else:
    print("You stumble around and fall on a knife and die.")
