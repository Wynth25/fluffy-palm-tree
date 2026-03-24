import random
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.core.window import Window

# --- CONFIGURATION ---
# Set background to dark grey so you can see the text
Window.clearcolor = (0.1, 0.1, 0.1, 1)

# Game State
grid = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, "a", "b", "c"],
    ["d", "e", "f", "_"]
]

# Player coordinates (Row, Column)
pr = 3
pc = 3

class GameLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 20
        self.spacing = 10

        # --- Top: The Game Grid (4x4) ---
        self.board_grid = GridLayout(cols=4, spacing=5, size_hint=(1, 0.7))
        self.cells = []  # List to hold the label widgets

        # Create 16 labels for the grid
        for r in range(4):
            row_cells = []
            for c in range(4):
                lbl = Label(
                    text=str(grid[r][c]),
                    font_size='30sp',
                    bold=True,
                    color=(0, 1, 0, 1)  # Green text
                )
                self.board_grid.add_widget(lbl)
                row_cells.append(lbl)
            self.cells.append(row_cells)
        
        self.add_widget(self.board_grid)

        # --- Middle: Status Label ---
        self.status_lbl = Label(text="Ready", size_hint=(1, 0.1), font_size='20sp')
        self.add_widget(self.status_lbl)

        # --- Bottom: Controls (D-Pad style) ---
        controls = GridLayout(cols=3, size_hint=(1, 0.2), spacing=10)
        
        # Row 1
        controls.add_widget(Label()) # Empty
        controls.add_widget(Button(text="UP", on_press=lambda x: self.move('w')))
        controls.add_widget(Label()) # Empty
        
        # Row 2
        controls.add_widget(Button(text="LEFT", on_press=lambda x: self.move('a')))
        controls.add_widget(Button(text="SHUFFLE", background_color=(1, 0, 0, 1), on_press=self.start_shuffle))
        controls.add_widget(Button(text="RIGHT", on_press=lambda x: self.move('d')))

        # Row 3
        controls.add_widget(Label()) # Empty
        controls.add_widget(Button(text="DOWN", on_press=lambda x: self.move('s')))
        controls.add_widget(Label()) # Empty

        self.add_widget(controls)

    def update_ui(self):
        """Syncs the visual labels with the grid data"""
        for r in range(4):
            for c in range(4):
                val = str(grid[r][c])
                self.cells[r][c].text = val
                
                # Highlight the empty spot ("_") vs numbers
                if val == "_":
                    self.cells[r][c].text = "[ _ ]" # Make it more visible
                    self.cells[r][c].color = (1, 0.2, 0.2, 1) # Redish
                else:
                    self.cells[r][c].color = (0, 1, 0, 1) # Bright Green

    def start_shuffle(self, instance):
        self.status_lbl.text = "Shuffling..."
        allowed = ['w', 'a', 's', 'd']
        # Reduced to 10 moves for faster shuffle
        self.shuffle_moves = random.choices(allowed, k=10)
        Clock.schedule_interval(self.execute_shuffle_step, 0.1)

    def execute_shuffle_step(self, dt):
        if self.shuffle_moves:
            move = self.shuffle_moves.pop(0)
            self.move(move)
        else:
            self.status_lbl.text = "Go!"
            return False # Stop the clock

    def move(self, direction):
        global pr, pc, grid
        
        # Logic copied from your original script
        if direction == 'w':
            grid[(pr+0)%4][pc] = grid[(pr+1)%4][pc]
            grid[(pr+1)%4][pc] = grid[(pr+2)%4][pc]
            grid[(pr+2)%4][pc] = grid[(pr+3)%4][pc]
            grid[(pr-1)%4][pc] = "_"
            pr = (pr-1)%4

        elif direction == 's':
            grid[(pr-0)%4][pc] = grid[(pr-1)%4][pc]
            grid[(pr-1)%4][pc] = grid[(pr-2)%4][pc]
            grid[(pr-2)%4][pc] = grid[(pr-3)%4][pc]
            grid[(pr+1)%4][pc] = "_"
            pr = (pr+1)%4

        elif direction == 'a':
            grid[pr][(pc+0)%4] = grid[pr][(pc+1)%4]
            grid[pr][(pc+1)%4] = grid[pr][(pc+2)%4]
            grid[pr][(pc+2)%4] = grid[pr][(pc+3)%4]
            grid[pr][(pc-1)%4] = "_"
            pc = (pc-1)%4

        elif direction == 'd':
            grid[pr][(pc-0)%4] = grid[pr][(pc-1)%4]
            grid[pr][(pc-1)%4] = grid[pr][(pc-2)%4]
            grid[pr][(pc-2)%4] = grid[pr][(pc-3)%4]
            grid[pr][(pc+1)%4] = "_"
            pc = (pc+1)%4

        self.update_ui()

class PuzzleApp(App):
    def build(self):
        game = GameLayout()
        game.update_ui()
        return game

if __name__ == '__main__':
    PuzzleApp().run()
