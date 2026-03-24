import random
import time
import os
import sys

db = 0
solution = 0
demonstration = 0
allowed = ['w', 'a', 's', 'd']

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

move_counter = 0

if demonstration == 1:
    delay = 0.01
else:
    delay = 0
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

def clear_screen(shuffle, move_counter):
    if IS_PYTHONISTA:
        console.clear()
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
    print("Solution:")
    visualize(start_grid)
    if solution == 0:
        shuffle = "May the odds be ever in your favor."
    print("="*35,shuffle,"="*35,"",f"Moves: {move_counter}","", sep="\n")

def gv_shuffle(target_len, shuffle_seq=""):
    global allowed 
    if len(shuffle_seq) == 0:
        shuffle_seq += random.choice(allowed)
    while len(shuffle_seq) < target_len:
        char = random.choice(allowed)
        
        # No WS no SS&DD
        if (char == shuffle_seq[-1] and char in "sd") or shuffle_seq[-1] == allowed[(allowed.index(char) + 2) % 4]:
            continue
            
        # No WWW
        if len(shuffle_seq) >= 2:
            suffix = shuffle_seq[-2:]
            if suffix == char * 2:
                continue
                
        shuffle_seq += char
        
    return shuffle_seq

def move_yo_a16(i, grid, pr, pc, solution, move_counter=0, wait=0):
    if i=='w':
        grid[(pr+0)%4][pc] = grid[(pr+1)%4][pc]
        grid[(pr+1)%4][pc] = grid[(pr+2)%4][pc]
        grid[(pr+2)%4][pc] = grid[(pr+3)%4][pc]
        grid[(pr-1)%4][pc] = "_"
        pr=(pr-1)%4
   
       
    elif i=='s':
        grid[(pr-0)%4][pc] = grid[(pr-1)%4][pc]
        grid[(pr-1)%4][pc] = grid[(pr-2)%4][pc]
        grid[(pr-2)%4][pc] = grid[(pr-3)%4][pc]
        grid[(pr+1)%4][pc] = "_"
        pr=(pr+1)%4
       
    elif i=='a':
        grid[pr][(pc+0)%4] = grid[pr][(pc+1)%4]
        grid[pr][(pc+1)%4] = grid[pr][(pc+2)%4]
        grid[pr][(pc+2)%4] = grid[pr][(pc+3)%4]
        grid[pr][(pc-1)%4]= "_"
        pc=(pc-1)%4
   
       
    elif i=='d':
        grid[pr][(pc-0)%4] = grid[pr][(pc-1)%4]
        grid[pr][(pc-1)%4] = grid[pr][(pc-2)%4]
        grid[pr][(pc-2)%4] = grid[pr][(pc-3)%4]
        grid[pr][(pc+1)%4]= "_"
        pc=(pc+1)%4
    
    elif i in 'gj':
        if solution == 1:
            for i in "wwawdwwawawdwwawawwdwawawwdwa":
                pr, pc, move_counter = move_yo_a16(i, grid, pr, pc, solution, move_counter, delay)
                clear_screen("Super W!", move_counter)
                visualize(grid)
            return pr, pc, move_counter
        
    elif i in 'vk':
        if solution == 1:
            for i in "aasawaasasawaasasaawasasaawas":
                pr, pc, move_counter = move_yo_a16(i, grid, pr, pc, solution, move_counter, delay)
                clear_screen("Super A!", move_counter)
                visualize(grid)
            return pr, pc, move_counter
        
    elif i in 'bu':
        if solution == 1:
            for i in "ssdsassdsdsassdsdssasdsdssasd":
                pr, pc, move_counter = move_yo_a16(i, grid, pr, pc, solution, move_counter, delay)
                clear_screen("Super D!", move_counter)
                visualize(grid)
            return pr, pc, move_counter
        
    elif i in 'nh':
        if solution == 1:
            for i in "ddwdsddwdwdsddwdwddsdwdwddsdw":
                pr, pc, move_counter = move_yo_a16(i, grid, pr, pc, solution, move_counter, delay)
                clear_screen("Super S!", move_counter)
                visualize(grid)
            return pr, pc, move_counter
    	
    time.sleep(wait)
    move_counter += 1
    return pr, pc, move_counter

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
    shuffle = gv_shuffle(30, shuffle_seq)

    if db == 1:
        print("Shuffling:")
    for i in shuffle:
        pr, pc, move_counter = move_yo_a16(i, grid, pr, pc, solution, move_counter=-1)
    
    if solution == 0:
        shuffle = "May the odds be ever in your favor."
    print("="*35,shuffle,"="*35,"", sep="\n")
    visualize(grid)

    while True:
        i=get_single_keypress()
        if i=='q':
        	break
        pr, pc, move_counter = move_yo_a16(i, grid, pr, pc, solution, move_counter)
        clear_screen(shuffle, move_counter)
        visualize(grid)
       
        if grid == start_grid:
            print(f"\nSuccess! Took {move_counter} moves.\n")
            break
   
main()
