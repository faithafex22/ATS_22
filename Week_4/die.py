"""Roll a six-sided die 6,000,000 times."""
import random

 # face frequency counters
frequency1 = 0
frequency2 = 0
frequency3 = 0
frequency4 = 0
frequency5 = 0
frequency6 = 0

# 6,000,000 die rolls
for roll in range(6_000_000): # note underscore separators
    face = random.randrange(1, 7)


    #increment appropriate face counter
    if face == 1:
        frequency1 += 1
    elif face == 2:
        frequency2 += 1
    elif face == 3:
        frequency3 += 1
    elif face == 4:
        frequency4 += 1
    elif face == 5:
        frequency5 += 1
    elif face == 6:
        frequency6 += 1

print(f'Face{"Frequency":>6}')
print(f'{1:>1}{frequency1:>13}')
print(f'{2:>1}{frequency2:>13}')
print(f'{3:>1}{frequency3:>13}')
print(f'{4:>1}{frequency4:>13}')
print(f'{5:>1}{frequency5:>13}')
print(f'{6:>1}{frequency6:>13}')

name = "Faith"
surname = "Adeosun"

print(f"{name} {surname}")