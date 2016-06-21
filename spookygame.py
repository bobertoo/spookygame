#!/usr/bin/python

#This a game of survival. See how many monsters you can escape from!

import random

def spookyGame():
    print '\nof course you do!\n'
    monsters = [['ogre', 3], ['vampire', 5], ['spooky snake', 10], ['cranky old dude', 1]]
    health = 10
    score = 0
    while health > 0:
        dice = random.randint(0, len(monsters)-1)
        freakotheweek = monsters[dice][0]
        print 'you were attacked by a ' + freakotheweek
        health -= monsters[dice][1]

        if health <= 0:
            print 'your top score was ' + str(score)
            print 'game over!! :(\n'

            print 'want to play again?\n'
            playagame = raw_input('Type "yes" to play again! Type anything else to quit.\nAnswer: ')
            if playagame == 'yes' or playagame == 'y' or playagame == 'YES':
                    spookyGame()
            else:
                    print 'maybe next time!'

        else:
            print 'your health is now at ' + str(health) + ' points\n'
            score += 1

print '\nthis is a game about trying to see how many monsters you can get past.'
print 'want to play?\n'
playagame = raw_input('Type "yes" to play! Type anything else to quit.\nAnswer: ')
if playagame == 'yes' or playagame == 'y' or playagame == 'YES':
        spookyGame()
else:
        print 'try again if you want!'
