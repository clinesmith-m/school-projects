import random

# Functions
def look(location):
    # Self-explanatory, thank God.
    print(descriptions[location])
    print(show_exits[location])
    if check_enemy(location) == True:
        print(enemy_desc[location])
    if items[location] == []:
        print("You see nothing around that can help you.")
    else:
        print("Around you, you see: a(n)", ", a(n) ".join(items[location]))

def move(attempt, location, previous):
    # Checks validity, and returns valid entries.
    if attempt in exits[location] and attempt in causes:
        death(attempt)
        return ""
    elif attempt == previous and attempt in exits[location]:
        return attempt
    elif check_enemy(location) == True:
        print("You cannot advance. There is an enemy present.")
        return ""
    elif attempt in exits[location]:
        return attempt
    else:
        print("'%s' is not a valid location." % attempt)
        return ""

def check_enemy(location):
    # Check for enemies, returns a Bool.
    for item in enemies:
        if location in enemies[item][0]:
            return True
    return False

def take(attempt, location):
    #Checks validity and takes item. Returns nothing.
    if check_enemy(location):
        print("You cannot take anything, there is an enemy present.")
        return
    if attempt in items[location] and attempt in causes:
        death(attempt)
    elif attempt in items[location]:
        items[location].remove(attempt)
        items["player"].append(attempt)
        print("Taken.")
    else:
        print("There is no '%s' here" % attempt)

def drop(attempt, location):
    # Check validity and drops item in current location
    if attempt in items["player"]:
        items["player"].remove(attempt)
        items[location].append(attempt)
        print("Dropped.")
    else:
        print("You do not have a '%s' in your inventory." % attempt)
        
def eat(attempt, hp):
    # Checks for validity and eats edible stuff.
    if attempt in foods and attempt in items["player"]:
        print("You feel satisfied. Your health is replenished.")
        hp = 5
        items["player"].remove(attempt)
        return hp
    elif attempt in items["player"]:
        print("You try to eat %s. That isn't food. You should know that." % attempt)
        death("dysentery")
        return hp
    else:
        print("You do not have '%s' in your inventory." % attempt)
        return hp

def check_combat(attempt, location):
    # Checks validity of "attack" inputs by cross-checking the player's current location, enemy location and the attempted weapon. Returns valid inputs.
    with_index = find_with(attempt)
    if with_index == -1:
        print("I'm sorry, I don't know how to 'attack %s'." % attempt)
        return ""
    else:
        enemy = " ".join(list_of_words[0:with_index])
        weapon = " ".join(list_of_words[with_index +1:])
        if enemy not in enemies or location not in enemies[enemy][0]:
            print("There is no '%s' to attack here." % enemy)
            return ""
        elif weapon not in enemies[enemy][1]:
            print("You cannot attack '%s' with '%s'." % (enemy, weapon))
            return ""
        elif weapon not in items["player"]:
            print("There is no '%s' in your inventory." % weapon)
            return ""
        else:
            return enemy

def find_with(attempt):
    # Breaks attack inputs into weapon and enemy
    global list_of_words
    list_of_words = attempt.split(" ")
    for index in range(0, len(list_of_words)):
        if list_of_words[index] == "with":
            return index
    return -1

def combat(hp, enemy):
    # Takes health and calculates battle. Deletes the enemy from 'enemies' dictionary if you win.
    enemy_hp = 1
    p_hits = 0
    npc_hits = 0
    p_strike = random.randint(0,10)
    npc_strike = random.randint(0,9)
    if p_strike >= 5:
        p_hits += 1
    if npc_strike >= 6:
        npc_hits += 1
    if hp - npc_hits == 0:
        print("You lose the battle. You have been slain.")
        return 0
    if p_hits == 1:
        print("You have slain the %s." % enemy)
        del enemies[enemy]
        hp = hp - npc_hits
        print("He hit you %d time(s). %d more hit(s) and you will die." % (npc_hits, hp))
        return hp
    else:
        hp = hp - npc_hits
        print("Your attack misses.")
        print("He hit you %d time(s). %d more hit(s) and you will die." % (npc_hits, hp))
        return hp

