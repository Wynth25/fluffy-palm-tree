import sys

# --- INPUT CONFIGURATION START ---

# We check if 'msvcrt' is available (only exists on Windows)
try:
    import msvcrt
    IS_WINDOWS = True
except ImportError:
    IS_WINDOWS = False

def get_single_keypress():
    """
    detects a keypress based on the operating system.
    Returns: a single character string (e.g., 'w') or None.
    """
    
    # === WINDOWS MODE (Instant 'w', 'a', 's', 'd') ===
    if IS_WINDOWS:
        # getch() pauses the program until you press a key.
        # It reads the key raw, without hitting Enter.
        key_byte = msvcrt.getch()

        # DECODING: Windows gives us bytes (b'w'), we need a string ('w')
        try:
            char = key_byte.decode('utf-8').lower()
            return char
        except UnicodeDecodeError:
            # This happens if you press a special key like F1 or Delete
            return None

    # === IOS / PYTHONISTA MODE (Fallback) ===
    else:
        # On Pythonista console, we CANNOT get raw keystrokes easily.
        # We must use standard input where you press 'w' then 'Enter'.
        try:
            text = input("Move (w/a/s/d): ")
            if len(text) > 0:
                return text[0].lower() # Return just the first letter
            return None
        except (KeyboardInterrupt, EOFError):
            return "q" # Safety exit if the user tries to force quit

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
			grid[pr][pc] = grid[(pr+1)%4][pc]
			grid[(pr+0)%4][pc] = grid[(pr+1)%4][pc]
			grid[(pr+1)%4][pc] = grid[(pr+2)%4][pc]
			grid[(pr+2)%4][pc] = grid[(pr+3)%4][pc]
			grid[(pr-1)%4][pc] = "_"
			visualize(grid)
			pr=pr-1
		
		
		i=input()
			
		if i=='w':
			grid[pr][pc] = grid[(pr+1)%4][pc]
			grid[(pr+0)%4][pc] = grid[(pr+1)%4][pc]
			grid[(pr+1)%4][pc] = grid[(pr+2)%4][pc]
			grid[(pr+2)%4][pc] = grid[(pr+3)%4][pc]
			grid[(pr-1)%4][pc] = "_"
			visualize(grid)
			pr=pr-1
		
		
		
		
		
		'''
		
		r = 0
		c = 0
		
		
		while r<4:
		   while c<4:
		       if c==pc:
		           grid[pr][pc] = "_"
		           print("HERE")
		           visualize(grid)
		           c=c+1
		       else:
		           print(c, "c")
		           c=c+1
		   if r == pr:
		       grid[pr][pc] = "_"
		       print("HERE")
		       visualize(grid)
		       r=r+1
		   else:
		       print(r, "r")
		       r=r+1
		
		'''
		
	
	
	
	
main()
