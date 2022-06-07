#Hangman
import os
import random
logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''']
word_list = ['abruptly', 'absurd', 'abyss', 'affix', 'askew', 'avenue', 'awkward', 'axiom', 'azure', 'bagpipes', 'bandwagon', 'banjo', 
'bayou', 'beekeeper', 'bikini', 'blitz', 'blizzard', 'boggle', 'bookworm', 'boxcar', 'boxful', 'buckaroo', 'buffalo', 'buffoon', 'buxom', 
'buzzard', 'buzzing', 'buzzwords','caliph', 'cobweb', 'cockiness', 'croquet', 'crypt', 'curacao', 'cycle', 'daiquiri', 'dirndl', 'disavow', 
'dizzying', 'duplex', 'dwarves', 'embezzle', 'equip','espionage', 'euouae', 'exodus', 'faking', 'fishhook', 'fixable', 'fjord', 'flapjack', 
'flopping', 'fluffiness', 'flyby', 'foxglove', 'frazzled', 'fuchsia', 'funny', 'gabby', 'galaxy', 'galvanize', 'gazebo', 'giaour', 'gizmo', 
'glowworm', 'glyph', 'gnarly', 'gnostic', 'grogginess', 'haiku', 'haphazard', 'hyphen', 'iatrogenic', 'icebox', 'injury', 'ivory', 'ivy', 
'jackpot', 'jaundice', 'jawbreaker', 'jaywalk', 'jazzy', 'jelly', 'jigsaw', 'jinx', 'jiujitsu', 'jockey', 'jogging', 'joking', 'jovial', 
'joyful', 'juicy', 'jukebox', 'jumbo', 'kayak', 'kazoo', 'keyhole', 'khaki', 'kilobyte','kiosk', 'kitsch', 'kiwifruit', 'klutz', 'knapsack', 
'larynx', 'lengths', 'lucky', 'luxury', 'lymph', 'marquis', 'matrix', 'megahertz', 'mnemonic', 'mystify', 'naphtha', 'nightclub', 'nowadays', 
'numbskull', 'nymph','onyx', 'ovary', 'oxidize', 'oxygen', 'pajama','peekaboo', 'phlegm', 'pixel', 'pizazz', 'pneumonia', 'polka', 
'pshaw', 'psyche','puppy', 'puzzling', 'quartz', 'queue', 'quips','quixotic','quiz', 'quizzes', 'quorum', 'razzmatazz', 'rhubarb', 'rhythm', 
'rickshaw', 'schnpps', 'scratch', 'shiv', 'snazzy', 'sphinx', 'squawk', 'staff', 'strength', 'strengths', 'stronghold', 'stymied', 'subway',
 'syndrome', 'thriftless', 'thumbscrew', 'topaz', 'transcript', 'transplant', 'triphthong', 'twelfth', 'twelfths', 'unknown', 'unworthy', 
 'unzip', 'uptown', 'vaporize', 'vixen', 'vodka', 'vortex', 'voyeurism', 'walkway', 'waltz', 'wave','wavy', 'waxy', 'wellspring', 'wheezy', 
'whiskey', 'whizzing', 'whomever', 'wimpy', 'witchcraft', 'wizard', 'woozy', 'wristwatch', 'wyvern', 'xylophone', 'yachtsman', 'yippee',
 'yoked', 'outhful', 'yummy', 'zephyr', 'zigzag', 'zigzagging', 'zilch', 'zipper', 'zodiac', 'zombie', ]

#code stars here

word = random.choice(word_list)
lives = 6
count1 = 0
result = []
for letter in word:
    result += "_"
print(logo)
while count1 < len(word):
    count2 =0
    guess = input("Guess a letter: ").lower()
    os.system("cls") 
    if guess in result:
        print("you have already gussed the letter")
    else:
        for no in range(len(word)):
            if(guess == word[no]):
                count1 += 1
                count2 += 1
                result[no] = guess

        if(count2>0):
            print("Your guess is correct")
        else:
            print("Your Guess is wrong")
            lives -= 1
            print(stages[lives])

        if lives == 0:
            count1 = len(word)+1
    print(f"{' '.join(result)}")
if count1 == len(word):
    print("You won")
else:
    print("You lost")
    print(f"the word was: {word}")
print("Game over")