def fight_wallace(command):
    # Shreks William Wallace.
    index = find_with(command)
    item = " ".join(list_of_words[index + 1:])
    if item in items["player"]:
        print(wallace_deaths[item])
        return True
    else:
        print("You do not have a(n) '%s' in your inventory." % item)
        return False

def attack_boucher(b_health, command):
    # attacks Bobby Boucher in penultimate stage.
    index = find_with(command)
    weapon = " ".join(list_of_words[index +1:])
    strike = random.randint(0,10)
    if weapon == "dirty water":
        print("He reels in disgust, stammering incoherently.")
        return 0
    if strike >= 3:
        print("You hit Boucher with '%s'. It is effective, but the strike hurts your hand. You drop your weapon." % weapon)
        drop(weapon, "causeway")
        b_health = b_health - 1
        print("%d more hit(s), and you'll defeat him." % b_health)
        return b_health
    else:
        print("Your attack misses.")
        return b_health

def boucher_attack(hp):
    strike = random.randint(0,10)
    if strike > 5:
        hp -= 1
        print("Boucher lunges at you, and catches you in a ferocious sack. You can only take %d more hits." % hp)
        return hp
    else:
        print("Boucher lunges at you, but you step aside.")
        return hp

def hug(npc):
    # Self-explanatory
    if npc == "watchman":
        print("You open your arms to him. He accepts. Tears beginning to form in his eyes.")
        print("\"Thank you, kind stranger,\" he says to you. \"Now let me repay you. Are you a foe of William Wallace, played here by the incomparable Mel Gibson?\"")
        print("You tell him you are.")
        print("\"Well,\" he explains, \"William is guarded by his loyal and trustworthy waterboy, Bobby Boucher. Go to the storm drain beyond the dungeon to get dirty water, which will vanquish him instantly.\"")
        print("The watchman the keels over, dead from starvation. Which was a long time coming, to be honest.")
        del enemies["watchman"]
    else:
        print("You cannot hug '%s'." % npc)

def death(trigger):
    # Removes a life and tells you why
    global lives
    lives = lives - 1
    try:
        print(descriptions[trigger])
    except:
        pass
    print(causes[trigger])
    print("Lives - 1. You now have %d lives left." % lives)

# Global variables.
location = "outside"
previous_loc = "outside"
health = 5
boucher_health = 4
wallace_alive = True
boss_fight = False
foods = ["apple", "beer", "horse meat", "sausage", "bread", "potato", "flagon", "dirty water"]
while True:
    try:
        lives = int(input("How many lives do you want? (3 or more is highly reccomended) "))
        break
    except:
        print("That is not a valid number of lives")
        
exits = {
    # exits from a given location
    "outside" : ["drawbridge", "sewer"],
    "drawbridge" : ["moat", "courtyard"],
    "courtyard" : ["stables", "turret", "mess hall", "dungeon"],
    "stables" : ["courtyard", "window"],
    "mess hall" : ["courtyard", "storeroom"],
    "turret" : ["spire", "courtyard", "barracks"],
    "spire" : ["turret", "the sky"],
    "the sky" : [],
    "barracks" : ["dungeon", "turret", "causeway", "armory"],
    "dungeon" : ["barracks", "storm drain"],
    "storm drain" : ["dungeon"],
    "causeway" : ["chambers"]
    }

