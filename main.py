# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define f = Character("Dr.Fox")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it
    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    scene bg black
    with None

    centered "{i}{b}Warning{/i}{/b}\nThis game contains content that may not be suitable for everyone\nPlayer discretion advised"
    centered "{i}{b}DO NOT ATTEMPT TO SAVE DURING THE GAMBLING PORTION{/i}{/b}"
    scene bg room
    with fade

    "{i}You wake up in a dark room, with nothing but an old wooden table before you{/i}"
    "{i}The last thing you remember was some kind of fight, the details are fuzzy{/i}"
    "{i}Perhaps you hit your head too hard. But you need to figure out the details{/i}"


    default hostile = False
    show drfox neutral
    with dissolve 
    f "My, oh my, Friend. It seems you have finally woken up"
    f "Tell me, how do you feel? I am an excellent doctor after all"
    "I... feel fine -"

    menu:
        "Why am I here?":
            jump here

        "What happened?":
            jump happened

    label here:
        f "Long story short, you were as good as dead"
        hide drfox neutral
        show drfox arms
        f "But I am an excellent doctor, so I gave you a second chance"
        f "After all, I got my prize and victory. I've won the jackpot, you could say."
        hide drfox arms
        show drfox neutral
        f "Or perhaps the \"Russian roulette\" is more appropriate"

        menu:
            "Dead.....?":
                jump happened

            "Victory...?":
                jump victory


    label happened:
        hide drfox neutral
        show drfox arms
        f "Well, my friend, after the great battle you put up to defend your dignity, you were in rough shape"
        f "Unfortunately for you, my twin assistants got their hands on an RPG, and goodness knows what happened from there"
        hide drfox arms
        show drfox neutral
        f "Naturally, your wife wouldn't want to stay with someone who messes around with other women"


    label victory:
        hide drfox neutral
        show drfox arms
        f "You don't need to worry about proving yourself to your wife now, my friend."
        f "You can play around with those mechanic women or cabaret women as much as you like now"
        hide drfox arms
        show drfox neutral
    

        menu:
            "How dare you!":
                jump offense
            
            "My wife-!":
                jump wife

        label offense:
            $ hostile = True    
            "Our family was fine without you"
            "I'll make you pay for that fox!"
            jump wager

        label wife:
            hide drfox neutral
            show drfox arms
            f "You had your chance to protect her happiness"
            f "Even your daughter deserted you"
            hide drfox arms
            show drfox neutral
            jump wager

        


label wager:
    if hostile:
        hide drfox neutral
        show drfox arms
        f "You would've died had it not been for me!"
        f "So now let's see if you're worth your life"
        jump gamble
    else:
        hide drfox neutral
        show drfox arms
        f "But I am not an unkind fox"
        f "So I'll let you earn back your life"
        jump gamble
label gamble:
    
    if hostile:
        play music "aura.mp3" volume 0.7
    else:
        pass
    f "I may be a Doctor but I do love a good gamble"
    f "So here's my deal, if you can beat me, you live"
    f "It's a simple game I play with my patients to zero or double their bills"
    f "I'll roll two dice. You guess two numbers."
    f "The dice hits your number, your win"
    f "But whats the fun in that"
    show drfox arms
    with None
    show revolver at right 
    with fade
    "You-!"
    f "Now now, I won't be using it yet my friend"
    f "The idea is each dice roll, the loser will have to pull the trigger"
    f "Of course only one chamber is full"
    f "A thrilling gamble, is it not!?"
    if hostile:
        pass
    else:
        play music "aura.mp3" volume 0.7
    default lived = False
    default luck = False
    define lives = 0
 
    label code:
        if lived:
            f "So you lived for another round"
        else:
            pass
        if luck:
            f "Seems I got lucky. Lets see if the same can be said for you"
        else:
            pass
       
     
        python:
            import random
            dice1 = random.randint(1, 6)
            dice2 = random.randint(1, 6)
            
            def main():
                
   
                try:
                    guess1 = int(renpy.input("Guess a number"))
                    guess2 = int(renpy.input("Guess your second number"))
                except ValueError:
                    narrator("Not a number!")
                    renpy.jump("code")

                    
                if valid(guess1):
                    pass
                if valid(guess2):
                    pass
                else:
                    narrator("Pick a number between 1 - 6")
                    renpy.jump("code")


                if guess1 == dice1:
                    renpy.jump ("gunfox")
                elif guess1 == dice2:
                    renpy.jump ("gunfox")
                elif guess2 == dice1:
                    renpy.jump ("gunfox")
                elif guess2 == dice2:
                    renpy.jump ("gunfox")
                else:
                    renpy.jump ("yougun")

            def valid(s):
                if s >= 1 and s <= 6:
                    return True


            main()
    label gunfox:
            f "The dice are [dice1] and [dice2]"
            f "Good guess!"
            "{i}He takes the gun and pulls the trigger{/i}"
            jump foxshoot
        
    label yougun:
        f "The dice are [dice1] and [dice2]"    
        f "Seems like you lucked out"
        menu:
            "Take the gun":
                jump youshoot
    label youshoot:
        $ lived = True
        $ lives += 1
        if lives == 8:
            jump youn
        python:
            import random
            bullets = ['1', '2', '3', '4', '5', 'Death']
            random.shuffle(bullets)
            while bullets:
                result = bullets.pop()
                if 'Death' == result:
                    renpy.play ("gunshot.mp3")
                    renpy.jump ("bad_end")
                else:
                    renpy.play ("blank.mp3")
                    renpy.jump ("code")
        
    label foxshoot:
        $ luck = True
        $ lives += 1
        if lives == 8:
            jump foxn
        else:
            pass
        python:
            import random
            bullets = ['1', '2', '3', '4', '5', 'Death']
            random.shuffle(bullets)
            while bullets:
                result = bullets.pop()
                if 'Death' == result:
                    renpy.play ("gunshot.mp3")
                    renpy.jump ("good_end")
                else:
                    renpy.play ("blank.mp3")
                    renpy.jump ("code")
    
