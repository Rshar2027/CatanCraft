import random


ores=['ore']*3
sheeps=['sheep']*4
bricks=['brick']*3
hays=['hay']*4
woods=['wood']*4
deserts=['desert']*1

recources = ores + sheeps + bricks + hays + woods + deserts

random.shuffle(recources)
random.shuffle(recources)
random.shuffle(recources)
random.shuffle(recources)
random.shuffle(recources)
random.shuffle(recources)
random.shuffle(recources)
random.shuffle(recources)
random.shuffle(recources)
random.shuffle(recources)
random.shuffle(recources)
random.shuffle(recources)
random.shuffle(recources)
random.shuffle(recources)
random.shuffle(recources)
random.shuffle(recources)
random.shuffle(recources)
random.shuffle(recources)
random.shuffle(recources)
random.shuffle(recources)
random.shuffle(recources)
random.shuffle(recources)
random.shuffle(recources)
random.shuffle(recources)
random.shuffle(recources)
random.shuffle(recources)
random.shuffle(recources)
random.shuffle(recources)
 
print(f"length: {len(recources)}")

board_recources = [
        ['-1', '-1'," ", " ", " ", "-1", "-1", ]
        ['-1', ' '," ", " ", " ", " ", "-1", ]
        [' ', ' '," ", " ", " ", " ", " ", ]
        [' ', ' '," ", " ", " ", " ", " ", ]
        [' ', ' '," ", " ", " ", " ", " ", ]
]
for row in range(5):
    for column in range(9):
        if board_recources[row][column] != '-1':
            board_recources[row][column] = recources.pop()


board_tokens=[2,3,4,5,6,8,9,10,11,12]
additional_tokens =[2,3,4,5,6,8,9,10,11,12]
random.shuffle(additional_tokens)
random.shuffle(additional_tokens)
random.shuffle(additional_tokens)
random.shuffle(additional_tokens)
random.shuffle(additional_tokens)
random.shuffle(additional_tokens)
random.shuffle(additional_tokens)
random.shuffle(additional_tokens)
random.shuffle(additional_tokens)
random.shuffle(additional_tokens)
random.shuffle(additional_tokens)
random.shuffle(additional_tokens)
random.shuffle(additional_tokens)
random.shuffle(additional_tokens)
random.shuffle(additional_tokens)
random.shuffle(additional_tokens)
random.shuffle(additional_tokens)
random.shuffle(additional_tokens)
random.shuffle(additional_tokens)
random.shuffle(additional_tokens)
random.shuffle(additional_tokens)
random.shuffle(additional_tokens)


while len(board_tokens) < 18:
        board_tokens.append(additional_tokens.pop())


board_numbers = [
        ['-1', '-1', '-1', ' ', ' ', ' ', '-1', '-1', '-1'],
        ['-1', '-1', ' ', ' ', ' ', ' ', ' ', '-1', '-1'],
        ['-1', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '-1'],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    ]

for row in range(5):
     for column in range(9):
          if board_tokens[row][column] != '-1':
               if board_tokens[row][column] !='desert':
                    board_numbers[row][column]=board_tokens.pop()




