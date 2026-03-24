import itertools

# 1. Start with a LIST, not a dictionary
all_scrambled_grids = [] 

# --- YOUR LOOP ---
for label, data_list in wasd_lists.items():
    print(f"Processing folder: {label}")
    
    for combo in data_list:
        # ... (Your grid moving logic here) ...
        # ... (pr, pc, grid changes) ...

        # Flatten the grid
        flat_list = list(itertools.chain.from_iterable(grid))
        
        # Convert hex/underscore to numbers
        flat_list_num = [16 if x == '_' else x for x in flat_list]
        flat_list_num = [int(i, 16) if isinstance(i, str) else i for i in flat_list_num]
        
        # 2. APPEND to the list (Don't overwrite!)
        all_scrambled_grids.append(flat_list_num)

# --- OUTSIDE THE LOOP ---

print("Sorting...")
# 3. Sort the massive list of grids
all_scrambled_grids.sort()

print(f"Total grids sorted: {len(all_scrambled_grids)}")
print(f"Smallest Grid: {all_scrambled_grids[0]}")
print(f"Largest Grid:  {all_scrambled_grids[-1]}")
