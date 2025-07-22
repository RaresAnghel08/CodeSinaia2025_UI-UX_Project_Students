import tkinter as tk
from tkinter import Canvas, Entry, Text, Button, PhotoImage, messagebox
from pathlib import Path
import json
import webbrowser
import os

from ux.messages import send_message, clear_chat
from ux.json_handling import load_chat, save_chat

ASSETS_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "assets")

figma_link = "https://www.figma.com/design/cuNtrpjCHpGHbauYEfwbeJ/CodeSinaia_UI_Students?node-id=0-1&t=mcJ6qFdLuzdR6EcY-1"

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def open_app():
    
    # daca nu exista directorul data, se creeaza unul nou
    if not Path("data").exists():
        Path("data").mkdir(parents=True, exist_ok=True)
    
    # daca nu exista fisierul json, se creeaza unul nou
    if not Path("data/history.json").exists():
        with open("data/history.json", "w", encoding="utf-8") as f:
            json.dump([], f, indent=2, ensure_ascii=False)
    
    root = tk.Tk()
    
    #TODO: de ce nu merge
    # upper left image logo
    root.iconbitmap('code_sinaia_logo.ico')  # Ensure you have a code_sinaia_logo.ico file in the same directory
    
    window_width = 800
    window_height = 600
    
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    display_x = (screen_width // 2) - (window_width // 2)
    display_y = (screen_height // 2) - (window_height // 2)
    root.geometry(f"{window_width}x{window_height}+{display_x}+{display_y}")

    root.configure(bg="#D9D9D9")
    root.title("Code Sinaia 2025 - Chatbot App")
    canvas = Canvas(root, bg="#D9D9D9", height=600, width=800, bd=0, highlightthickness=0, relief="ridge")
    canvas.place(x=0, y=0)

    # Background and layout
    canvas.create_rectangle(0.0, 0.0, 800.0, 600.0, fill="#D9D9D9", outline="")
    canvas.create_rectangle(30.0, 73.0, 770.0, 434.0, fill="#C5C5C5", outline="")

    # Chat log (Text widget)
    chat_log = Text(root, bg="#C5C5C5", bd=0, state=tk.DISABLED, wrap="word")
    chat_log.place(x=30.0, y=73.0, width=740.0, height=361.0)

    # Entry box
    entry = Entry(root, bd=0)
    entry.place(x=30.0, y=465.0, width=740.0, height=40.0)
    entry.configure(bg="#C5C5C5", font=("Inter", 14 * -1), highlightthickness=0, relief="flat")
    
    # Buttons
    def on_send():
        send_message(entry, chat_log)
    def on_clear():
        clear_chat(chat_log)
    def on_load():
        load_chat(chat_log)
    def on_save():
        save_chat(chat_log)
        
    root.bind('<Return>', lambda event=None: on_send()) # Send message on Enter key press
    root.resizable(False, False)
    root.mainloop()
