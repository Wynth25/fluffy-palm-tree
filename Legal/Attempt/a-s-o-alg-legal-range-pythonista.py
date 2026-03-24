import itertools


# visualize_debug 
# 1 -> Combo result
# 2 -> Combo progress


folders_debug = 1

combo_debug = 1
visualize_debug = 1
flat_list_debug = 1

counter_debug = 1



optimized = 1
repeats = 2


any_debug = combo_debug + flat_list_debug + visualize_debug

import re

try:
    import console
    _in_pythonista = True
except ImportError:
    _in_pythonista = False


class t:
    # Groups
    grid = '\033[1;40;92m'  # VS Code: Bold, Black BG, Bright Green text
    folder = '\033[1;4;36m'

    # Text Modifiers
    end = '\033[0m'
    bold = '\033[1m'
    dim = '\033[2m'
    italic = '\033[3m'
    underline = '\033[4m'
    invert = '\033[7m'
    strikethrough = '\033[9m'

    # Greys
    light_grey = '\033[37m'
    dark_grey = '\033[90m'

    # Standard Text Colors
    black = '\033[30m'
    red = '\033[31m'
    green = '\033[32m'
    yellow = '\033[33m'
    blue = '\033[34m'
    magenta = '\033[35m'
    cyan = '\033[36m'
    white = '\033[97m' # Bright white

    # Bright / High-Intensity Text Colors
    bright_black = '\033[90m'  
    bright_red = '\033[91m'
    bright_green = '\033[92m'
    bright_yellow = '\033[93m'
    bright_blue = '\033[94m'
    bright_magenta = '\033[95m'
    bright_cyan = '\033[96m'
    bright_white = '\033[97m'

    # Background Colors
    black_bg = '\033[40m'
    red_bg = '\033[41m'
    green_bg = '\033[42m'
    yellow_bg = '\033[43m'
    blue_bg = '\033[44m'
    magenta_bg = '\033[45m'
    cyan_bg = '\033[46m'
    white_bg = '\033[47m'


def cprint(text, **kwargs):
    """Cross-platform colored print function."""
    if not _in_pythonista:
        # We are in VS Code. Print normally; the terminal handles the ANSI.
        print(text, **kwargs)
        return

    # We are in Pythonista. Intercept the ANSI codes.
    ansi_regex = re.compile(r'(\033\[[0-9;]*m)')
    parts = ansi_regex.split(str(text))

    # Map standard ANSI numbers to Pythonista RGB color tuples
    color_map = {
        '30': (0, 0, 0),       '31': (1, 0.2, 0.2),   '32': (0, 0.8, 0),
        '33': (1, 1, 0),       '34': (0, 0, 1),       '35': (1, 0, 1),
        
        # --- UPDATED GREYS ---
        '37': (0.85, 0.85, 0.85), # Light Grey (Brighter, easy to read)
        '90': (0.55, 0.55, 0.55), # Dark Grey (Boosted so it doesn't vanish)
        # ---------------------
        
        '91': (1, 0.2, 0.2),   '92': (0.2, 1, 0.2),   
        '93': (1, 1, 0.2),     '94': (0.3, 0.3, 1),   '95': (1, 0.2, 1),
        '96': (0.2, 1, 1),     '97': (1, 1, 1)        
    }

    for part in parts:
        if part.startswith('\033['):
            # Extract the numbers (e.g., '1;40;92' from '\033[1;40;92m')
            codes = part[2:-1].split(';')
            for code in codes:
                if code == '0':
                    console.set_color()  # Reset everything
                elif code in color_map:
                    console.set_color(*color_map[code]) # Apply RGB tuple
                # Note: '40' (background) and '1' (bold) are safely ignored here
        elif part:
            # Print the actual text without dropping to a new line yet
            print(part, end="")

    # Apply the final newline (or whatever was passed in kwargs like end=" ")
    print(kwargs.get('end', '\n'), end="")
    console.set_color()  # Safety reset



print("")
allowed = ['w', 'a', 's', 'd']

def visualize(grid, reqdb=0):
		a = 0
		if reqdb == 1:
				if visualize_debug == 1:
						a = 1
				else:
						a = 0
		if reqdb == 2:
				if visualize_debug == 2:
						a = 1
				else:
						a = 0

		if a == 1:
				cprint(f"{t.grid}{grid[0][0]} {grid[0][1]} {grid[0][2]} {grid[0][3]}{t.end}")
				cprint(f"{t.grid}{grid[1][0]} {grid[1][1]} {grid[1][2]} {grid[1][3]}{t.end}")
				cprint(f"{t.grid}{grid[2][0]} {grid[2][1]} {grid[2][2]} {grid[2][3]}{t.end}")
				cprint(f"{t.grid}{grid[3][0]} {grid[3][1]} {grid[3][2]} {grid[3][3]}{t.end}")
				if flat_list_debug == 0:
					print("")

				