descriptions = {
    "outside" : "You are outside a castle in the lovely Scottish countryside.",
    "drawbridge" : "Once you are on the drawbridge, you realize that all the guards have died of the plague. You are able to advance easily.",
    "sewer" : "You are in the sewer. It looks like a sewer. It smells like a sewer. You realize you've made a bad call.",
    "moat" : "The water in the moat is very cold and full of sewage. You feel regret immediately.",
    "courtyard" : "You are in the castle's main courtyard.",
    "stables" : "The stable smells of it's equestrian occupants.",
    "turret" : "There is a lovely view from atop the castle's turret.",
    "mess hall" : "The mess hall is full of delicious, uneaten food. Which makes sense, because all of the soldiers are dead from the plague.",
    "window" : "There is nothing but air for many feet beneath you.",
    "storeroom" : "There's nothing in here but a few links of sausage. The rats have eaten the rest.",
    "spire" : "From atop the spire, everything looks small.",
    "the sky" : "You flap your arms and fly away like a bird. It's beautiful up here!",
    "barracks" : "The barracks are practically empty. You would think no one was left in this castle if not for someone in the causeway beyond quietly murmmering, \"Momma, momma.\"",
    "dungeon" : "The dungeon is rank, but empty, save for a dead knight sitting by the door, and the slow gurgle of water flowing from the storm drain beyond.",
    "storm drain" : "There is nothing here but dirty water and an old bucket.",
    "armory" : "You swing the door of the armory open to see the face of a man you swear you recognize. In fact, it looks just like your Computer Science I teacher, Dr. Shepherd.",
    "causeway" : "You stand in the causeway, mere inches from your main objective.",
    "chambers" : "Finally, you have reached your objective. You open the door to see William Wallace, played by the incomparable Mel Gibson, laying on his bed, mostly dead from the plaugue."
    }

show_exits = {
    "outside" : "To your left is a drawbridge. It's down, but well guarded. A sewer also empties into the moat beneath you.",
    "drawbridge" : "In front of you is an open courtyard. Beneath you, the water of the moat ripples gently.",
    "courtyard" : "Directly in front of you is the mess hall. You also see a ladder that goes up to castle's turret, and some stables to your left.",
    "stables" : "The stables have only one exit: back into the courtyard. A small window shines light on the scene.",
    "mess hall" : "Behind you is the courtyard, while on the far side of the room, you spy the castle's storeroom.",
    "turret" : "You see you can return to the courtyard. You can also venture up the spire to your left, or proceed into the castle's barracks on your right.",
    "spire" : "From the bright blue light of the sky, you can tell there's nowhere to go but back down to the turret.",
    "the sky" : "You fly home. You fail your mission, but you can fly. The positives outweigh the negative here.",
    "barracks" : "There are many options before you. You can go back to the turret or proceed right into the dungeon or left into the armory. There's also the causeway, but you feel sure that if you go there, there will be no turning back.",
    "dungeon" : "You see no obvious options but to go back to the barracks.",
    "storm drain" : "The only way out is back through the dungeon",
    "causeway" : "Wallace's chambers are now only a few steps away.",
    "chambers" : "There's nothing left now but to kill the insurgent Wallace with... hell, just about anything would do it at this point."
    }

items = {
    "player" : ["armor", "sword", "helmet"],
    "outside" : ["apple", "fair maiden"],
    "drawbridge" : [],
    "courtyard" : ["spear", "horseshoe", "shield"],
    "stables" : ["horse meat", "horse meat", "horse meat", "horse meat", "sword", "hammer", "nails"],
    "mess hall" : ["beer", "sausage", "bread", "potato", "frying pan", "kitchen knife"],
    "turret" : ["bow", "rock"],
    "spire" : ["rusty sword", "horn", "flag", "crossbow"],
    "the sky" : ["beautiful life unfold before you"],
    "barracks" : ["axe", "flagon",],
    "dungeon" : ["longsword", "pail of death"],
    "storm drain" : ["bucket", "dirty water", "porno mag"],
    "causeway" : [],
    "chambers" : [],
    }

weapons = ["sword", "spear", "shield", "hammer", "nails", "frying pan", "kitchen knife", "bow", "rock", "rusty sword", "crossbow", "axe", "longsword",
               "dirty water",]
things = ["armor", "sword", "helmet", "apple", "spear", "horseshoe", "shield", "horse meat", "hammer", "nails", "beer", "sausage",
             "bread", "potato", "frying pan", "kitchen knife", "bow", "rock", "rusty sword", "horn", "flag", "crossbow", "axe", "flagon",
             "porno mag", "longsword", "bucket", "dirty water",]
