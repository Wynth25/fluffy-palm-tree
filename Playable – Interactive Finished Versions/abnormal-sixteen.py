import sys

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

def visualize(grid):
   print(grid[0][0], grid[0][1], grid[0][2], grid[0][3])
   print(grid[1][0], grid[1][1], grid[1][2], grid[1][3])
   print(grid[2][0], grid[2][1], grid[2][2], grid[2][3])
   print(grid[3][0], grid[3][1], grid[3][2], grid[3][3])


def main():
	
	pr = 3
	pc = 3
	
	visualize(grid)
	
	
	
	while True:
		
		i=get_single_keypress()
		
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
