name = input('Type your name: ')
print("Welcome", name, "to this adventure!")

answer = input("You are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go? ").lower()

if answer == "left":
    answer = input("You come to a river, you can walk around it or swim across? Type walk to walk around or swim to swim across: ").lower()

    if answer == "swim":
        print("You swim across and were eaten by an aligator.")

    elif answer == "walk":
        print("You walk for a while, ran out of water and you lost the game.")

    else:
        print("Not a valid option, YOU LOSE!")

elif answer == "right":
    answer = input("You come to a bridge, it looks wobbly, do you want to cross it or head back (cross/back) ")

    if answer == "back":
        print("You go back to the main road. YOU LOSE!")

    elif answer == "cross":
        answer = input("You cross the bridge and meet a stranger. Do you talk to them(Yes/No)? ")

        if answer == "yes":
            print("You talk to stranger and they give a gold medal. YOU WIN!!")

        elif answer == "no":
            print("You ignore the stranger and they are offended and kill you. YOU LOSE!")

        else:
             print("Not a valid option, YOU LOSE!")

    else:
        print("Not a valid option, YOU LOSE!")

else:
    print("Not a valid option. YOU LOSE!")
