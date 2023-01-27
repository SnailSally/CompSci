import time

have_money = False

def start():
    print("Oh no! Fred, the school bully lost the lunch money he stole from you!\nIt's after hours and you were about to walk home, but he caught you in Town Hall!\nIf you don't find the money and bring it back to him soon, he'll beat you up!!")
    time.sleep(10)
    townhall()

def townhall():
    global have_money
    if have_money == False:
        print("You are in Town Hall")
        move = input("\nWhere would you like to go? Say one of these choices:\n\tcourtyard\n\tcafeteria\n\tbathroom\n\tb hallway\n\tattendance\n")
        if move.lower() == "courtyard":
            courtyard()
        elif move.lower() == "cafeteria":
            cafeteria()
        elif move.lower() == "bathroom":
            bathroom()
        elif move.lower() == "b hallway":
            B_Hallway()
        elif move.lower() == "attendance":
            attendance()
        else:
            print("That's not an option, stupid. I'll assume you want to stay here.")
            time.sleep(5)
            townhall()
    if have_money == True:
        print("Congrats! You got the money back to Fred! You've saved yourself... for now\n🥸")


def courtyard():
    print("You are in the Courtyard. But... there's a HUGE food fight! You get attacked with mashed potatoes and chocolate milk! ")
    move = input("\nWhere would you like to go? Say one of these choices:\n\ttown hall\n")
    if move.lower() == "town hall":
        townhall()
   
    else:
        print("That's not an option, stupid. I'll assume you want to stay here and get pummeled with more food.")
        time.sleep(5)
        courtyard()

def cafeteria():
    print("You are in the cafeteria.\nThere isn't much here, only the disgusting school food.")
    move = input("\nWhere would you like to go? Say one of these choices:\n\ttown hall\n\tbathroom\n")
    if move.lower() == "town hall":
        townhall()
    elif move.lower() == "bathroom":
        bathroom()
    else:
        print("You moron, that's not an option. I'll assume you want to stay here.")
        time.sleep(5)
        cafeteria()

def bathroom():
    print("You are in the bathroom. There's a huge clump of people talking about how much they hate school")
    move = input("\nWhere would you like to go? Say one of these choices:\n\ttown hall\n\tcafeteria\n")
    if move.lower() == "town hall":
        townhall()
    elif move.lower() == "cafeteria":
        cafeteria()
    else:
        print("That's not an option, stupid. I'll assume you want to stay here chat with these losers.")
        time.sleep(5)
        bathroom()

def B_Hallway():
    print("You are in the B Hallway")
    move = input("\nWhere would you like to go? Say one of these choices:\n\ttown hall\n\tlibrary\n\tgym\n")
    if move.lower() == "town hall":
        townhall()
    elif move.lower() == "library":
        library()
    elif move.lower() == "gym":
        gym()
    else:
       print("That's not an option. I'll assume you want to stay here.")
       time.sleep(5)
       B_Hallway()

def library():
    print("You walk into the library and... oh no.")
    time.sleep(4)
    print("You're worst nightmare. Best Buddies Club is meeting there!")
    time.sleep(4)
    print("Everyone is gathered around in a circle, holding hands, and singing the Teamwork song!")
    time.sleep(4)
    print("You try to make a run for it but they catch you and make you join them!")
    time.sleep(4)
    move = input("\nWhere would you like to go? Say one of these choices:\n\ttown hall\n\tgym\n\tcourtyard\n")
    if move.lower == "town hall":
        townhall()
    elif move.lower() == "gym":
        gym()
    elif move.lower() == "courtyard":
        courtyard()
    else:
        print("That's not an option, stupid. I'll assume you want to stay here and continue singing children's songs.")
        time.sleep(5)
        library()

def gym():
    print("Congrats! You found jammed in between the bleachers in the gym! Now get it back to Frad before it's too late!")
    time.sleep(4)
    global have_money 
    have_money = True
    move = input("\nWhere would you like to go? Say one of these choices:\n\ttown hall\n\tlibrary\n")
    if move.lower == "town hall":
        townhall()
    if move.lower == "library":
        library()
        ###

def attendance():
    print("You are in the attendance office.\nthe principle isn't very happy to see you. You've already been suspended twice for making ketchup bombs.")
    move = input("\nWhere would you like to go? Say one of these choices:\n\ttown hall\n\tcourtyard\n")
    if move.lower() == "town hall":
        townhall()
    elif move.lower() == "courtyard":
        courtyard()
    else:
        print("That's not an option, you dummy. I'll assume you want to stay here anger the principal even more.")
        time.sleep(5)
        attendance()

start()