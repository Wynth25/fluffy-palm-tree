debug = 1

def printd(content):
	if debug == 1:
		print(content)
	if debug == 2:
		print(content)

def visualize(grid, reqdb=0):
	 a=0
	 if reqdb==1:
			if debug==1:
				 a=1
			else:
				 a=0
	 if reqdb==2:
			if debug==2:
				 a=1
			else:
				 a=0
	 if reqdb==0:
			a=1
			
	 if a==1:
			print(grid[0][0], grid[0][1], grid[0][2], grid[0][3])
			print(grid[1][0], grid[1][1], grid[1][2], grid[1][3])
			print(grid[2][0], grid[2][1], grid[2][2], grid[2][3])
			print(grid[3][0], grid[3][1], grid[3][2], grid[3][3])
			print("-------")

def gv_seq(current_seq, target_len, current_list):
	if len(current_seq) == target_len:
		current_list.append(current_seq)
		return
	for char in allowed:
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


for length in range(1,5):
	for start_char in allowed:
		list_name = f"al_{start_char}{length}"
		current_list = []
		gv_seq(start_char, length, current_list)
		wasd_lists[list_name] = current_list
		print(list_name)

# CYCLEEEEEEEEEEEEEE

grid_start = [
[ 1, 2, 3 , 4 ],
[ 5, 6, 7, 8 ],
[ 9, "a", "b", "c" ],
[ "d", "e", "f", "_" ]
]



for label, data_list in wasd_lists.items():
		
		# label ------> 'al_w1', 'al_a1'...
		# data_list --> ['wwww', 'wwwa'...]
		
		print(f"Opening folder: {label}\n")
		
		for combo in data_list:
			
			pr = 3
			pc = 3
				
			grid = [
			[ 1, 2, 3 , 4 ],
			[ 5, 6, 7, 8 ],
			[ 9, "a", "b", "c" ],
			[ "d", "e", "f", "_" ]
			]
		
			for item_combo in combo:
				
				if item_combo=='w':
						grid[(pr+0)%4][pc] = grid[(pr+1)%4][pc]
						grid[(pr+1)%4][pc] = grid[(pr+2)%4][pc]
						grid[(pr+2)%4][pc] = grid[(pr+3)%4][pc]
						grid[(pr-1)%4][pc] = "_"
						visualize(grid, 2)
						pr=(pr-1)%4
		 
			 
				if item_combo=='s':
						grid[(pr-0)%4][pc] = grid[(pr-1)%4][pc]
						grid[(pr-1)%4][pc] = grid[(pr-2)%4][pc]
						grid[(pr-2)%4][pc] = grid[(pr-3)%4][pc]
						grid[(pr+1)%4][pc] = "_"
						visualize(grid, 2)
						pr=(pr+1)%4
			 
				if item_combo=='a':
						grid[pr][(pc+0)%4] = grid[pr][(pc+1)%4]
						grid[pr][(pc+1)%4] = grid[pr][(pc+2)%4]
						grid[pr][(pc+2)%4] = grid[pr][(pc+3)%4]
						grid[pr][(pc-1)%4]= "_"
						visualize(grid, 2)
						pc=(pc-1)%4
		 
			 
				if item_combo=='d':
						grid[pr][(pc-0)%4] = grid[pr][(pc-1)%4]
						grid[pr][(pc-1)%4] = grid[pr][(pc-2)%4]
						grid[pr][(pc-2)%4] = grid[pr][(pc-3)%4]
						grid[pr][(pc+1)%4]= "_"
						visualize(grid, 2)
						pc=(pc+1)%4
					
			diff_count = 0
		
			for sub_grid_start, sub_grid in zip(grid_start, grid):
				for item_grid_start, item_grid in zip(sub_grid_start, sub_grid):
					if item_grid_start != item_grid:
						diff_count += 1
					
			if diff_count == 2:
					print("COMBINATION:",combo)
					visualize(grid, 1)
					print("DIFFERENCES:",diff_count,"\n") 
					printd("■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")
					printd("")



print("finito\n\n")







