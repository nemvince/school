import tkinter as tk
import datetime


class GameUI:
    def __init__(self, materials=None):
        self.materials = materials
        self.root = tk.Tk()
        self.root.title("Grid of Buttons")
        self.root.geometry("600x400")
        self.root.resizable(False, False)
        self.font = ("Arial", 14)
        self.buttons = [[None, None, None] for _ in range(3)]

        self.status_box = tk.Label(self.root, text="Status: OK")
        self.status_box.grid(
            row=4, column=0, columnspan=3, padx=5, pady=5, sticky="nsew"
        )
        self.status_box.config(bg="green", fg="white")
        self.status_box.config(font=self.font)

        self.material_box = tk.Label(self.root, text="placeholder")
        self.update_materials(self.materials)
        self.material_box.grid(
            row=3, column=0, columnspan=3, padx=5, pady=5, sticky="nsew"
        )
        self.material_box.config(font=self.font)

        self.message_box = tk.Text(self.root, height=6, width=30, state=tk.DISABLED)
        self.message_box.grid(
            row=5, column=0, columnspan=3, padx=5, pady=5, sticky="nsew"
        )

        self.message_box.config(font=self.font)

        # Configure row and column weights for resizing
        for i in range(3):
            self.root.grid_rowconfigure(i, weight=1)
            self.root.grid_columnconfigure(i, weight=1)

    def add_message(self, message):
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        self.message_box.config(state=tk.NORMAL)
        self.message_box.insert(tk.END, f"{current_time} - {message}\n")
        self.message_box.config(state=tk.DISABLED)
        self.message_box.see(tk.END)

    def update_materials(self, materials):
        self.material_box.config(text=f"Materials: {materials}")

    def add_button(self, i, j, text, command):
        self.buttons[i][j] = tk.Button(
            self.root,
            text=text,
            command=lambda i=i, j=j: command(),
            height=1,
        )
        self.buttons[i][j].grid(
            row=i, column=j, padx=5, pady=5, sticky="nsew"
        )  # Added 'sticky' option
        self.buttons[i][j].config(font=self.font)

    def run(self):
        self.root.mainloop()


ui = GameUI(["Iron", "Copper", "Gold"])
ui.add_button(0, 0, "Move", lambda: ui.add_message("Moving..."))
ui.add_button(0, 1, "Fire", lambda: ui.add_message("Firing..."))
ui.add_button(0, 2, "Build", lambda: ui.add_message("Building..."))
ui.add_button(1, 0, "Upgrade", lambda: ui.add_message("Upgrading..."))
ui.run()
