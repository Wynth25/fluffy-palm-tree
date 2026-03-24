import itertools

debug = 1

def printd(content):
	if debug == 1:
		print(content)
	if debug == 2:
		print(content)

def visualize(grid, reqdb=0):
	 if reqdb==1:
			if debug==2:
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



allowed = ['w', 'a', 's', 'd']
wasd_lists = {}

for length in range(1, 4):
	
		for start_char in allowed:
				list_name = f"al_{start_char}{length}"
				suffixes = itertools.product(allowed, repeat=length-1)
				current_list = []
				
				for suffix_tuple in suffixes:
						full_string = start_char + "".join(suffix_tuple)
						current_list.append(full_string)
						
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
		
		print(f"Opening folder: {label}")
		
		for combo in data_list:
			
			printd(combo)
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
						visualize(grid, 1)
						pr=(pr-1)%4
		 
			 
				if item_combo=='s':
						grid[(pr-0)%4][pc] = grid[(pr-1)%4][pc]
						grid[(pr-1)%4][pc] = grid[(pr-2)%4][pc]
						grid[(pr-2)%4][pc] = grid[(pr-3)%4][pc]
						grid[(pr+1)%4][pc] = "_"
						visualize(grid, 1)
						pr=(pr+1)%4
			 
				if item_combo=='a':
						grid[pr][(pc+0)%4] = grid[pr][(pc+1)%4]
						grid[pr][(pc+1)%4] = grid[pr][(pc+2)%4]
						grid[pr][(pc+2)%4] = grid[pr][(pc+3)%4]
						grid[pr][(pc-1)%4]= "_"
						visualize(grid, 1)
						pc=(pc-1)%4
		 
			 
				if item_combo=='d':
						grid[pr][(pc-0)%4] = grid[pr][(pc-1)%4]
						grid[pr][(pc-1)%4] = grid[pr][(pc-2)%4]
						grid[pr][(pc-2)%4] = grid[pr][(pc-3)%4]
						grid[pr][(pc+1)%4]= "_"
						visualize(grid, 1)
						pc=(pc+1)%4
					
			diff_count = 0
		
			for sub_grid_start, sub_grid in zip(grid_start, grid):
				for item_grid_start, item_grid in zip(sub_grid_start, sub_grid):
					if item_grid_start != item_grid:
						diff_count += 1
					
			if diff_count != 0:
					print("\nCOMBINATION:",combo)
					visualize(grid)
					print("\nDIFFERENCES:",diff_count) 
					print("\n■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")

print("")
i = 0
while i < 10:
	print("\n")
	i += 1




'''

grid = [
[ 1, 2, 3 , 4 ],
[ 5, 6, 7, 8 ],
[ 9, "a", "b", "c" ],
[ "d", "e", "f", "_" ]
]

for i in action_list:





grid2test = [
[ 1, 0, 3 , 0 ],
[ 5, 6, 0, 8 ],
[ 9, "a", "b", "c" ],
[ "d", "e", "f", "_" ]
]

diff_count = 0
'''