enemies = {
    # list[0] is the location, list[1] is what they can be attacked with
    "stable boy" : [
                    ["stables"],
                    weapons,
                    ],
    "archer" : [
                ["turret"],
                weapons,
                ],
    "cook" : [
                ["mess hall"],
                weapons,
                ],
    "watchman" : [
                ["spire"],
                weapons,
                ],
    "bobby boucher" : [
                ["causeway"],
                weapons
                ],
    "william wallace" : [
                ["chambers"],
                things
                ]
    }

enemy_desc = {
    "stables": "A stable boy stirs, sword in hand, none too happy to see you.",
    "mess hall": "Except for the cook, who's ready to charge you with a frying pan.",
    "turret": "The view is currently being observed by an archer. Who is now looking at you. Bow in hand.",
    "spire": "A haggard watchman gazes deeply into your soul with forlorn eyes. \"I've been stuck up here for 30 years,\" he tells you, \"And over all those long cold nights, all I've ever wanted is a hug.\"",
    "causeway": "But, the faint murmmering you heard earlier turns into a blood-curdling shout, \"MOMMA SAYS YOU THE DEVIL!!\" and just like that, Bobby Boucher, the WATERBOY is upon you.",
    "chambers": "It's really just matter of personal taste."
    }

causes = {
    "fair maiden" : "Seeing the fair maiden, you try to take her for your esteemed wife. She doesn't like that, though, and stabs you in the face. You twitch awkwardly for a bit and die.",
    "sewer" : "You start to feel a sharp pain in your gut. You hardly have time to realize that you've contracted dysentery before you keel over dead.",
    "moat" : "You feel very chilled. You decide it's time to give up and go home. You only feel worse once you get there, though. You linger for a few days and then die shamefully of pneumonia.",
    "window" : "You climb out the window. For some reason. Even though there's no reason for you to do that. You fall to your death.",
    "storeroom" : "You sniff the room to determine if these are plaugue carrying rats. They are. You contract plaugue from them and die.",
    "armory" : "That's when you realize that it's the 1300s and computer science doesn't exist. The room is clearly full of toxic hallucinagens. You body crumples in what is, without doubt, the most far-out death of all time.",
    "pail of death" : "You take a thing called 'pail of death' and die instantly... Who says there are no great cinematic twists anymore?",
    "dysentery" : "You would know that. If it wasn't for the dysentery."
    }

