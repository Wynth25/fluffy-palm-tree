import itertools

# -1 – Created, Opening
# 0 – Created, Opening: combo, diff_count
# 1 – Created, Opening: combo, visual, diff_count
# 2 – Created, Opening: combo, moves, diff_count

debug = -1
upper_range = 5


def printd(content):
		if debug >= 0:
			print(content)


def visualize(grid, reqdb=0):
		a = 0
		if reqdb == 1:
				if debug == 1:
						a = 1
				else:
						a = 0
		if reqdb == 2:
				if debug == 2:
						a = 1
				else:
						a = 0
		if reqdb == 0:
				a = 1

		if a == 1:
				print("")
				print(grid[0][0], grid[0][1], grid[0][2], grid[0][3])
				print(grid[1][0], grid[1][1], grid[1][2], grid[1][3])
				print(grid[2][0], grid[2][1], grid[2][2], grid[2][3])
				print(grid[3][0], grid[3][1], grid[3][2], grid[3][3])
				print("")
				


def gv_seq(current_seq, target_len, current_list):
		global allowed


		if len(current_seq) == target_len:
				current_list.append(current_seq)
				return
				
		for char in allowed:
				if (char == current_seq[-1] and char in "sd") or current_seq[-1] == allowed[(allowed.index(char) + 2) % 4]:
						continue
				if len(current_seq) >= 2:
						suffix = current_seq[-2:]
						if suffix == char * 2:
								continue

								'''
				if len(current_seq) >= 1:
						suff = current_seq[-1]
						if suff xxx(opak)xxx char
								'''

						gv_seq(current_seq + char, target_len, current_list)


allowed = ['w', 'a', 's', 'd']
wasd_lists = {}

for length in range(1, upper_range+1):
		for start_char in allowed:
				list_name = f"al_{start_char}{length}"
				current_list = []
				gv_seq(start_char, length, current_list)
				wasd_lists[list_name] = current_list
				print(f"Created folder: {list_name}")




print(f"\nCreated {length} folders!\n")


a_wasd_result = []

for label, data_list in wasd_lists.items():

		# label ------> 'al_w1', 'al_a1'...
		# data_list --> ['wwww', 'wwwa'...]

		print(f"Opening folder: {label}")

		for combo in data_list:

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

				flat_list = []
				flat_list = list(itertools.chain.from_iterable(grid))
				#print(flat_list)
		
				flat_list_num = [16 if x == '_' else x for x in flat_list]
				flat_list_num = [int(i, 16) if isinstance(i, str) else i for i in flat_list_num]
				#print(flat_list_num)
				a_wasd_result.append(tuple(flat_list_num))

a_wasd_result.sort()


# test a_wasd_result.append([7, 3, 12, 6, 9, 10, 5, 4, 13, 14, 11, 16, 2, 15, 8, 1])



dupls = []
dupls_count = 0
wasd_count = 0

from collections import Counter

# Count them
wasd_counts = Counter(a_wasd_result)
# Print any grid that appears more than once
for grid, count in wasd_counts.items():
		if count > 1:
				#print(f"Duplicate found! {grid} appears {count} times.")
				dupls.append(grid)
				dupls_count += count - 1
		wasd_count += 1
# Output: Duplicate found! (2, 3, 1) appears 2 times.

print(f"Total unique count: {wasd_count}")
print(f"Duplicates: {dupls_count}")



print("finito\n\n")
