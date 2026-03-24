import ui
import random
from objc_util import ObjCClass

#LLM used to generate UI

# --- HAPTICS SETUP (Native iOS) ---
def trigger_haptic(style='light'):
    try:
        # Access iOS native UIImpactFeedbackGenerator
        Generator = ObjCClass('UIImpactFeedbackGenerator').alloc().initWithStyle_(0 if style=='light' else 1)
        Generator.prepare()
        Generator.impactOccurred()
    except:
        pass # Fails silently on iPads or very old devices

# --- GAME LOGIC ---
grid = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, "a", "b", "c"],
    ["d", "e", "f", "_"]
]
pr, pc = 3, 3 

# --- COLORS (OLED Dark Mode) ---
BG_COLOR = '#000000'       # Pure Black
TILE_COLOR = '#1c1c1e'     # Dark Grey
TEXT_COLOR = '#32d74b'     # Neon Green
CURSOR_COLOR = '#ff453a'   # Red
BUTTON_COLOR = '#2c2c2e'   # Button Grey

class PuzzleGame(ui.View):
    def __init__(self):
        self.background_color = BG_COLOR
        self.buttons = []
        self.shuffle_moves = []
        
        screen_w, screen_h = ui.get_screen_size()
        
        # --- LAYOUT ---
        top_pad = 80 
        side_margin = 20
        
        # Quit Button (Top Right)
        quit_btn_size = 30
        self.quit_btn = ui.Button(title='✕')
        self.quit_btn.frame = (screen_w - quit_btn_size - 20, 40, quit_btn_size, quit_btn_size)
        self.quit_btn.tint_color = 'gray'
        self.quit_btn.action = self.quit_game
        self.add_subview(self.quit_btn)

        # Calculate Grid Tile Size
        available_width = screen_w - (side_margin * 2)
        tile_gap = 6
        tile_size = (available_width - (tile_gap * 3)) / 4 #4
        
        # --- GRID ---
        self.grid_container = ui.View()
        self.grid_container.frame = (side_margin, top_pad, available_width, available_width)
        self.add_subview(self.grid_container)

        for r in range(4):
            row_btns = []
            for c in range(4):
                btn = ui.Button()
                x_pos = c * (tile_size + tile_gap)
                y_pos = r * (tile_size + tile_gap)
                btn.frame = (x_pos, y_pos, tile_size, tile_size)
                btn.background_color = TILE_COLOR
                btn.tint_color = TEXT_COLOR
                btn.font = ('<system-bold>', 30)
                btn.corner_radius = 12
                btn.touch_enabled = False
                
                self.grid_container.add_subview(btn)
                row_btns.append(btn)
            self.buttons.append(row_btns)

        # --- STATUS LABEL ---
        self.status_lbl = ui.Label()
        lbl_y = top_pad + available_width + 30
        self.status_lbl.frame = (0, lbl_y, screen_w, 40)
        self.status_lbl.text_color = 'white'
        self.status_lbl.alignment = ui.ALIGN_CENTER
        self.status_lbl.font = ('<system>', 22)
        self.status_lbl.text = "Ready"
        self.add_subview(self.status_lbl)

        # --- D-PAD CONTROLS ---
        btn_size = 75
        control_y_start = screen_h - 320 
        cx = screen_w / 2
        pad_gap = 10
        
        controls = [
            ("W", 0, 0, 'w'),                           # UP
            ("A", -(btn_size + pad_gap), btn_size + pad_gap, 'a'), # LEFT
            ("D", (btn_size + pad_gap), btn_size + pad_gap, 'd'),  # RIGHT
            ("S", 0, (btn_size + pad_gap) * 2, 's'),    # DOWN
        ]

        for text, dx, dy, arg in controls:
            btn = ui.Button(title=text)
            btn.frame = (cx - (btn_size/2) + dx, control_y_start + dy, btn_size, btn_size)
            btn.background_color = BUTTON_COLOR
            btn.tint_color = 'white'
            btn.corner_radius = btn_size / 2
            btn.action = lambda sender, d=arg: self.move(d)
            self.add_subview(btn)

        # --- SHUFFLE BUTTON ---
        self.shuffle_btn = ui.Button(title="SHUFFLE")
        self.shuffle_btn.frame = (cx - (btn_size/2), control_y_start + btn_size + pad_gap, btn_size, btn_size)
        self.shuffle_btn.background_color = '#ff9f0a'
        self.shuffle_btn.tint_color = 'black'
        self.shuffle_btn.corner_radius = btn_size / 2
        self.shuffle_btn.action = self.start_shuffle
        self.add_subview(self.shuffle_btn)

        self.update_grid_ui()

    def quit_game(self, sender):
        self.close()

    def update_grid_ui(self):
        for r in range(4):
            for c in range(4):
                val = str(grid[r][c])
                btn = self.buttons[r][c]
                
                if val == "_":
                    btn.title = ""
                    btn.background_color = BG_COLOR 
                    btn.border_width = 2
                    btn.border_color = CURSOR_COLOR
                else:
                    btn.title = val
                    btn.background_color = TILE_COLOR
                    btn.border_width = 0

    def move(self, direction):
        global pr, pc
        moved = False
        
        if direction == 'w':
            grid[(pr+0)%4][pc] = grid[(pr+1)%4][pc]
            grid[(pr+1)%4][pc] = grid[(pr+2)%4][pc]
            grid[(pr+2)%4][pc] = grid[(pr+3)%4][pc]
            grid[(pr-1)%4][pc] = "_"
            pr = (pr-1)%4
            moved = True
        elif direction == 's':
            grid[(pr-0)%4][pc] = grid[(pr-1)%4][pc]
            grid[(pr-1)%4][pc] = grid[(pr-2)%4][pc]
            grid[(pr-2)%4][pc] = grid[(pr-3)%4][pc]
            grid[(pr+1)%4][pc] = "_"
            pr = (pr+1)%4
            moved = True
        elif direction == 'a':
            grid[pr][(pc+0)%4] = grid[pr][(pc+1)%4]
            grid[pr][(pc+1)%4] = grid[pr][(pc+2)%4]
            grid[pr][(pc+2)%4] = grid[pr][(pc+3)%4]
            grid[pr][(pc-1)%4] = "_"
            pc = (pc-1)%4
            moved = True
        elif direction == 'd':
            grid[pr][(pc-0)%4] = grid[pr][(pc-1)%4]
            grid[pr][(pc-1)%4] = grid[pr][(pc-2)%4]
            grid[pr][(pc-2)%4] = grid[pr][(pc-3)%4]
            grid[pr][(pc+1)%4] = "_"
            pc = (pc+1)%4
            moved = True
            
        if moved:
            self.update_grid_ui()
            trigger_haptic()

    def start_shuffle(self, sender):
        self.status_lbl.text = "Shuffling..."
        self.shuffle_btn.enabled = False
        allowed = ['w', 'a', 's', 'd']
        self.shuffle_moves = random.choices(allowed, k=15)
        self.run_shuffle_step()

    def run_shuffle_step(self):
        if len(self.shuffle_moves) > 0:
            move = self.shuffle_moves.pop(0)
            self.move(move)
            ui.delay(self.run_shuffle_step, 0.08)
        else:
            self.status_lbl.text = "Go!"
            self.shuffle_btn.enabled = True
            trigger_haptic('heavy')

if __name__ == '__main__':
    v = PuzzleGame()
    v.present('fullscreen', hide_title_bar=True)
