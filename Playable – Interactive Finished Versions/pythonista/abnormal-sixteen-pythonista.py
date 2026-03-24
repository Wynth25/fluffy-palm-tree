import ui
import time
import random

class GridGame(ui.View):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.background_color = 'white'
        
        # 1. SETUP DATA
        self.grid = [
            [ 1, 2, 3 , 4 ],
            [ 5, 6, 7, 8 ],
            [ 9, "a", "b", "c" ],
            [ "d", "e", "f", "_" ]
        ]
        self.pr = 3
        self.pc = 3
        self.labels = []
        
        # 2. SETUP UI (Buttons & Labels)
        # We need to know the screen size to place things correctly
        sw, sh = ui.get_screen_size()
        
        # --- A. The Grid ---
        # We make the grid width based on the screen width
        grid_w = sw - 20 
        cell_w = grid_w / 4
        
        grid_container = ui.View(frame=(10, 50, grid_w, grid_w))
        
        for r in range(4):
            row_labels = []
            for c in range(4):
                l = ui.Label()
                l.frame = (c*cell_w, r*cell_w, cell_w-4, cell_w-4)
                l.alignment = ui.ALIGN_CENTER
                l.background_color = '#eeeeee'
                l.font = ('<system-bold>', 24)
                l.corner_radius = 8
                grid_container.add_subview(l)
                row_labels.append(l)
            self.labels.append(row_labels)
        
        self.add_subview(grid_container)
        
        # --- B. The Buttons ---
        # Calculate center positions below the grid
        cx = sw / 2 
        cy = sh / 2 + 100 # Push it down a bit
        
        def make_btn(title, x, y, action_name):
            b = ui.Button(title=title)
            # Center the button on x,y
            b.frame = (x - 40, y - 40, 80, 80)
            b.background_color = '#007aff'
            b.tint_color = 'white'
            b.corner_radius = 40
            b.action = self.button_tapped
            b.name = action_name 
            self.add_subview(b)
            
        make_btn("Up", cx, cy - 100, 'w')
        make_btn("Down", cx, cy + 100, 's')
        make_btn("Left", cx - 100, cy, 'a')
        make_btn("Right", cx + 100, cy, 'd')

        # 3. INITIAL UPDATE
        self.update_display()
        
        # 4. START SHUFFLE (Delayed)
        ui.delay(self.run_shuffle_animation, 1.0)

    def update_display(self):
        for r in range(4):
            for c in range(4):
                val = str(self.grid[r][c])
                self.labels[r][c].text = val
                if val == "_":
                    self.labels[r][c].background_color = '#ffaaaa'
                else:
                    self.labels[r][c].background_color = '#dddddd'

    def process_move(self, i):
        grid = self.grid
        pr, pc = self.pr, self.pc
        
        if i == 'w':
            grid[(pr+0)%4][pc] = grid[(pr+1)%4][pc]
            grid[(pr+1)%4][pc] = grid[(pr+2)%4][pc]
            grid[(pr+2)%4][pc] = grid[(pr+3)%4][pc]
            grid[(pr-1)%4][pc] = "_"
            self.pr = (pr-1)%4

        elif i == 's':
            grid[(pr-0)%4][pc] = grid[(pr-1)%4][pc]
            grid[(pr-1)%4][pc] = grid[(pr-2)%4][pc]
            grid[(pr-2)%4][pc] = grid[(pr-3)%4][pc]
            grid[(pr+1)%4][pc] = "_"
            self.pr = (pr+1)%4

        elif i == 'a':
            grid[pr][(pc+0)%4] = grid[pr][(pc+1)%4]
            grid[pr][(pc+1)%4] = grid[pr][(pc+2)%4]
            grid[pr][(pc+2)%4] = grid[pr][(pc+3)%4]
            grid[pr][(pc-1)%4] = "_"
            self.pc = (pc-1)%4

        elif i == 'd':
            grid[pr][(pc-0)%4] = grid[pr][(pc-1)%4]
            grid[pr][(pc-1)%4] = grid[pr][(pc-2)%4]
            grid[pr][(pc-2)%4] = grid[pr][(pc-3)%4]
            grid[pr][(pc+1)%4] = "_"
            self.pc = (pc+1)%4
            
        self.update_display()

    def button_tapped(self, sender):
        self.process_move(sender.name)

    def run_shuffle_animation(self):
        # We need a recursive or threaded approach for animations in UI
        # This simple loop might block UI, so we use ui.delay for smooth effect
        allowed = ['w', 'a', 's', 'd']
        moves = random.choices(allowed, k=0)
        
        def step_shuffle(moves_left):
            if not moves_left:
                return
            move = moves_left.pop(0)
            self.process_move(move)
            # Schedule next step in 0.05 seconds
            ui.delay(lambda: step_shuffle(moves_left), 0.05)
            
        step_shuffle(moves)

# Run it
v = GridGame()
v.present('fullscreen')
