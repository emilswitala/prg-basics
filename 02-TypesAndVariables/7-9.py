# dice number is either 1 or 6 - true, otherwise false

import random
dice = random.randint(1,6)

good_dice = dice == 1 or dice == 6
bad_dice = dice != 1 and dice != 6

print(f'Your dice number was {dice}. Your dice number is special!: {good_dice}')