import random
# Comment**
# print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518")      ● ┌ ─ ┐ │ └ ┘

"┌─────────┐"
"│         │"
"│         │"
"│         │"
"└─────────┘"

dice_art = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘")
}

dice = []
total = 0
num_of_dice = int(input("How many dice?: "))

for die in range(num_of_dice):
    dice.append(random.randint(1,6))

for die in range(num_of_dice):                          # for line in range(5):
    for line in dice_art.get(dice[die]):                #   for die in dice:
        print(line)                                     #       print(dice_art.get(die[line],end=""))
                                                        #   print()
for die in dice:
    total += die
print(f"total: {total}")



'''The program simulates rolling two dice, displays their visual representations, 
and calculates the total value obtained from the roll.'''

# OUTPUT
How many dice?: 2
┌─────────┐
│  ●      │
│    ●    │
│      ●  │
└─────────┘
┌─────────┐
│  ●   ●  │
│    ●    │
│  ●   ●  │
└─────────┘
total: 8

How many dice?: 2
┌─────────┐
│         │
│    ●    │
│         │
└─────────┘
┌─────────┐
│  ●   ●  │
│         │
│  ●   ●  │
└─────────┘
total: 5
