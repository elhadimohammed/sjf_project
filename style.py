
from tkinter import ttk

def apply_style(btn_create, btn_run):
    style = ttk.Style()
    style.theme_use("clam")

    HEADER_BG = "#3F51B5"  # Indigo
    HEADER_FG = "#FFFFFF"
    BTN_PRIMARY_BG = "#1976D2"  # Blue
    BTN_PRIMARY_FG = "#FFFFFF"
    BTN_SUCCESS_BG = "#00897B"  # Teal
    BTN_SUCCESS_FG = "#FFFFFF"

    style.configure("Treeview.Heading",
                    font=("Arial", 10, "bold"),
                    background=HEADER_BG,
                    foreground=HEADER_FG)
    style.configure("Treeview", font=("Arial", 9), rowheight=25)

    btn_create.config(font=("Arial", 10, "bold"),
                      bg=BTN_PRIMARY_BG, fg=BTN_PRIMARY_FG,
                      activebackground=BTN_PRIMARY_BG)
    btn_run.config(font=("Arial", 10, "bold"),
                   bg=BTN_SUCCESS_BG, fg=BTN_SUCCESS_FG,
                   activebackground=BTN_SUCCESS_BG)