def gv_seq(current_seq, target_len, current_list):
		
		if len(current_seq) == target_len:
				current_list.append(current_seq)
				return
		for char in allowed:
				if optimized == 1:
					if (char == current_seq[-1] and char in "sd") or current_seq[-1] == allowed[(allowed.index(char) + 2) % 4]:
							continue
					if len(current_seq) >= 2:
							suffix = current_seq[-2:]
							if suffix == char * 2:
									continue

				gv_seq(current_seq + char, target_len, current_list)


def main():

	wasd_lists = {}

	for length in range(1, upper_range+1):
			for start_char in allowed:
					list_name = f"al_{start_char}{length}"
					current_list = []
					gv_seq(start_char, length, current_list)
					wasd_lists[list_name] = current_list
					if folders_debug == 1:
						print(f"Created folder: {list_name}")



	if folders_debug == 1:
		print(f"\nCreated {length} * 4 folders!\n")


	a_wasd_result = []

	for label, data_list in wasd_lists.items():

			# label ------> 'al_w1', 'al_a1'...
			# data_list --> ['wwww', 'wwwa'...]
			if folders_debug == 1:
				cprint(f"{t.folder}Opening folder:{t.end} {label}")
			if any_debug > 0:
				print("")

			for combo in data_list:
					if combo_debug == 1:
						cprint(f"{t.light_grey}Combo:{t.end} {combo}")
					pr = 3
					pc = 3

	#				 wwasdwwawasasd

					grid = [
							[1, 2, 3, 4],
							[5, 6, 7, 8],
							[9, "a", "b", "c"],
							["d", "e", "f", "_"]
							]

					for item_combo in combo:

							if item_combo == 'w':
									grid[(pr + 0) % 4][pc] = grid[(pr + 1) % 4][pc]
									grid[(pr + 1) % 4][pc] = grid[(pr + 2) % 4][pc]
									grid[(pr + 2) % 4][pc] = grid[(pr + 3) % 4][pc]
									grid[(pr - 1) % 4][pc] = "_"
									visualize(grid, 2)
									pr = (pr - 1) % 4

							if item_combo == 's':
									grid[(pr - 0) % 4][pc] = grid[(pr - 1) % 4][pc]
									grid[(pr - 1) % 4][pc] = grid[(pr - 2) % 4][pc]
									grid[(pr - 2) % 4][pc] = grid[(pr - 3) % 4][pc]
									grid[(pr + 1) % 4][pc] = "_"
									visualize(grid, 2)
									pr = (pr + 1) % 4

							if item_combo == 'a':
									grid[pr][(pc + 0) % 4] = grid[pr][(pc + 1) % 4]
									grid[pr][(pc + 1) % 4] = grid[pr][(pc + 2) % 4]
									grid[pr][(pc + 2) % 4] = grid[pr][(pc + 3) % 4]
									grid[pr][(pc - 1) % 4] = "_"
									visualize(grid, 2)
									pc = (pc - 1) % 4

							if item_combo == 'd':
									grid[pr][(pc - 0) % 4] = grid[pr][(pc - 1) % 4]
									grid[pr][(pc - 1) % 4] = grid[pr][(pc - 2) % 4]
									grid[pr][(pc - 2) % 4] = grid[pr][(pc - 3) % 4]
									grid[pr][(pc + 1) % 4] = "_"
									visualize(grid, 2)
									pc = (pc + 1) % 4
					visualize(grid, 1)

					flat_list = []
					flat_list = list(itertools.chain.from_iterable(grid))

			
					flat_list_num = [16 if x == '_' else x for x in flat_list]
					flat_list_num = [int(i, 16) if isinstance(i, str) else i for i in flat_list_num]
					if flat_list_debug == 1:
						cprint(f"{t.blue}Flat list:{t.end} {flat_list_num}\n")
					a_wasd_result.append(tuple(flat_list_num))

	a_wasd_result.sort()


	# test a_wasd_result.append([7, 3, 12, 6, 9, 10, 5, 4, 13, 14, 11, 16, 2, 15, 8, 1])

	print("")

	dupls = []
	dupls_count = 0
	wasd_count = 0

	from collections import Counter


	wasd_counts = Counter(a_wasd_result)
	target_grid = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16)


	if counter_debug == 1 and optimized == 0:
		cprint(f"Original grid appeared {wasd_counts[target_grid]} times.\n")
	original_grid_count = wasd_counts[target_grid]

	del wasd_counts[target_grid]

	for grid, count in wasd_counts.items():
			if count > 1:
					dupls.append(grid)
					dupls_count += count - 1
			wasd_count += 1


	if counter_debug == 1:
		for grid, count in wasd_counts.items():
			cprint(f"{grid}  ->  {count} times")
		print("")


	print(f"Duplicates: 		{dupls_count:,}")
	if optimized == 0:
		print(f"Original grid: 		{original_grid_count:,}")
	cprint(f"\n{t.bold}{t.underline}Total unique count:	{wasd_count:,}{t.end}")
	print(f"Total grids count: 	{dupls_count + wasd_count:,}")
	if optimized == 0:
		print(f"Total inc original: 	{dupls_count + wasd_count + original_grid_count:,}")

	cprint(f"{t.bold}{t.green}\nFinito: {upper_range}\n\n{t.end}")


for upper_range in range (1, repeats + 1):
	main()
