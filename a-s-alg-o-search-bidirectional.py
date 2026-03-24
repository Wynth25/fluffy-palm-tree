import itertools

# -1 – Created, Opening
# 0 – Created, Opening: combo, diff_count
# 1 – Created, Opening: combo, visual, diff_count
# 2 – Created, Opening: combo, moves, diff_count
debug = -1

#15 – in range(1, 16)
upper_range = 15


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
	
	print(f"A: Opening folder: {label}")
	
	
	for combo in data_list:
	
		pr = 3
		pc = 3
		
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
		a_wasd_result.append((tuple(flat_list_num), (combo)))

a_wasd_result.sort()
#print(a_wasd_result)

b_wasd_result = []

for label, data_list in wasd_lists.items():

	# label ------> 'al_w1', 'al_a1'...
	# data_list --> ['wwww', 'wwwa'...]
	
	print(f"B: Opening folder: {label}")
	
	for combo in data_list:
	
		pr = 3
		pc = 3
		
		grid2 = [
		[1, 2, 3, 4],
		[5, 6, 7, 8],
		[9, "a", "b", "c"],
		["e", "f", "d", "_"]
		]
		
		for item_combo in combo:
		
			if item_combo == 'w':
				grid2[(pr + 0) % 4][pc] = grid2[(pr + 1) % 4][pc]
				grid2[(pr + 1) % 4][pc] = grid2[(pr + 2) % 4][pc]
				grid2[(pr + 2) % 4][pc] = grid2[(pr + 3) % 4][pc]
				grid2[(pr - 1) % 4][pc] = "_"
				visualize(grid2, 2)
				pr = (pr - 1) % 4
				
			if item_combo == 's':
				grid2[(pr - 0) % 4][pc] = grid2[(pr - 1) % 4][pc]
				grid2[(pr - 1) % 4][pc] = grid2[(pr - 2) % 4][pc]
				grid2[(pr - 2) % 4][pc] = grid2[(pr - 3) % 4][pc]
				grid2[(pr + 1) % 4][pc] = "_"
				visualize(grid2, 2)
				pr = (pr + 1) % 4
				
			if item_combo == 'a':
				grid2[pr][(pc + 0) % 4] = grid2[pr][(pc + 1) % 4]
				grid2[pr][(pc + 1) % 4] = grid2[pr][(pc + 2) % 4]
				grid2[pr][(pc + 2) % 4] = grid2[pr][(pc + 3) % 4]
				grid2[pr][(pc - 1) % 4] = "_"
				visualize(grid2, 2)
				pc = (pc - 1) % 4
				
			if item_combo == 'd':
				grid2[pr][(pc - 0) % 4] = grid2[pr][(pc - 1) % 4]
				grid2[pr][(pc - 1) % 4] = grid2[pr][(pc - 2) % 4]
				grid2[pr][(pc - 2) % 4] = grid2[pr][(pc - 3) % 4]
				grid2[pr][(pc + 1) % 4] = "_"
				visualize(grid2, 2)
				pc = (pc + 1) % 4
				
		flat_list = []
		flat_list = list(itertools.chain.from_iterable(grid2))
		#print(flat_list)
			
		flat_list_num = [16 if x == '_' else x for x in flat_list]
		flat_list_num = [int(i, 16) if isinstance(i, str) else i for i in flat_list_num]
		#print(flat_list_num)
		b_wasd_result.append((tuple(flat_list_num), (combo)))

b_wasd_result.sort()
#print(b_wasd_result)

idx_a = 0
idx_b = 0
matches = 0

while idx_a < len(a_wasd_result) and idx_b < len(b_wasd_result):
	grid_a, combo_a= a_wasd_result[idx_a]
	grid_b, combo_b= b_wasd_result[idx_b]
	if grid_a == grid_b:
		print("success!!!")
		print(f"Combo A: {combo_a}")
		print(f"Combo B: {combo_b}")
		idx_a += 1
		idx_b += 1
		matches += 1
	elif grid_a < grid_b:
		idx_a += 1
	else:
		idx_b += 1
	#print(idx_a, idx_b)
print(matches)

			
'''
        diff_count = 0


        for sub_grid_start, sub_grid in zip(grid_start, grid):
            for item_grid_start, item_grid in zip(sub_grid_start, sub_grid):
                if item_grid_start != item_grid:
                    diff_count += 1

        if diff_count != -1:
            printd(f"COMBINATION: {combo} {len(combo)}")
            visualize(grid, 1)
            printd(f"DIFFERENCES: {diff_count}\n")
            printd("——––––––––––––––")
            printd("")
            if diff_count == 0:
                print(combo)
                visualize(grid)
                input()
'''

print("finito\n\n")