label foxn:
python:
    import random
    bullets = ['1', '2', '3', '4', '5', 'Death']
    random.shuffle(bullets)
    while bullets:
        result = bullets.pop()
        if 'Death' == result:
            renpy.play ("gunshot.mp3")
            renpy.jump ("good_end")
        else:
            renpy.play ("blank.mp3")
            renpy.jump ("neutral_end")

label youn:
python:
    import random
    bullets = ['1', '2', '3', '4', '5', 'Death']
    random.shuffle(bullets)
    while bullets:
        result = bullets.pop()
        if 'Death' == result:
            renpy.play ("gunshot.mp3")
            renpy.jump ("good_end")
        else:
            renpy.play ("blank.mp3")
            renpy.jump ("neutral_end")

label good_end:
    scene bg black
    scene bg sky
    with fade
    stop music fadeout 1.5
    "The bitter taste of your previous defeat leaves with every breath of fresh air"
    if victor:
        "{b}Good Ending...?{/b}"
    else:
        "{b}Good Ending{/b}"
    jump credits

default victor = False
label neutral_end:
    $ victor = True
    hide revolver
    hide drfox arms
    show drfox neutral
    stop music fadeout 2.0
    f "It seems lady luck has smiled on us today"
    hide drfox neutral 
    with fade
    show drfox arms
    with None  
    f "We shall part ways here so you can enjoy your new second life"
    hide drfox arms
    with dissolve
    scene bg black
    with dissolve
    "Somehow it still feels like you lost despite being alive"
    menu:
        "{i}I'll count this as my win{/i}":
            jump good_end
        "...........":
            jump sudoku
    
label sudoku:
    scene bg room
    "Can you accept this win and move on and live?"
    menu:
        "....... Yes":
            jump good_end
        "...........":
            pass
    "The silence in the room is deafening. You can only hear your heartbeat."
    "................."
    "You can still leave the building. You can move on"    
    label rusure:
        "Are you sure?"
        menu:
            "I have nothing left":
                jump commit
                
            "I don't know":
                jump sudoku
    label commit:
        "You can still turn back"
        menu:
            "Turn back":
                jump sudoku        
            ".........":
                jump rusure    
            "End it all":
                jump doit

    label doit:
        show revolver at right
        with dissolve
        "{i}There's still one in the chamber{/i}"
        menu:
            "I can't":
                jump sudoku
            "Take the gun":
                pass
        hide revolver
        show revolver
        menu:
            "I can't":
                jump sudoku
            "Cock the gun":
                pass
        play sound "blank.mp3"
        menu:
            "I can't":
                jump sudoku
            "End it all":
                pass
        hide revolver
        show revolver at truecenter
        with dissolve
        menu:
            "I can't":
                jump sudoku
            "Pull the trigger":
                pass
        play sound "gunshot.mp3"
        jump bad_end



label bad_end:
    scene bg black
    with dissolve
    $ renpy.music.set_volume(1.0, 0.0)
    "You died!"
    "{b}Bad Ending{/b}"
    jump credits
# This ends the game.

label credits:
    scene bg black
    centered "{b}{i}Credits{/b}{/i}\nImages: bg room - FNaF Pizzeria Simulator Wiki\n Revolver - Fortnite Wiki\nAudio - Pixabay, {i}Made in Abyss{/i}, Kevin Penkin - The Rumble of Scientific Triumph"
    centered "Characters - Loosely based off of Hololive GTA5 Roleplay (Shirakami Fubuki and Inugami Korone)"
    centered "Made by GoldiusWonder"
    centered "Thanks for playing!"
    return
