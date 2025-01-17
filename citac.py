import os
import time
import random
import msvcrt

BOARD_WIDTH = 20
BOARD_HEIGHT = 5
DIFFICULTY = 4  # Smanjeno na 4 da uspori igru

def create_fruit(tail_positions):
    fruit_position = [random.randint(1, BOARD_WIDTH), random.randint(1, BOARD_HEIGHT)]
    while fruit_position in tail_positions:
        fruit_position = [random.randint(1, BOARD_WIDTH), random.randint(1, BOARD_HEIGHT)]
    return fruit_position

def create_board(fruit_position, head_position, tail_positions):
    board = ''
    for i in range(BOARD_HEIGHT + 2):
        for j in range(BOARD_WIDTH + 2):
            if i == 0 or j == 0 or i == BOARD_HEIGHT + 1 or j == BOARD_WIDTH + 1:
                board += '#'
            elif fruit_position == [j, i]:
                board += 'F'
            elif head_position == [j, i]:
                board += 'O'
            elif [j, i] in tail_positions:
                board += 'o'
            else:
                board += ' '
        board += '\n'
    return board

def draw(fruit_position, head_position, tail_positions, score):
    tail_positions.pop(0)
    tail_positions.append(head_position.copy())
    board = create_board(fruit_position, head_position, tail_positions)
    os.system('cls')  # Za Linux/Mac koristi 'clear'
    print(board)
    print('Score:', score)

def get_pressed_key():
    if msvcrt.kbhit():
        return msvcrt.getch().decode()
    else:
        return ''

def change_side(head_position):
    if head_position[0] == 0:
        head_position[0] = BOARD_WIDTH
    elif head_position[0] == BOARD_WIDTH + 1:
        head_position[0] = 1
    if head_position[1] == 0:
        head_position[1] = BOARD_HEIGHT
    elif head_position[1] == BOARD_HEIGHT + 1:
        head_position[1] = 1
    return head_position

def move(head_position, directions):
    key = get_pressed_key()
    if key == 'd' and directions['LEFT'] == False:
        head_position[0] += 1
        directions['UP'] = False
        directions['DOWN'] = False
        directions['RIGHT'] = True
    elif key == 'a' and directions['RIGHT'] == False:
        head_position[0] -= 1
        directions['UP'] = False
        directions['DOWN'] = False
        directions['LEFT'] = True
    elif key == 's' and directions['UP'] == False:
        head_position[1] += 1
        directions['RIGHT'] = False
        directions['LEFT'] = False
        directions['DOWN'] = True
    elif key == 'w' and directions['DOWN'] == False:
        head_position[1] -= 1
        directions['RIGHT'] = False
        directions['LEFT'] = False
        directions['UP'] = True
    else:
        if directions['RIGHT'] == True:
            head_position[0] += 1
        elif directions['LEFT'] == True:
            head_position[0] -= 1
        elif directions['DOWN'] == True:
            head_position[1] += 1
        elif directions['UP'] == True:
            head_position[1] -= 1

    head_position = change_side(head_position)
    return head_position

def main():
    head_position = [BOARD_WIDTH // 2, BOARD_HEIGHT // 2]
    tail_positions = [head_position.copy()]
    fruit_position = create_fruit(tail_positions)
    directions = {'RIGHT': True, 'LEFT': False, 'UP': False, 'DOWN': False}
    score = 0
    
    # Dodaj pauzu na početku kako bi igrač video šta se dešava
    time.sleep(2)
    
    while True:
        draw(fruit_position, head_position, tail_positions, score)
        head_position = move(head_position, directions)
        
        if head_position in tail_positions:
            break  # Kraj igre ako zmija udari u rep

        if head_position == fruit_position:
            tail_positions.append(head_position.copy())
            fruit_position = create_fruit(tail_positions)
            score += 9

        time.sleep(1 / DIFFICULTY)  # Smanjeno osvežavanje igre

main()

 
 