wallace_deaths = {
    "armor": "You take off your armor, and place it on Wallace. Which doesn't really do anything, but he dies anyway.",
    "sword": "You swing your sword at Wallace. It's overkill, but it doesn't not work.",
    "helmet": "In a less than dignified moment, you pose Wallace with your helmet on his head. If looks coud kill, Wallace would roast you alive. Looks don't kill, though. Plaugue does. Wallace dies.",
    "apple": "Sympathetic to his struggle, you give Wallace and apple to help him recoup his health. It doesn't work, though, and he dies.",
    "spear": "You throw a spear at him. ... You throw a spear at a bedridden man. To be fair, though, he is dead now.",
    "horseshoe": "You ask him if he wants to play horseshoes. He dies. I guess that's a no.",
    "shield": "You bash him with a shield. He dies. Unsurprisingly.",
    "horse meat": "You offer him horse meat. From his own horse. He dies, but you can still tell he doesn't like you.",
    "hammer": "You bash his head in with a hammer. Six hundred years from now, you'd be diagnosed as a psycopath. For now, though... it's the 1300s. We just won't talk about this.",
    "nails": "You take the nails, and use them to tack a picture of Wallace's wife, Marion, above his bed. He mouths \"Thanks\" at you and dies peacefully.",
    "beer": "You offer him a final beer. He's already dead, but his Scottish reflexes drink it anyway. Impressed by his ability to reinforce stereotypes, you go home.",
    "sausage": "You munch on some sausage, confident that Wallace will die soon of natural causes. He does. Good job, Hitman.",
    "bread": "You ask if it's okay if you eat some of his bread. He dies. You assume that means it's probably okay. It's a safe assumption.",
    "potato": "You throw a potato at him. He dies. Yay!",
    "frying pan": "You whack him upside the head with a frying pan. He does not survive.",
    "kitchen knife": "You draw your kitchen knife, and start whittling a nearby stick. Wallace dies. In other news, your stick should be satisfactory in about five minutes or so.",
    "bow": "You shoot Wallace with an arrow, even though he's bedridden. He dies. Somehow, though, I don't feel like you're a hero.",
    "rock": "You show him the cool rock you found. He dies before he can compliment your find, though. Unfortunate. It is a cool rock.",
    "rusty sword": "You show him your rusty sword. He dies from thinking about tetnis. And plaugue. He dies of plaugue, too.",
    "horn": "You blast your battle-horn in his face. He yells \"FREEDOM\" and dies. You feel cool, though. You got hear his catchphrase.",
    "flag": "You pull out the Scottish flag you found and begin to crochet profanities onto it. Wallace tells you that he always prefered cross-stitch and then dies.",
    "crossbow": "You pull out your crossbow, but decide that that would be a bit much. No worries, though, because he dies anyway.",
    "axe": "Good lord. You sicken, but you're effective. In your own sick way.",
    "flagon": "You take out your flagon and sip from it. Scotch. Very tasty. Wallace is already dead. Plaugue got 'im. The important thing is that this is some dang good scotch.",
    "porno mag": "You move in for the kill, but get distracted by your porno mag. He dies, but let's be honest, no one feels like a winner in this scenario. Except kind of you. It is some good porn.",
    "longsword": "You swing your longsword, aiming for his neck, but pulling you back. Your not proud, but he dies anyway. Next mission: find a chiropracter.",
    "bucket": "You put a bucket on his head. Unconventional, but effective. And by effective, I mean he died from natural causes. But, he had a bucket on his head, and that wouldn't have happened without you.",
    "dirty water": "You spill dirty water on the floor. Wallace dies. That works.",
    }

# Main program.
print("Welcome to Hitman: Agent 1347.")
print("It is the middle ages, and you are an elite member of King Edward III's personal death squad.")
print("Your mission: To infiltrate a Scottish castle and kill a reincarnation of William Wallace (played by the incomparable Mel Gibson) before he can invade England.")
throwaway = input("Press 'Enter' to begin.")
look(location)
while wallace_alive == True:
    command = input("Command? ")
    if command.startswith("go to "):
        if move(command[6:], location, previous_loc) != "":
            previous_loc = location
            location = command[6:]
            look(location)
    elif command.startswith("take "):
        take(command[5:], location)
    elif command.startswith("drop "):
        drop(command[5:], location)
    elif command.startswith("attack "):
        enemy = check_combat(command[7:], location)
        if enemy == "william wallace":
            temp1 = fight_wallace(command)
            if temp1 == True:
                print("MISSION COMPLETE.")
                print("CONGRATULATIONS.")
                wallace_alive = False
        elif enemy == "bobby boucher":
            boucher_health = attack_boucher(boucher_health, command)
            boss_fight = True
            if boucher_health == 0:
                del enemies["bobby boucher"]
                print("You defeat Bobby Boucher so hard that he has no choice but to run back to his Momma in tears.")
                boss_fight = False
        elif enemy != "":
            health = combat(health, enemy)
    elif command.startswith("eat "):
        health = eat(command[4:], health)
    elif command.startswith("hug "):
        hug(command[4:])
    elif command == "inventory":
        print("You have", ", ".join(items["player"]))
    elif command == "look":
        look(location)
    elif command == "quit":
        print("You abort the mission.")
        break
    else:
        print("'%s' is not a valid command." % command)
    if boss_fight == True:
        health = boucher_attack(health)
    if health == 0:
        break
    if location == "the sky":
        break

print()
print("Thank you for playing 'Hitman: Agent 1347'.")