import itertools
from collections import Counter

# visualize_debug 
# 1 -> Combo result
# 2 -> Combo progress


folders_debug = 1

combo_debug = 0
visualize_debug = 0
flat_list_debug = 0

counter_debug = 1


stop_after = 12					#prints 			-1 = all

optimized = 1
upper_range = 16


any_debug = combo_debug + flat_list_debug + visualize_debug
stop_after_initial_value = stop_after

import re

try:
	import console
	_in_pythonista = True
except ImportError:
	_in_pythonista = False

class t:
	# Groups
	grid = '\033[1;40;92m' 	# <<<<<<<
	folder = '\033[1;4;36m'	# <<<<<<<

	# Text Modifiers
	end = '\033[0m'						#<<<<<<<<
	bold = '\033[1m'					#<<<<<<<<
	underline = '\033[4m'			#<
	light_grey = '\033[37m'		#<<<<<<<<
	green = '\033[32m'				#<<<<<<<<
	blue = '\033[34m'					#<<<<<<<<
	cyan = '\033[36m'					#<
	bright_green = '\033[92m'	#<
	black_bg = '\033[40m'			#<

def cprint(text, **kwargs):
	"""Cross-platform colored print function."""
	if not _in_pythonista:
		# We are in VS Code. Print normally; the terminal handles the ANSI.
		print(text, **kwargs)
		return

	# We are in Pythonista. Intercept the ANSI codes.
	ansi_regex = re.compile(r'(\033\[[0-9;]*m)')
	parts = ansi_regex.split(str(text))

	# Map for Pythonista (inside cprint)
	color_map = {
		'32': (0, 0.8, 0),			# green
		'34': (0.4, 0.6, 1),	  	# blue (lightened slightly to be readable on black)
		'36': (0, 1, 1),		  	# cyan
		'37': (0.85, 0.85, 0.85), 	# light_grey 
		'92': (0.2, 1, 0.2)	   		# bright_green
	}

	for part in parts:
		if part.startswith('\033['):
			codes = part[2:-1].split(';')
			for code in codes:
				if code == '0':
					console.set_color()  # Reset everything
				elif code in color_map:
					console.set_color(*color_map[code]) 
				elif code == '4':
					console.set_color(1, 1, 0) # Replaces underline with Yellow
				# -------------------------------

		elif part:
			print(part, end="")

	# Apply the final newline (or whatever was passed in kwargs like end=" ")
	print(kwargs.get('end', '\n'), end="")
	console.set_color()  # Safety reset

print("")

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
		global allowed

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


allowed = ['w', 'a', 's', 'd']
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
				# Replaces the itertools line completely
				flat_list = [item for row in grid for item in row]


		
				flat_list_num = [16 if x == '_' else x for x in flat_list]
				flat_list_num = [int(i, 16) if isinstance(i, str) else i for i in flat_list_num]
				if flat_list_debug == 1:
					cprint(f"{t.blue}Flat list:{t.end} {flat_list_num}\n")
				a_wasd_result.append(tuple(flat_list_num))
				
				# Go through the entire database and mask every grid
				

a_wasd_result.sort()



from collections import Counter


print("\n" + "="*30)
cprint(f"{t.bold}{t.blue}MASKED VISUAL GRIDS {t.end}")
print("="*30)


visual_grids_99 = [tuple(x if x in (1,2,3,4,16) else 99 for x in grid) for grid in a_wasd_result]

visual_grids_99.sort()

visual_grids_ = [tuple(" " if x == 99 else (0 if x == 16 else x) for x in grid) for grid in visual_grids_99]

visual_counts = Counter(visual_grids_)


unique_lines = 0

if counter_debug == 1:
	for grid, count in visual_counts.items():
	# Joins everything with a single space to remove the string quotes
		clean_grid = " ".join(str(item) for item in grid)
		print(f"{clean_grid}  ->  {count} times")
		stop_after -= 1
		unique_lines += 1
		if stop_after == 0:
			break


if stop_after_initial_value > 0:
	print("" + "="*30)
	cprint(f"{t.bold}{t.cyan}Printed {stop_after_initial_value} lines.{t.end}")
print("="*30)



print(f"Total: {unique_lines}")
cprint(f"{t.bold}{t.green}\nfinito\n\n{t.end}")

