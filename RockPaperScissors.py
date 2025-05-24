import random

values = { "R":"Rock", "P":"Paper", "S":"Scissors"}
choose_random = random.choice(list(values))

print("Let's Play the classic game of Rock, Paper and Scissors")
print("Considered as valid input: \n\"R: Rock\" \n\"P: Paper\" \n\"S: Scissors\" \n")

user = input("Enter your Choice: ")

if user in values:
    if(choose_random == "R" and user == "R"):
        print("it's a tie try again.")
    elif(choose_random == "P" and user == "P"):
        print("it's a tie try again.")
    elif(choose_random == "S" and user == "S"):
        print("it's a tie try again.")
    elif(choose_random == "R" and user == "S"):
        print("program wins.")
    elif(choose_random == "R" and user == "P"):
        print("user wins.")
    elif(choose_random == "P" and user == "S"):
        print("user wins.")
    elif(choose_random == "P" and user == "R"):
        print("program wins.")
    elif(choose_random == "S" and user == "R"):
        print("user wins.")
    elif(choose_random == "S" and user == "P"):
        print("program wins.")

else:
    print("Invalid Input!")
print("End! \nThanks for Playing.")
