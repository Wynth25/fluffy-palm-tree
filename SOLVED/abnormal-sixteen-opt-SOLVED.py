import random
import time
import os
import sys

db = 0
solution = 1
allowed = ['w', 'a', 's', 'd']

# --- INPUT CONFIGURATION START ---

try:
    import msvcrt
    IS_WINDOWS = True
except ImportError:
    IS_WINDOWS = False

try:
    import console
    IS_PYTHONISTA = True
except ImportError:
    IS_PYTHONISTA = False
    
def get_single_keypress():
    # === WINDOWS MODE (Instant 'w', 'a', 's', 'd') ===
    if IS_WINDOWS:
        key_byte = msvcrt.getch()
        try:
            char = key_byte.decode('utf-8').lower()
            return char
        except UnicodeDecodeError:
            return None

    # === IOS / PYTHONISTA MODE (Fallback) ===
    else:
        try:
            text = input("Move (w/a/s/d): ")
            if len(text) > 0:
                return text[0].lower()
            return None
        except (KeyboardInterrupt, EOFError):
            return "q"

# --- INPUT CONFIGURATION END ---

def clear_screen(shuffle):
    if IS_PYTHONISTA:
        console.clear()
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
    print("Solution:")
    visualize(start_grid)

    print("="*35,shuffle,"="*35,"", sep="\n")


def gv_shuffle(target_len, shuffle_seq=""):
    global allowed 
    if len(shuffle_seq) == 0:
        shuffle_seq += random.choice(allowed)
    while len(shuffle_seq) < target_len:
        char = random.choice(allowed)
        
        # Rule 1: No opposites, and no 'ss' or 'dd'
        if (char == shuffle_seq[-1] and char in "sd") or shuffle_seq[-1] == allowed[(allowed.index(char) + 2) % 4]:
            continue
            
        # Rule 2: No triple repeats ('www' or 'aaa')
        if len(shuffle_seq) >= 2:
            suffix = shuffle_seq[-2:]
            if suffix == char * 2:
                continue
                
        # If the character passes all tests, append it!
        shuffle_seq += char
        
    return shuffle_seq

start_grid = [
[ 1, 2, 3 , 4 ],
[ 5, 6, 7, 8 ],
[ 9, "a", "b", "c" ],
[ "d", "e", "f", "_" ]
]

grid = [
[ 1, 2, 3 , 4 ],
[ 5, 6, 7, 8 ],
[ 9, "a", "b", "c" ],
[ "d", "e", "f", "_" ]
]


def visualize(grid, reqdb=0):
   if reqdb==1:
      if db==1:
         a=1
      else:
         a=0
   else:
      a=1
   if a==1:
      print(grid[0][0], grid[0][1], grid[0][2], grid[0][3])
      print(grid[1][0], grid[1][1], grid[1][2], grid[1][3])
      print(grid[2][0], grid[2][1], grid[2][2], grid[2][3])
      print(grid[3][0], grid[3][1], grid[3][2], grid[3][3], "\n")



def main():
   
    pr = 3
    pc = 3
    
    print("Solution:")
    visualize(grid)
    
    shuffle_seq = ""
    shuffle = gv_shuffle(5, shuffle_seq)

    if db == 1:
        print("Shuffling:")
    for i in shuffle:
        if i=='w':
            grid[(pr+0)%4][pc] = grid[(pr+1)%4][pc]
            grid[(pr+1)%4][pc] = grid[(pr+2)%4][pc]
            grid[(pr+2)%4][pc] = grid[(pr+3)%4][pc]
            grid[(pr-1)%4][pc] = "_"
            visualize(grid, 1)
            pr=(pr-1)%4
   
       
        if i=='s':
            grid[(pr-0)%4][pc] = grid[(pr-1)%4][pc]
            grid[(pr-1)%4][pc] = grid[(pr-2)%4][pc]
            grid[(pr-2)%4][pc] = grid[(pr-3)%4][pc]
            grid[(pr+1)%4][pc] = "_"
            visualize(grid, 1)
            pr=(pr+1)%4
       
        if i=='a':
            grid[pr][(pc+0)%4] = grid[pr][(pc+1)%4]
            grid[pr][(pc+1)%4] = grid[pr][(pc+2)%4]
            grid[pr][(pc+2)%4] = grid[pr][(pc+3)%4]
            grid[pr][(pc-1)%4]= "_"
            visualize(grid, 1)
            pc=(pc-1)%4
   
       
        if i=='d':
            grid[pr][(pc-0)%4] = grid[pr][(pc-1)%4]
            grid[pr][(pc-1)%4] = grid[pr][(pc-2)%4]
            grid[pr][(pc-2)%4] = grid[pr][(pc-3)%4]
            grid[pr][(pc+1)%4]= "_"
            visualize(grid, 1)
            pc=(pc+1)%4
    
    if solution == 0:
        shuffle = "May the odds be ever in your favor."
    print("="*35,shuffle,"="*35,"", sep="\n")
    visualize(grid)

    move_counter = 0
    while True:
        move_counter += 1
        i=get_single_keypress()
        if i=='w':
            grid[(pr+0)%4][pc] = grid[(pr+1)%4][pc]
            grid[(pr+1)%4][pc] = grid[(pr+2)%4][pc]
            grid[(pr+2)%4][pc] = grid[(pr+3)%4][pc]
            grid[(pr-1)%4][pc] = "_"
            clear_screen(shuffle)
            visualize(grid)
            pr=(pr-1)%4
   
       
        if i=='s':
            grid[(pr-0)%4][pc] = grid[(pr-1)%4][pc]
            grid[(pr-1)%4][pc] = grid[(pr-2)%4][pc]
            grid[(pr-2)%4][pc] = grid[(pr-3)%4][pc]
            grid[(pr+1)%4][pc] = "_"
            clear_screen(shuffle)
            visualize(grid)
            pr=(pr+1)%4
       
        if i=='a':
            grid[pr][(pc+0)%4] = grid[pr][(pc+1)%4]
            grid[pr][(pc+1)%4] = grid[pr][(pc+2)%4]
            grid[pr][(pc+2)%4] = grid[pr][(pc+3)%4]
            grid[pr][(pc-1)%4]= "_"
            clear_screen(shuffle)
            visualize(grid)
            pc=(pc-1)%4
   
       
        if i=='d':
            grid[pr][(pc-0)%4] = grid[pr][(pc-1)%4]
            grid[pr][(pc-1)%4] = grid[pr][(pc-2)%4]
            grid[pr][(pc-2)%4] = grid[pr][(pc-3)%4]
            grid[pr][(pc+1)%4]= "_"
            clear_screen(shuffle)
            visualize(grid)
            pc=(pc+1)%4
       
        if grid == start_grid:
            print(f"\nSuccess! Took {move_counter} moves.\n")
            break
   
   
   
main()
