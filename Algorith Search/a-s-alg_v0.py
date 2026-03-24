import random
import time
import os
import sys

db = 0

#v0 not finished. ALG integrated in v1


# --- INPUT CONFIGURATION START ---

try:
    import msvcrt
    IS_WINDOWS = True
except ImportError:
    IS_WINDOWS = False

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
      print(grid[3][0], grid[3][1], grid[3][2], grid[3][3])
      print("-------")


def main():
   
    pr = 3
    pc = 3
    
    print("\n■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")
    print("Solution:")
    visualize(grid)

    print("Go!")


    wasd = ['w', 'a', 's', 'd']
    for i in wasd:








     while True:
       
        i=get_single_keypress()
        
        if i=='r':
          allowed = ['w', 'a', 's', 'd']
          action_list = random.choices(allowed, k=20)
          for r in action_list:
            if r=='w':
              grid[(pr+0)%4][pc] = grid[(pr+1)%4][pc]
              grid[(pr+1)%4][pc] = grid[(pr+2)%4][pc]
              grid[(pr+2)%4][pc] = grid[(pr+3)%4][pc]
              grid[(pr-1)%4][pc] = "_"
              visualize(grid, 1)
              pr=(pr-1)%4
   
       
            if r=='s':
              grid[(pr-0)%4][pc] = grid[(pr-1)%4][pc]
              grid[(pr-1)%4][pc] = grid[(pr-2)%4][pc]
              grid[(pr-2)%4][pc] = grid[(pr-3)%4][pc]
              grid[(pr+1)%4][pc] = "_"
              visualize(grid, 1)
              pr=(pr+1)%4
         
            if r=='a':
              grid[pr][(pc+0)%4] = grid[pr][(pc+1)%4]
              grid[pr][(pc+1)%4] = grid[pr][(pc+2)%4]
              grid[pr][(pc+2)%4] = grid[pr][(pc+3)%4]
              grid[pr][(pc-1)%4]= "_"
              visualize(grid, 1)
              pc=(pc-1)%4
   
       
            if r=='d':
              grid[pr][(pc-0)%4] = grid[pr][(pc-1)%4]
              grid[pr][(pc-1)%4] = grid[pr][(pc-2)%4]
              grid[pr][(pc-2)%4] = grid[pr][(pc-3)%4]
              grid[pr][(pc+1)%4]= "_"
              visualize(grid, 1)
              pc=(pc+1)%4
            
          visualize(grid)
          
        if i=='w':
            grid[(pr+0)%4][pc] = grid[(pr+1)%4][pc]
            grid[(pr+1)%4][pc] = grid[(pr+2)%4][pc]
            grid[(pr+2)%4][pc] = grid[(pr+3)%4][pc]
            grid[(pr-1)%4][pc] = "_"
            visualize(grid)
            pr=(pr-1)%4
   
       
        if i=='s':
            grid[(pr-0)%4][pc] = grid[(pr-1)%4][pc]
            grid[(pr-1)%4][pc] = grid[(pr-2)%4][pc]
            grid[(pr-2)%4][pc] = grid[(pr-3)%4][pc]
            grid[(pr+1)%4][pc] = "_"
            visualize(grid)
            pr=(pr+1)%4
       
        if i=='a':
            grid[pr][(pc+0)%4] = grid[pr][(pc+1)%4]
            grid[pr][(pc+1)%4] = grid[pr][(pc+2)%4]
            grid[pr][(pc+2)%4] = grid[pr][(pc+3)%4]
            grid[pr][(pc-1)%4]= "_"
            visualize(grid)
            pc=(pc-1)%4
   
       
        if i=='d':
            grid[pr][(pc-0)%4] = grid[pr][(pc-1)%4]
            grid[pr][(pc-1)%4] = grid[pr][(pc-2)%4]
            grid[pr][(pc-2)%4] = grid[pr][(pc-3)%4]
            grid[pr][(pc+1)%4]= "_"
            visualize(grid)
            pc=(pc+1)%4
       
        if i=='q':
            break
            
        

       
       
   
   
   
main()
