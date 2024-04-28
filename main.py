def add(list1,list2,d):
    list1.append(list2[d-1])

def fire(list):
    for item in range(len(list)):
        if list[item] == "lighter and batteries" or list[item] == "matches":
            return True
    return False

def light(list):
    for item in range(len(list)):
        if list[item] == "lantern":
            for i in range(len(list)):
                if list[i] == "matches":
                    return True
        elif list[item] == "flashlight":
            for i in range(len(list)):
                if list[i] == "lighter and batteries":
                    return True
    return False

def explo(list):
    for item in range(len(list)):
        if list[item] == "lighter fluid":
            for i in range(len(list)):
                if list[i] == "matches":
                    return True
        elif list[item] == "hair spray":
            for i in range(len(list)):
                if list[i] == "lighter and batteries":
                    return True
    return False

alive = 0

inventory = ["thin scarf","wooden stake"]
room1 = ["lighter and batteries", "matches"]
room2  = ["flashlight","lantern"]
room3 = ["hair spray","lighter fluid"]

print("This game is a choose your own adventure story. In each room you will be given a choice between two items to pick up that will help you defeat the next challenge.\n\n")
print(inventory)
print("\nThe outside resembles an old abandoned warehouse long forgotten by the small town it's on the edge of. Shattered windows, no power and graffiti covering the outside add to the image. The entrance keeps those appearances with having to step over suspicious puddles of liquid to get to the door and then spending a full minute to open the door from the rusted hinges. It reveals a room much more put together than the outside but still unclean in a way that hasn't been visited in years. The painting is chipped, and tables are dusty but still standing. There are also a few shelves in the otherwise barren room. On the shelves there are lighter and batteries or matches")

d1 = int(input(print("\nWould you like the lighter and batteries or matches? (1 for first choice/ 2 for second choice)\n")))
add(inventory,room1,d1)
print(inventory)





print("\nMoving on through the entrance room you go through the wooden door opposite to you. It reveals a straw doll in the middle about 5 feet tall and facing you. The room is plain, nothing is in except for a box on top of a shelf in the corner. There is a door behind the straw doll. When you go to take a step around the straw doll it moves sideways with you.\n")
if fire(inventory):
    d2 = input(print("\nWould you like to burn the straw doll? (yes/no)\n"))
    if d2 == "yes":
        print("\nThe straw doll goes up in flames and is gone in seconds. You then walk over to the box in the corner to find a flashlight and a lantern that looks like it needs matches")
        d3 = int(input(print("\n\nWould you like a flashlight or lantern? (1/2)")))
        add(inventory,room2,d3)
        print(inventory)
    else:
        alive = 1
        print("\n\nThe straw doll got to you before you were able to do anything. You Lose!")
else:
    alive = 1
    print("\n\nThe straw doll got to you before you were able to do anything. You Lose!")






if alive == 0:
    print("\n\nThrough the door is a small hallway that has no lights. You can make out a few doors on either side of the halfway, the ones that can be clearly seen appear to be bolted shut. Despite the light behind you the shadowy mass in the back of the hallway covers everything. You can though make out a few boxes in the middle of the hallway tucked against the wall. ")
    if light(inventory):
        d4 = input(print("\nWould you like to light up the room?(yes/no)"))
        if d4 == "yes":
            print("\nAfter the shadows are pulled to the corner of the room you go to the boxes and find hair spray and lighter fluid.")
            d5 = int(input(print("\nWould you like hair spray or lighter fluid? (1/2)")))
            add(inventory,room3,d5)
            print(inventory)
        else:
            alive = 1
            print("\n\nThe shadows swallowed everything before you could do anything. You Lose")
    else:
        alive = 1
        print("\n\nThe shadows swallowed everything before you could do anything. You Lose")




if alive == 0:
    print("\n\nThrough the final door is a hive with bugs everywhere. Crawling through holes in the ceiling, cracks on the ground. All types of ones too centipedes, wasps, what looks like a praying mantis egg lining the walls. In the middle though sits a ring encased in a glass box on top of a podium that's covered in insects. All that's left is to find a way to get it.")
    if explo(inventory):
        d6 = input(print("\nWould you like to burn all the bugs?(yes/no)"))
        if d6 == "yes":
            print("\nYou douse the oil over as much as the room as you can before pulling the cloth and wooden stake from your backpack. Wrapping the cloth around the stake and lighting it on fire takes less than 30 seconds but by now the bugs have noticed you in the door along with the oil they've been spreading. When they start to approach you, throw the torch into the center of the room and slam the door trying to get out of the warhouse as fast as you can. The sound of the bugs slowly die off until you are finally about 1/4 mile away from the warehouse. The warehouse is up in a blaise for the rest of the night. You go back in the morning to find the ring in the middle of the warehouse completely undefended. ")
            alive = 2
        else:
            print("\n\nThe bugs swarmed you before you could do anything. You Lose!")
            alive = 1
    else:
        print("\n\nThe bugs swarmed you before you could do anything. You Lose!")
        alive = 1

if alive == 2:
    print("\n\n\nCongradulations you completed the game!")

